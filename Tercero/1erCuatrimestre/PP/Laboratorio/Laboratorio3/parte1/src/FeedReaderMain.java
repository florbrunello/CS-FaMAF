import org.json.JSONObject;
import org.json.JSONArray;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import feed.Feed;
import parser.*;
import httpRequest.httpRequester;
import namedEntity.Application;
import namedEntity.NamedEntity;
import namedEntity.heuristic.QuickHeuristic;

public class FeedReaderMain {

	private static void printHelp(){
		System.out.println("Please, call this program in correct way: FeedReader [-ne]");
	}
	
	public static void main(String[] args) throws IOException {
		System.out.println("************* FeedReader version 1.0 *************");

		if (args.length == 0) {		
			//Leemos el archivo de suscription por defecto
			// Creamos un string con el archivo
			Path filepath = Paths.get("config/subscriptions.json");
			System.out.println("Reading file: " + filepath);
			SubscriptionParser parser = new SubscriptionParser();
			JSONObject json = parser.parseJsonFile(filepath.toString());			
			
			//Llamamos al httpRequester para obtener el feed del servidor
			JSONArray rssArray = json.getJSONArray("rss");
			for (int i = 0; i < rssArray.length(); i++) {
				String Url = rssArray.getString(i);
				System.out.println("\n\n\n\nReading feed from: " + Url);
				httpRequester requester = new httpRequester();
				String f = requester.getFeedRss(Url);			
		
				//Llamamos al Parser especifico para extrar los datos necesarios por la aplicacion 
				RssParser parserRss = new RssParser();
				
				//Llamamos al constructor de Feed
				Feed feed = parserRss.parse(f);			
				
				//Llamamos al prettyPrint del Feed para ver los articulos del feed en forma legible y amigable para el usuario
				feed.prettyPrint();
			}
		} 
		else if (args.length == 1 && args[0].equals("-ne")){
			//Leemos el archivo de suscription por defecto
			// Creamos un string con el archivo
			Path filepath = Paths.get("config/subscriptions.json");
			System.out.println("Reading file: " + filepath);
			SubscriptionParser parser = new SubscriptionParser();
			JSONObject json = parser.parseJsonFile(filepath.toString());	
			
			JSONArray rssArray = json.getJSONArray("rss");
			for (int i = 0; i < rssArray.length(); i++) {	
				String Url = rssArray.getString(i);		
				System.out.println("\n\n\n\nReading named entities in: " + Url);
				httpRequester requester = new httpRequester();
				String f = requester.getFeedRss(Url);			
				RssParser parserRss = new RssParser();
				Feed feed = parserRss.parse(f);	

				//Llamamos a la heuristica para que compute las entidades nombradas de cada articulos del feed
				QuickHeuristic quickHeuristic = new QuickHeuristic();
				// randomHeuristic
				//RandomHeuristic randomHeuristic = new RandomHeuristic();
				
				Application application = new Application();
				List<NamedEntity> namedEntities = new ArrayList<>();	
				namedEntities = application.main(feed, quickHeuristic);
				
				//Llamamos al prettyPrint de la tabla de entidades nombradas del feed.
				namedEntities.forEach(entity -> entity.prettyPrint());
			}
		} else {
			printHelp();
		}
	}

}
