package namedEntity.category;

import java.util.List;

public class Name extends Person {
    private String canonicalForm;
    private String origin;
    private List<String> alternativeForms;

    public Name(String name, String category, int frequency, String id, String canonicalForm, String origin, List<String> alternativeForms) {
        super(name, category, frequency, id);
        this.canonicalForm = canonicalForm;
        this.origin = origin;
        this.alternativeForms = alternativeForms;
    }

    public String getNameCanonicalForm() {
        return canonicalForm;
    }

    public void setNameCanonicalForm(String canonicalForm) {
        this.canonicalForm = canonicalForm;
    }

    public String getNameOrigin() {
        return origin;
    }

    public void setNameOrigin(String origin) {
        this.origin = origin;
    }

    public List<String> getNameAlternativeForms() {
        return alternativeForms;
    }

    public void setNameAlternativeForms(List<String> alternativeForms) {
        this.alternativeForms = alternativeForms;
    }

    public void addNameAlternativeForm(String alternativeForm) {
        this.alternativeForms.add(alternativeForm);
    }
}
