package zadatak2;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import com.opencsv.CSVWriter;
import com.opencsv.CSVWriterBuilder;
import com.opencsv.ICSVWriter;

public class zad2 {
	static ArrayList<StudentOcena> studentOcena = new ArrayList<StudentOcena>();
	
	public static void main(String[] args) {
		ucitajPodatke();
		ispisiCSVocena();
	}
	
	public static void ucitajPodatke() {
		try (BufferedReader bf = new BufferedReader(new FileReader("resources/ocene.csv"))){
			String line = "";
			
			bf.readLine();
			
			while ((line = bf.readLine()) != null) {
				String[] tokens = line.split(",");
				StudentOcena so = new StudentOcena(tokens[0], tokens[1], tokens[2], tokens[3], Integer.parseInt(tokens[4]));
				studentOcena.add(so);
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void ispisiCSVocena() {
		for (int i = 5; i <= 10; i ++) {
			try(CSVWriter csvWriter = (CSVWriter) new CSVWriterBuilder(new FileWriter("resources/ocena" + i + ".csv"))
				    .withSeparator(',')
				    .withQuoteChar(ICSVWriter.NO_QUOTE_CHARACTER)
				    .build()) {
				
				ArrayList<String> indeksi = new ArrayList<String>();
				ArrayList<Student> student = new ArrayList<Student>();
				
				for (StudentOcena so: studentOcena){
					if (so.getOcena() == i) {
						if (indeksi.contains(so.getIndeks())) {
							for (Student s: student) {
								if (s.getIndeks().equals(so.getIndeks())) {
									s.setBrojOcene(s.getBrojOcene() + 1);
								}
							}
						}
						else {
							indeksi.add(so.getIndeks());
							Student s = new Student(so.getIndeks(), so.getIme(), so.getPrezime(), 1);
							student.add(s);
						}
					}
				}
				
				for (Student s: student) {
					csvWriter.writeNext(s.write());
				}
				
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
