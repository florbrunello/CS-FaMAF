package namedEntity;
import namedEntity.category.Organization;
import namedEntity.themes.Others;

public class OrganizationOthers extends Organization implements Others {
    String theme;

    public OrganizationOthers(String name, String category, int frequency, String canonicalForm, int numberOfMembers,
    String organizationType) {
        super(name, category, frequency, canonicalForm, numberOfMembers, organizationType);
        this.theme = others();
    }

    public String others() {
        return "others";
    }

    public String getTheme() {
        return theme;
    }

    @Override
    public String toString() {
        return super.toString() + " " + theme;
    }
    
}
