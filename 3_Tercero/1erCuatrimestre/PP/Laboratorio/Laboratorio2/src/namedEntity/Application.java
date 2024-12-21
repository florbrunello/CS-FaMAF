package namedEntity;
import namedEntity.category.*;
import namedEntity.heuristic.Heuristic;
import feed.*;
import java.util.*;


public class Application {

    public List<NamedEntity> main (Feed feed, Heuristic heuristic){
        List<NamedEntity> entitiesList = new ArrayList<NamedEntity>();

        for (Article article : feed.getArticleList()) {
            String text = article.getTitle();
            text = text + ". " + article.getText();

            for (String word : text.split(" ")) {
                if (heuristic.isEntity(word)) {
                    //chequeo categoría
                    String category = heuristic.getCategory(word);
                    //chequeo tema
                    String theme = heuristic.getTheme(word);
                    
                    int namedEntityIndex = searchEntities(word, entitiesList);
                    if (namedEntityIndex != -1) {
                        // si lo encuentra, incrementa la frecuencia
                        entitiesList.get(namedEntityIndex).incFrequency();
                    } 
                    else {
                        // primero vemos la categoría del objeto
                        if ("Person".equals(category)) {
                            // ahora vemos el tema
                            if ("Futbol".equals(theme)) {
                                PersonFutbol personFutbol = new PersonFutbol(word, 1, "id", "position");
                                entitiesList.add(personFutbol);
                            } else if ("Tenis".equals(theme)) {
                                PersonTenis personTenis = new PersonTenis(word, 1, "id", "position");
                                entitiesList.add(personTenis);
                            } else if ("Politics".equals(theme)) {
                                PersonPolitics personPolitics = new PersonPolitics(word, 1, "id");
                                entitiesList.add(personPolitics);
                            } else if ("Others".equals(theme)){
                                PersonOthers personOthers = new PersonOthers(word, 1, "id");
                                entitiesList.add(personOthers);
                            } else {
                                Person person = new Person(word, category, 1, "id");
                                entitiesList.add(person);
                            }
                        } 
                        else if ("Place".equals(category)) {
                            if("Others".equals(theme)) {
                                PlaceOthers placeOthers = new PlaceOthers(word, category, 1, "id");
                                entitiesList.add(placeOthers);
                            } else {
                                Place place = new Place(word, category, 1, "id");
                                entitiesList.add(place);
                            }
                        } 
                        else if ("Organization".equals(category)) {
                            if ("Others".equals(theme)) {
                                OrganizationOthers organizationOthers = new OrganizationOthers(word, category, 1, 
                                                                                            "id", 1,
                                                                                            "id");
                                entitiesList.add(organizationOthers);
                            } else {
                                Organization organization = new Organization(word, category, 1, 
                                                            "id", 1,
                                                            "id");
                                entitiesList.add(organization);
                            }
                        } else if ("Other".equals(category)) {
                            Other others = new Other(word, category, 1, "id");
                            entitiesList.add(others);
                        } 
                    }
                }
            }
        }
        return entitiesList;
    }
    
    public int searchEntities(String name, List<NamedEntity> entitiesList) {
        for (NamedEntity namedEntity : entitiesList) {
            if (namedEntity.getName().equals(name)) {
                // si lo encuentra, devuelve la posición
                return entitiesList.indexOf(namedEntity);
            }
        }
        return -1;
    } 

}
