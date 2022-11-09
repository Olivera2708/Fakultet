package zadatak1;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonToken;

public class main {
	static ArrayList<Knjiga> knjige = new ArrayList<Knjiga>();
	
	public static void main(String[] args) throws JsonParseException, IOException {
		ParseJSON();
		writeJSON();
	}
	
	
	public static void ParseJSON() throws JsonParseException, IOException {
		JsonFactory jsonFactory = new JsonFactory();
		JsonParser jsonParser = jsonFactory.createParser(new File("resources/Bookstore.json"));
		
		jsonParser.nextToken();
		
		while (jsonParser.nextToken() != JsonToken.END_OBJECT) {
			String fieldName = jsonParser.getCurrentName();

			if ("Books".equals(fieldName)) { // field value contains an object
				Knjiga knjiga = new Knjiga();
				// parse this object in the same way the whole JSON is parsed
				while (jsonParser.nextToken() != JsonToken.END_OBJECT) {
					String nameField = jsonParser.getCurrentName();
					jsonParser.nextToken(); // move to value

					if ("ISBN".equals(nameField)) {
						knjiga.setISBN(jsonParser.getText());
					}
					else if ("Price".equals(nameField)) {
						knjiga.setCena(jsonParser.getText());
						System.out.print(jsonParser.getText());
					}
					else if ("Edition".equals(nameField)) {
						knjiga.setEdicija(jsonParser.getText());
					}
					else if ("Title".equals(nameField)) {
						knjiga.setNaslov(jsonParser.getText());
					}
					else if ("Authors".equals(nameField)) {
						ArrayList<Autor> autori = new ArrayList<Autor>();
						//ovde mora vise njih da se ucita u listu
						while (jsonParser.nextToken() != JsonToken.END_OBJECT) {
							String filed = jsonParser.getCurrentName();
							jsonParser.nextToken();
							Autor autor = new Autor();
							
							if ("First_Name".equals(nameField)) {
								autor.setIme(jsonParser.getText());
							}
							else if ("Last_Name".equals(nameField)) {
								autor.setPrezime(jsonParser.getText());
							}
						}
						knjiga.setAutori(autori);
					}
					else if ("Tags".equals(nameField)) {
						//procitaj i ubaci u listu stringova
						ArrayList<String> tagovi = new ArrayList<String>();
						
						while (jsonParser.nextToken() != JsonToken.END_OBJECT) {
							String field = jsonParser.getCurrentName();
							tagovi.add(field);
						}
						knjiga.setTagovi(tagovi);
					}
				}
			}
		}
	}
	
	public static void writeJSON() {
		for (Knjiga k : knjige) {
			System.out.print(k);
		}
	}
}
