package namedEntity.category;

public class City extends Place {
    private String country;
    private String capital;
    private String population;    

    public City(String name, String category, int frequency, String place, String country, String capital, String population) {
        super(name, category, frequency, place);
        this.country = country;
        this.capital = capital;
        this.population = population;
    }

    public String getCountry() {
        return country;
    }

    public String getCityCapital() {
        return capital;
    }

    public String getCityPopulation() {
        return population;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public void setCityCapital(String capital) {
        this.capital = capital;
    }

    public void setCityPopulation(String population) {
        this.population = population;
    }
}
