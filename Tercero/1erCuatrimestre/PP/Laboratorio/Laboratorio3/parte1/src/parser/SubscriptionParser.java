package parser;

import org.json.JSONObject;
import org.json.JSONArray;

import subscription.SingleSubscription;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/*
 * Esta clase implementa el parser del  archivo de suscripcion (json)
 * Leer https://www.w3docs.com/snippets/java/how-to-parse-json-in-java.html
 * */

public class SubscriptionParser {

    public JSONObject parseJsonFile (String path) {
        
        // Creamos un string con el archivo
        String jsonString = null;
        try {
            Path filePath = Paths.get(path);
            jsonString = new String(Files.readAllBytes(filePath));
        } catch (Exception e) {
            System.out.println("Error al leer el archivo");
            return null;
        }
        
        JSONArray subscriptions = new JSONArray(jsonString);
        
        JSONArray rssUrls = new JSONArray();
        JSONArray redditUrls = new JSONArray();
        
        for (int i = 0; i < subscriptions.length(); i++) {

            JSONObject obj = subscriptions.getJSONObject(i);
            String urlType = obj.getString("urlType");
            SingleSubscription singlesubs = new SingleSubscription(null, null, urlType);
            
            if (urlType.equals("rss")) {
                String url = obj.getString("url");
                JSONArray urlParams = obj.getJSONArray("urlParams");
                
                singlesubs.setUrl(url);
                for(int j = 0; j < urlParams.length(); j++) {
                    singlesubs.setUlrParams(urlParams.getString(j));
                }

                for (int j = 0; j < singlesubs.getUlrParamsSize(); j++) {
                    String res = singlesubs.getFeedToRequest(j);
                    rssUrls.put(res);
                }
            } else if (urlType.equals("reddit")) {
                String url = obj.getString("url");
                JSONArray urlParams = obj.getJSONArray("urlParams");
                
                singlesubs.setUrl(url);
                for(int j = 0; j < urlParams.length(); j++) {
                    singlesubs.setUlrParams(urlParams.getString(j));
                }

                for (int j = 0; j < singlesubs.getUlrParamsSize(); j++) {
                    String res = singlesubs.getFeedToRequest(j);
                    redditUrls.put(res);
                }
            }
        }
        
        // Creamos un objeto JSON con campos rss y reddit
        JSONObject json = new JSONObject();
        json.put("rss", rssUrls);
        json.put("reddit", redditUrls);

        System.out.println(json.toString());
        return json;
    }
}
