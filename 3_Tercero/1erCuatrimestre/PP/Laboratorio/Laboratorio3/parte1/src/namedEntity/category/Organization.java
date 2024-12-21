package namedEntity.category;

import namedEntity.NamedEntity;

public class Organization extends NamedEntity {
    private String canonicalForm;
    private int numberOfMembers;
    private String organizationType;

    public Organization(String name, String category, int frequency, String canonicalForm, int numberOfMembers, String organizationType) {
        super(name, category, frequency);
        this.canonicalForm = canonicalForm;
        this.numberOfMembers = numberOfMembers;
        this.organizationType = organizationType;
    }

    public String getOrganizationCanonicalForm() {
        return canonicalForm;
    }

    public void setOrganizationCanonicalForm(String canonicalForm) {
        this.canonicalForm = canonicalForm;
    }

    public int getOrganizationNumberOfMembers() {
        return numberOfMembers;
    }

    public void setOrganizationNumberOfMembers(int numberOfMembers) {
        this.numberOfMembers = numberOfMembers;
    }

    public String getOrganizationType() {
        return organizationType;
    }

    public void setOrganizationType(String type) {
        this.organizationType = type;
    }
}

