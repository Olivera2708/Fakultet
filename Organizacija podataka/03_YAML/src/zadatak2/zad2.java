package zadatak2;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

public class zad2 {
	static Invoice invoice;
	static Map<String, Object> kurs;
	static String izabrana;

	public static void main(String[] args) {
		ucitajInvoice();
		izaberiValutu();
		upisiYaml();
	}
	
	public static void upisiYaml() {
		Yaml yaml = new Yaml(new Constructor(Invoice.class));
		
		invoice.tax *= (Integer) kurs.get(izabrana);
		invoice.total *= (Integer) kurs.get(izabrana);
		
		for (Product p : invoice.product) {
			p.price *= (Integer) kurs.get(izabrana);
		}
		
		try {
			yaml.dump(invoice, new FileWriter("resources/invoice_" + izabrana + ".yaml"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void izaberiValutu() {
		Yaml yaml = new Yaml();
		
		try(InputStream input = new FileInputStream(new File("resources/exchange.yaml"))){
			for (Object object : yaml.loadAll(input)) {
				kurs = (Map<String, Object>) object;
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.print("Izaberi valutu: ");
		for (String kljuc : kurs.keySet()) {
			System.out.print(kljuc + " ");
		}
		System.out.println();
		System.out.print("Naziv valute -> ");
		Scanner s = new Scanner(System.in);
		izabrana = s.next();
	}
	
	public static void ucitajInvoice() {
		Yaml yaml = new Yaml(new Constructor(Invoice.class));
		
		try(InputStream input = new FileInputStream(new File("resources/invoice.yaml"))){
			
			for (Object object : yaml.loadAll(input)) {
				invoice = (Invoice) object;
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
