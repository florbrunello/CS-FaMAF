package namedEntity;

import namedEntity.category.*;
import namedEntity.themes.Others;

public class PlaceOthers extends Place implements Others{
    String theme;
    
    public PlaceOthers(String name, String category, int frequency, String id) {
        super(name, category, frequency, id);
        this.theme = others();
    }

    public String others(){
        return "other";
    }

    @Override 
    
    public String toString() {
        return super.toString() + " " + theme;
    }
}
