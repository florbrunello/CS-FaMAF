package namedEntity;
import namedEntity.category.Person;
import namedEntity.themes.Others;

public class PersonOthers extends Person implements Others{
    String theme;
    String position;
    
    public PersonOthers(String name, int frequency, String id) {
        super(name, "Other", frequency, id);
        this.theme = others();
    }

    public String others(){
        return "others";
    }

    @Override 
    
    public String toString() {
        return super.toString() + " " + theme;
    }
}
