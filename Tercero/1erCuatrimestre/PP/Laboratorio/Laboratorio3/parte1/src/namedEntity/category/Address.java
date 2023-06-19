package namedEntity.category;

public class Address extends Place {
    private String city; 
    private String neighborhood;
    private String street; 
    private int number;

    public Address(String name, String category, int frequency, String place, String city, String neighborhood, String street, int number) {
        super(name, category, frequency, place);
        this.city = city;
        this.neighborhood = neighborhood;
        this.street = street;
        this.number = number;
    }

    public void setAddressCity(String city) {
        this.city = city;
    }

    public String getAddressCity(){
        return city;
    }

    public void setAddressNeighborhood(String neighborhood) {
        this.neighborhood = neighborhood;
    }

    public String getAddressNeighborhood(){
        return neighborhood;
    }

    public void setAddressStreet(String street) {
        this.street = street;
    }

    public String getAddressStreet(){
        return street;
    }

    public void setAddressNumber(int number) {
        this.number = number;
    }

    public int getAddressNumber(){
        return number;
    }
    
}
