package namedEntity.heuristic;

import java.util.Map;

public abstract class Heuristic {

	private static Map<String, String> categoryMap = Map.of(
			"Microsoft", "Organization", 
			"Apple", "Organization", 
			"Google", "Organization",
			"Musk", "Person",
			"Biden", "Person",
			"Trump", "Person",
			"Messi", "Person",
			"Federer", "Person",
			"USA", "Place",
			"Russia", "Place"
			);
	
	private static Map<String, String> themeMap = Map.of(
			"Microsoft", "Others", 
			"Apple", "Others", 
			"Google", "Others",
			"Musk", "Others",
			"Biden", "Politics",
			"Trump", "Politics",
			"Messi", "Futbol",
			"Federer", "Tenis",
			"USA", "Others",
			"Russia", "Others"
			);

	public String getCategory(String entity){
		return categoryMap.get(entity);
	}
	
	public String getTheme(String entity){
		return themeMap.get(entity);
	}
	
	public abstract boolean isEntity(String word);
		
}
