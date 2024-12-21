package namedEntity.category;

import namedEntity.NamedEntity;

public class Other extends NamedEntity{
    private String otherString;

    public Other(String name, String category, int frequency, String otherString) {
        super(name, category, frequency);
        this.otherString = otherString;
    }

    public void setOther(String otherString) {
        this.otherString = otherString;
    }

    public String getOther() {
        return otherString;
    }
}
