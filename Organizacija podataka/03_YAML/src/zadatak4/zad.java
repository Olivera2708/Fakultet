package zadatak4;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Date;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

public class zad {
	static List<Map<String, Object>> mapa = new ArrayList<Map<String, Object>>();
	static List<Log> logoviGreska = new ArrayList<Log>();
	static List<Log> logoviUpozorenje = new ArrayList<Log>();

	public static void main(String[] args) {
		ucitajYAML();
		prebaciLog();
		razvrstajYAML();
	}
	
	public static void prebaciLog() {
		for (Map<String, Object> map : mapa) {
			if(map.containsKey("Warning")) {
				Log mojLog = new Log((Date) map.get("Time"),(String) map.get("User"), "Warning", (String) map.get("Warning"));
				logoviUpozorenje.add(mojLog);
			}
			else {
				Log mojLog = new Log((Date) map.get("Date"),(String) map.get("User"), "Fatal", (String) map.get("Fatal"), (List<Object>) map.get("Stack"));
				logoviGreska.add(mojLog);
			}
		}
		
	}
	
	public static void razvrstajYAML() {
		Yaml yaml = new Yaml(new Constructor(Log.class));
		
		try {
			FileWriter warning = new FileWriter("resources/log_warn.yaml");
			FileWriter error = new FileWriter("resources/log_error.yaml");
	
			yaml.dump(logoviUpozorenje, warning);
			yaml.dump(logoviGreska, error);
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	public static void ucitajYAML() {
		Yaml yaml = new Yaml();
		
		try(InputStream input = new FileInputStream(new File("resources/log.yaml"))){
			
			for (Object o : yaml.loadAll(input)) {
				mapa.add((Map<String, Object>) o);
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
