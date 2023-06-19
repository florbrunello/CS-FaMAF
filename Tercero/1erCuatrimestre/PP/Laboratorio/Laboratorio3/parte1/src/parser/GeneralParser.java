package parser;

import feed.Feed;

/*Esta clase modela los ATRIBUTOS Y METODOS COMUNES a todos los distintos tipos de parser existentes en la aplicacion*/
public abstract class GeneralParser {
    public abstract Feed parse (String str); 
}
