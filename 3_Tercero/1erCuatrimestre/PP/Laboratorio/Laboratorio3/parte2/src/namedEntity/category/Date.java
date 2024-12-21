package namedEntity.category;

import namedEntity.NamedEntity;

public class Date extends NamedEntity{
    private int year; 
    private int month;
    private int day; 
    //canoncia 
    

    public Date(String name, String category, int frequency, int year, int month, int day) {
        super(name, category, frequency);
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public void setDate(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day; 
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year; 
    }

    public int getMonth() {
        return month; 
    }

    public void setMonth(int month) {
        this.month = month; 
    }

    public int getDay() {
        return day; 
    }

    public void setDay(int day) {
        this.day = day; 
    }

    public String getDate() {
        return year + "-" + month + "-" + day; 
    }
}
