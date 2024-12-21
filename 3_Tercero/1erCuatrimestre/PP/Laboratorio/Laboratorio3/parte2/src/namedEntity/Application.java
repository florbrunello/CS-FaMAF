package namedEntity;
import namedEntity.category.*;
import namedEntity.heuristic.Heuristic;
import feed.*;
import java.util.ArrayList;
import java.util.*;

import org.apache.spark.sql.SparkSession;
import org.apache.spark.api.java.JavaRDD;
import java.util.stream.Collectors;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.JavaPairRDD;
import scala.Tuple2;


public class Application {

    public List<NamedEntity> entitiesCount(Feed feed, Heuristic heuristic){
        // Creo SparkSession
        SparkSession spark = SparkSession.builder()
                                        .appName("NamedEntitiesCount")
                                        .master("local")
                                        .getOrCreate();    

        // Creo contexto de Spark para Java
        JavaSparkContext sc = new JavaSparkContext(spark.sparkContext());
        
        spark.sparkContext().setLogLevel("ERROR");
        
        /* Parseo el feed a una lista de strings, donde se concatena el título y el texto de cada artículo,
        // para buscar entidades nombradas en ambos campos */
        List<String> text = feed.getArticleList().stream()
                .map(article -> article.getTitle() + " . " + article.getText()) 
                .collect(Collectors.toList());
        
        // Creo un RDD para paralelizar y distribuir la ejecución en el cluster
        JavaRDD<String> textRDD = sc.parallelize(text);

        // Spliteo las palabras extraídas de cada artículo y lo convierto a lista
        JavaRDD<String> words = textRDD.flatMap(txt -> Arrays.asList(txt.split(" ")).iterator());

        // Filtro las palabras que son entidades nombradas según la heurística
        JavaRDD<String> filteredEntities = words.filter(w -> heuristic.isEntity(w));

        /* Mapeo cada palabra a una tupla key-value (word, 1), para luego poder condensar las entidades a una sola tupla 
        con su conteo de apariciones */
        JavaPairRDD<String, Integer> pairEntities = filteredEntities.mapToPair(entity -> new Tuple2<>(entity, 1));

        // Reduzco las entidades a una sola tupla con su conteo de apariciones
        JavaPairRDD<String, Integer> reducedEntities = pairEntities.reduceByKey((a, b) -> a + b);

        /* Mapeo las entidades a objetos NamedEntity en una lista. Si no matchea con alguna palabra del diccionario, por 
        más que haya sido considerado entidad por la heurística, no se crea un objeto NamedEntity */
        List<NamedEntity> entitiesList = reducedEntities.map(tuple -> {
            String name = tuple._1();
            int frequency = tuple._2();
            String category = heuristic.getCategory(name);
            String theme = heuristic.getTheme(name);

            if ("Person".equals(category)) {
                if ("Futbol".equals(theme)) {
                    return new PersonFutbol(name, frequency, "id", "position");
                } else if ("Tenis".equals(theme)) {
                    return new PersonTenis(name, frequency, "id", "position");
                } else if ("Politics".equals(theme)) {
                    return new PersonPolitics(name, frequency, "id");
                } else if ("Others".equals(theme)) {
                    return new PersonOthers(name, frequency, "id");
                } else {
                    return new Person(name, category, frequency, "id");
                }
            } else if ("Place".equals(category)) {
                if ("Others".equals(theme)) {
                    return new PlaceOthers(name, category, frequency, "id");
                } else {
                    return new Place(name, category, frequency, "id");
                }
            } else if ("Organization".equals(category)) {
                if ("Others".equals(theme)) {
                    return new OrganizationOthers(name, category, frequency, "id", 1, "id");
                } else {
                    return new Organization(name, category, frequency, "id", 1, "id");
                }
            } else if ("Other".equals(category)) {
                return new Other(name, category, frequency, "id");
            } else {
                // Si no matchea con ninguna categoría, no creamos un objeto 
                // NamedEntity, para mantener el comportamiento del lab anterior, donde decidimos hacer esto
                return null;
            }
        }).filter(namedEntity -> namedEntity != null) // Filter para eliminar los nulls, i.e entidades que no están en el diccionario.
        .collect();

        // Detenemos el SparkContext
        sc.stop();
        sc.close();
        // Detenemos la SparkSession
        spark.stop();
        
        return entitiesList;   
    }

