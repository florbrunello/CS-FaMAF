package parser;
import feed.*;
import java.io.*;
import org.w3c.dom.*;
import java.util.*;
import java.text.SimpleDateFormat;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.w3c.dom.Element;

/* Esta clase implementa el parser de feed de tipo rss (xml)
 * https://www.tutorialspoint.com/java_xml/java_dom_parse_document.htm 
 * */

public class RssParser extends GeneralParser{
   
    @Override
    public Feed parse(String feedString) {
        try{
            //Ver bien acá para linkearlo con el archivo que devuelve el servidor . Chequear que esto esté bien.
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse(new InputSource(new StringReader(feedString))); 
            document.getDocumentElement().normalize();

            NodeList nList = document.getElementsByTagName("item");

            Feed feed = new Feed("Feed");

            //Lista de articulos
            for (int temp = 0; temp < nList.getLength(); temp++) {
                Node nNode = nList.item(temp);
                Element eElement = (Element) nNode;
                String dateString = eElement.getElementsByTagName("pubDate").item(0).getTextContent();
                SimpleDateFormat dateFormat = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss zzz", Locale.ENGLISH); 
                Date date = dateFormat.parse(dateString);

                Article article = new Article(eElement.getElementsByTagName("title").item(0).getTextContent(),
                                              eElement.getElementsByTagName("description").item(0).getTextContent(),
                                              date,
                                              eElement.getElementsByTagName("link").item(0).getTextContent());
        
                feed.addArticle(article);
            }

            return feed;   
        } catch (Exception e){
            e.printStackTrace();
            System.out.println("Error en el parser");
            return null;
        }
    }

}