package zadatak1;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;


public class zad1 {
	
	public static void main(String args[]) throws FileNotFoundException, IOException {
		Yaml yaml = new Yaml(new Constructor(Invoice.class));

		Invoice invoice = null;
		try (InputStream input = new FileInputStream(new File("resources/invoice.yaml"));) {
			invoice = (Invoice) yaml.load(input);
			
			System.out.print("Unesite ulicu -> ");
			Scanner in = new Scanner(System.in);
			String novaUlica = in.nextLine();
			invoice.billTo.address.lines = novaUlica;
			
			System.out.print("Unesite grad -> ");
			String noviGrad = in.nextLine();
			invoice.billTo.address.city = noviGrad;
			
			System.out.print("Unesite drzavu -> ");
			String novaDrzava = in.nextLine();
			invoice.billTo.address.state = novaDrzava;
			
			System.out.print("Unesite postanski broj -> ");
			String novaPosta = in.nextLine();
			invoice.billTo.address.postal = novaPosta;
			
			in.close();
		}
		
		yaml = new Yaml();

		String output = yaml.dump(invoice);
		try (BufferedWriter fout = new BufferedWriter(new FileWriter("resources/invoice_mod.yaml"));) {
			fout.write(output);
		}
	}
}
