package namedEntity;

import namedEntity.category.Person;
import namedEntity.themes.Futbol;

public class PersonFutbol extends Person implements Futbol{
    String sports; 
    String theme;
    String position;
    
    public PersonFutbol(String name, int frequency, String id, String position) {
        super(name, "Person", frequency, id);
        this.sports = sports();
        this.theme = futbol();
        this.position = position;
    }

    public String sports() {
        return "sports";
    }

    public String futbol(){
        return "futbol";
    }

    public String getSports() {
        return sports;
    }

    public String getTheme() {
        return theme;
    }

    public void setPosition(String position) {
        this.position = position;
    }    
    
    public String getPosition() {
        return position;
    }

    @Override 
    public String toString() {
        return super.toString() + " " + theme;
    }
}
