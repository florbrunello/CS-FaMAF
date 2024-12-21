package namedEntity.category;

import namedEntity.NamedEntity;

public class Place extends NamedEntity{
    private String stringPlace;

    public Place(String name, String category, int frequency, String stringPlace) {
        super(name, category, frequency);
        this.stringPlace = stringPlace;
    }

    public void setPlace(String stringPlace) {
        this.stringPlace = stringPlace;
    }

    public String getPlace(){
        return stringPlace;
    }
}