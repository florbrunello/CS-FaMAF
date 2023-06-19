package namedEntity.category;

public class Country extends Place{
    private String population;
    private String officialLanguage;

    public Country(String name, String category, int frequency, String place, String population, String officialLanguage) {
        super(name, category, frequency, place);
        this.population = population;
        this.officialLanguage = officialLanguage;
    }

    public String getCountryPopulation() {
        return population;
    }

    public String getCountryOfficialLanguage() {
        return officialLanguage;
    }

    public void setCountryPopulation(String population) {
        this.population = population;
    }  

    public void setCountryOfficialLanguage(String officialLanguage) {
        this.officialLanguage = officialLanguage;
    }
}