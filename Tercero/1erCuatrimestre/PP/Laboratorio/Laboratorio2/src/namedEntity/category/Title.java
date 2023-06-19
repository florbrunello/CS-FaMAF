package namedEntity.category;

public class Title extends Person {
    private String canonicalForm; 
    private String professional;

    public Title(String name, String category, int frequency, String id, String canonicalForm, String professional) {
        super(name, category, frequency, id);
        this.canonicalForm = canonicalForm;
        this.professional = professional;
    }

    public String getTitleCanonicalForm() {
        return canonicalForm;
    }

    public String getTitleProfessional() {
        return professional;
    }

    public void setTitleCanonicalForm(String canonicalForm) {
        this.canonicalForm = canonicalForm;
    }

    public void setTitleProfessional(String professional) {
        this.professional = professional;
    }
}