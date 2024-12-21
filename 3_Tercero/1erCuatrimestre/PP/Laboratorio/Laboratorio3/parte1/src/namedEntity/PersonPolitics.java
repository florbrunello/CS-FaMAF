package namedEntity;

import namedEntity.category.*;
import namedEntity.themes.Politics;

public class PersonPolitics extends Person implements Politics{
    String theme; 

    public PersonPolitics(String name, int frequency, String id) {
        super(name, "Person", frequency, id);
        this.theme = politics();
    }

    public String politics() {
        return "politics";
    }
    
    public String getTheme() {
        return theme;
    }

    @Override
    public String toString() {
        return super.toString() + " " + theme;
    }
}
