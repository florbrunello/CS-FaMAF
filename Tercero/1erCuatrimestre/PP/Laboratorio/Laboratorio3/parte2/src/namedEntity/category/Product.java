package namedEntity.category;

import namedEntity.NamedEntity;

public class Product extends NamedEntity {
    private String commercial;
    private String producer;

    public Product(String name, String category, int frequency, String commercial, String producer) {
        super(name, category, frequency);
        this.commercial = commercial;
        this.producer = producer;
    }

    public String getProductCommercial() {
        return commercial;
    }

    public void setProductCommercial(String commercial) {
        this.commercial = commercial;
    }

    public String getProductProducer() {
        return producer;
    }

    public void setProductProducer(String producer) {
        this.producer = producer;
    }
}
