package namedEntity;
import namedEntity.category.Person;
import namedEntity.themes.Tenis;

public class PersonTenis extends Person implements Tenis{
    String sports;
    String theme;
    String position;
    
    public PersonTenis(String name, int frequency, String id, String position) {
        super(name, "Person", frequency, id);
        this.sports = sports();
        this.theme = tenis();
        this.position = position;
    }

    public String sports() {
        return "sports";
    }

    public String tenis(){
        return "tenis";
    }

    public String getSports() {
        return sports;
    }

    public String getTheme() {
        return theme;
    }

    public String getPosition() {
        return position;
    }
    
    public void setPosition(String position) {
        this.position = position;
    }

    @Override 
    public String toString() {
        return super.toString() + " " + theme;
    }

}
