package zadatak1;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

import com.opencsv.CSVWriter;
import com.opencsv.CSVWriterBuilder;
import com.opencsv.ICSVWriter;

public class zad1{
	static ArrayList<Tacka> tacke = new ArrayList<Tacka>();
	
	public static void main(String[] args) {
		ucitajTacke();
		ispisiCSVsortirano();
	}
	
	public static void ucitajTacke() {
		try (BufferedReader bf = new BufferedReader(new FileReader("resources/koordinate.csv"))){
			String line = "";
			
			while ((line = bf.readLine()) != null) {
				String[] tokens = line.split(",");
				Tacka tacka = new Tacka(Integer.parseInt(tokens[0]), Integer.parseInt(tokens[1]), Integer.parseInt(tokens[2]));
				tacke.add(tacka);
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void ispisiCSV() {
		try(CSVWriter csvWriter = (CSVWriter) new CSVWriterBuilder(new FileWriter("resources/rastojanje.csv"))
			    .withSeparator('#')
			    .withQuoteChar(ICSVWriter.NO_QUOTE_CHARACTER)
			    .build()) {
			
			for (Tacka t: tacke){
				csvWriter.writeNext(t.niz());
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void ispisiCSVsortirano() {
		try(CSVWriter csvWriter = (CSVWriter) new CSVWriterBuilder(new FileWriter("resources/rastojanje.csv"))
			    .withSeparator('#')
			    .withQuoteChar(ICSVWriter.NO_QUOTE_CHARACTER)
			    .build()) {
			Collections.sort(tacke, Collections.reverseOrder());
			
			for (Tacka t: tacke){
				csvWriter.writeNext(t.niz());
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}