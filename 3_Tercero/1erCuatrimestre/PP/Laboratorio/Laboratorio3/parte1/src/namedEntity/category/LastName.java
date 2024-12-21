package namedEntity.category;

public class LastName extends Person {
    private String canonicalForm; 
    private String origin;

    public LastName(String name, String category, int frequency, String id, String canonicalForm, String origin) {
        super(name, category, frequency, id);
        this.canonicalForm = canonicalForm;
        this.origin = origin;
    }

    public String getLastNameCanonicalForm() {
        return canonicalForm;
    }

    public String getLastNameOrigin() {
        return origin;
    }
}