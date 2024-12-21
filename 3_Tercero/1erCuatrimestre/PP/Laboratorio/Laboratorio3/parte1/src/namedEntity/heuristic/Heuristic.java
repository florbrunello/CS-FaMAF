package namedEntity.heuristic;

import java.util.HashMap;
import java.util.Map;

public abstract class Heuristic {

	private static Map<String, String> categoryMap = new HashMap<>();
	static {
			categoryMap.put("Microsoft", "Organization");
			categoryMap.put("Apple", "Organization");
			categoryMap.put("Google", "Organization");
			categoryMap.put("Musk", "Person");
			categoryMap.put("Biden", "Person");
			categoryMap.put("Trump", "Person");
			categoryMap.put("Messi", "Person");
			categoryMap.put("Federer", "Person");
			categoryMap.put("USA", "Place");
			categoryMap.put("Russia", "Place");
		};
	
	private static Map<String, String> themeMap = new HashMap<>();
	static {
			themeMap.put("Microsoft", "Others");
			themeMap.put("Apple", "Others");
			themeMap.put("Google", "Others");
			themeMap.put("Musk", "Others");
			themeMap.put("Biden", "Politics");
			themeMap.put("Trump", "Politics");
			themeMap.put("Messi", "Futbol");
			themeMap.put("Federer", "Tenis");
			themeMap.put("USA", "Others");
			themeMap.put("Russia", "Others");
			};

	public String getCategory(String entity){
		return categoryMap.get(entity);
	}
	
	public String getTheme(String entity){
		return themeMap.get(entity);
	}
	
	public abstract boolean isEntity(String word);
		
}