    private List<Tuple2<Article,Integer>> getIndex(Feed feed) {
        List<Tuple2<Article,Integer>> articlesPair = new ArrayList<>();
        for (Article article : feed.getArticleList()) {
            articlesPair.add(new Tuple2<>(article, feed.getArticleList().indexOf(article)));
        }   
        return articlesPair;
    }
    
    public List<Tuple2<Article,Integer>> articleRecovery(String word, Feed feed) {
        List<Tuple2<Article,Integer>> articlesPair = new ArrayList<>();
        articlesPair = getIndex(feed);

        // Creo SparkSession
        SparkSession spark = SparkSession.builder()
                                        .appName("Article-Recovery")
                                        .master("local")
                                        .getOrCreate();    

        spark.sparkContext().setLogLevel("ERROR");
        
        // Creo contexto de Spark para Java
        JavaSparkContext sc = new JavaSparkContext(spark.sparkContext());
        
        //paralelizar los articulos
        JavaRDD<Tuple2<Article,Integer>> articleRDD = sc.parallelize(articlesPair);

       
        //por cada uno, mapeo la funcion q te toma el titulo y el texto, pero también el articulo de donde lo obtuve (para poder recuperarlo) . Frecuencia 
        JavaPairRDD<String,Integer> articleTuple = articleRDD.mapToPair(article -> 
                                                                    new Tuple2<>(article._1().getTitle().toLowerCase() + " " + article._1().getText().toLowerCase(), 
                                                                    article._2()));
        

        //Mapeo cada articleTuple (str, index) a una tupla (word, (index, 1)), donde word es una palabra de str
        JavaPairRDD<String, Tuple2<Integer, Integer>> triple = articleTuple.flatMapToPair(tuple -> {
            String[] words = tuple._1().split(" ");
            Integer index = tuple._2();
            return Arrays.stream(words)
                    .map(artWord -> new Tuple2<>(artWord, new Tuple2<>(index, 1)))
                    .iterator();
        });
        
        // Filtrar por la palabra que se quiere buscar (parámetro word)) 
        JavaPairRDD<String, Tuple2<Integer, Integer>> filteredTriple = triple.filter(tuple -> tuple._1().equals(word));

        // Si no se encontraron resultados, devuelvo una lista vacía
        if (filteredTriple.isEmpty()) {
            System.out.println("No se encontraron resultados para la palabra buscada.");
            return new ArrayList<>();
        }

        // mapeo a una tupla (index, frecuencia)
        JavaPairRDD<Integer, Integer> indexFreq = filteredTriple.mapToPair(tuple -> {
            Integer index = tuple._2()._1();
            Integer frequency = tuple._2()._2();
            return new Tuple2<>(index, frequency);
        });

        // Reduzco por key (index) sumando las frecuencias
        JavaPairRDD<Integer, Integer> reducedIndexFreq = indexFreq.reduceByKey((a, b) -> a + b);
        
        // Ahora ya tenemos cada índice de cada artículo que contiene la palabra buscada, y la frecuencia de la palabra en ese artículo.
        // Ordenamos por frecuencia, de mayor a menor, y devolvemos los artículos en orden de frecuencia.
        JavaPairRDD<Integer, Integer> sortedPair = reducedIndexFreq.mapToPair(pair -> new Tuple2<>(pair._2(), pair._1()))
                .sortByKey(false)
                .mapToPair(pair -> new Tuple2<>(pair._2(), pair._1()));

        // Por último, armamos la lista de tuplas (Article, frecuencia) 'articleList', que es lo que retorna la función.
        List<Tuple2<Article, Integer>> articleList = sortedPair.map(tuple -> {
            int index = tuple._1().intValue();
            return new Tuple2<>(feed.getArticle(index), tuple._2());
        }).collect();

        // Detenemos el SparkContext
        sc.stop();
        sc.close();
        // Detenemos la SparkSession
        spark.stop();
        return articleList;
    }
}
