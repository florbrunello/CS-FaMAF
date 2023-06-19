package httpRequest;
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;


/* Esta clase se encarga de realizar efectivamente el pedido de feed al servidor de noticias
 * Leer sobre como hacer una http request en java
 * https://www.baeldung.com/java-http-request
 
 ATENCIÓN: NO MANEJA PARÁMETROS DE REQUEST 
 * */

public class httpRequester {
	
	public String getFeedRss(String urlFeed){
		String feedRssXml = null;
		try {
			//Creo una objeto conexión
			URL url = new URL(urlFeed);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");

			//Leo el contenido de la respuesta y lo guardo en buffer 
			int status = conn.getResponseCode();
			if (status != 200) {
				System.out.println("Error al obtener el feed" + status);
				return null;
			}
			BufferedReader buf = new BufferedReader(
				new InputStreamReader(conn.getInputStream()));
			String inputLine;
			StringBuffer content = new StringBuffer();
			while ((inputLine = buf.readLine()) != null) {
				content.append(inputLine);
			}
			buf.close();
			conn.disconnect();
			feedRssXml = content.toString();

			return feedRssXml;

		} catch (Exception e) {
			System.out.println("Error al crear el objeto conexión");
			return null;
		}

	}

	public String getFeedReedit(String urlFeed) {
		String feedReeditJson = null;
		return feedReeditJson;
	}

}
