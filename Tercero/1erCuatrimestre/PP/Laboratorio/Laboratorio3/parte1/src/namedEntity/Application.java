package namedEntity;
import namedEntity.heuristic.Heuristic;
import feed.*;
import java.util.*;

import java.util.Arrays;
import java.util.List;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;


public class Application {

    public List<NamedEntity> main (Feed feed, Heuristic heuristic){
        List<NamedEntity> entitiesList = new ArrayList<NamedEntity>();

        SparkConf conf = new SparkConf()
            .setAppName("named-entities-counter")
            .setMaster("local")
            .set("spark.cores.max", "10");

        JavaSparkContext sc = new JavaSparkContext(conf);

        for (Article article : feed.getArticleList()) {
            JavaRDD<String> text = sc.parallelize(Arrays.asList(article.getTitle()));
            text = text.union(sc.parallelize(Arrays.asList(article.getText())));

            JavaPairRDD<String, Integer> words = text.flatMap(x -> Arrays.asList(x.split(" ")).iterator())
                                                        .mapToPair(x -> new Tuple2<>(x, 1))
                                                        .reduceByKey((x, y) -> x + y);

            List<Tuple2<String, Integer>> entityWords = words.filter((x) -> heuristic.isEntity(x._1()) 
                                                        && (("Person".equals(heuristic.getCategory(x._1())) && "Futbol".equals(heuristic.getTheme(x._1()))) 
                                                        || ("Person".equals(heuristic.getCategory(x._1())) && "Tenis".equals(heuristic.getTheme(x._1())))
                                                        || ("Person".equals(heuristic.getCategory(x._1())) && "Politics".equals(heuristic.getTheme(x._1())))
                                                        || ("Person".equals(heuristic.getCategory(x._1())) && "Others".equals(heuristic.getTheme(x._1())))
                                                        || ("Place".equals(heuristic.getCategory(x._1())) && "Others".equals(heuristic.getTheme(x._1())))
                                                        || ("Organization".equals(heuristic.getCategory(x._1())) && "Others".equals(heuristic.getTheme(x._1())))
                                                        || ("Person".equals(heuristic.getCategory(x._1())))
                                                        || ("Place".equals(heuristic.getCategory(x._1())))
                                                        || ("Organization".equals(heuristic.getCategory(x._1())))
                                                        || ("Other".equals(heuristic.getCategory(x._1())))))
                                                        .collect();

            // Agregar entityWords a la lista de entidades nombradas (entitiesList)
            for (Tuple2<String, Integer> y : entityWords) {
                NamedEntity namedEntity = new NamedEntity(y._1(), heuristic.getCategory(y._1()), y._2());
                entitiesList.add(namedEntity);
            }
        }

        // Reducir entitidades repetidas
        JavaRDD<NamedEntity> entitiesRDD = sc.parallelize(entitiesList);
        entitiesRDD = entitiesRDD.mapToPair(x -> new Tuple2<>(x.getName(), x))
                                    .reduceByKey((x, y) -> new NamedEntity(x.getName(), x.getCategory(), x.getFrequency() + y.getFrequency()))
                                    .map(x -> x._2());            
        
        entitiesList = entitiesRDD.collect();

        sc.close();
        return entitiesList;
    }
}
