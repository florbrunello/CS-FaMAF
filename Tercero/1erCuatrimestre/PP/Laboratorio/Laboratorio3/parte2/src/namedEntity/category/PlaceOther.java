package namedEntity.category;

public class PlaceOther extends Place {
    private String aditionalInfo; 

    public PlaceOther(String name, String category, int frequency, String placeString, String aditionalInfo) {
        super(name, category, frequency, placeString);
        this.aditionalInfo = aditionalInfo;
    }

    public void setAditionalInfo(String aditionalInfo) {
        this.aditionalInfo = aditionalInfo;
    }

    public String getAditionalInfo() {
        return aditionalInfo;
    }
}