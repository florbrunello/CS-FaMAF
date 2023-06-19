package namedEntity.category;

import namedEntity.NamedEntity;

public class Event extends NamedEntity {
    private String canonicalForm;
    private int year; 
    private int month;
    private int day; 
    private String recurrent;

    public Event(String name, String category, int frequency, String cannonicalForm, int year, int month, int day, String recurrent) {
        super(name, category, frequency);
        this.canonicalForm = cannonicalForm;
        this.year = year;
        this.month = month;
        this.day = day;
        this.recurrent = recurrent;
    }

    public void setEventCanonicalForm(String canonicalForm) {
        this.canonicalForm = canonicalForm;
    }

    public String getEventCanonicalForm() {
        return canonicalForm;
    }

    public void setEventRecurrent(String recurrent) {
        this.recurrent = recurrent;
    }

    public String getEventRecurrent() {
        return recurrent;
    }

    public void setEventDate(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day; 
    }

    public String getEventDate() {
        return year + "-" + month + "-" + day; 
    }

}
