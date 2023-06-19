package namedEntity.category;

import namedEntity.NamedEntity;

public class Person extends NamedEntity {
    private String id;

    public Person(String name, String category, int frequency, String id) {
        super(name, category, frequency);
        this.id = id;
    }

    public String getPerson() {
        return id;
    }

    public void setPerson(String id) {
        this.id = id;
    }
}