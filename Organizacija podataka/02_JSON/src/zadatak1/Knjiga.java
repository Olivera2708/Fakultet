package zadatak1;

import java.util.ArrayList;

public class Knjiga {
	String ISBN;
	String cena;
	String edicija;
	String naslov;
	ArrayList<Autor> autori = new ArrayList<Autor>();
	ArrayList<String> tagovi = new ArrayList<String>();
	
	public String getISBN() {
		return ISBN;
	}
	public void setISBN(String iSBN) {
		ISBN = iSBN;
	}
	public String getCena() {
		return cena;
	}
	public void setCena(String cena) {
		this.cena = cena;
	}
	public String getEdicija() {
		return edicija;
	}
	public void setEdicija(String edicija) {
		this.edicija = edicija;
	}
	public String getNaslov() {
		return naslov;
	}
	public void setNaslov(String naslov) {
		this.naslov = naslov;
	}
	public ArrayList<Autor> getAutori() {
		return autori;
	}
	public void setAutori(ArrayList<Autor> autori) {
		this.autori = autori;
	}
	public ArrayList<String> getTagovi() {
		return tagovi;
	}
	public void setTagovi(ArrayList<String> tagovi) {
		this.tagovi = tagovi;
	}
	
	@Override
	public String toString() {
		return "ISBN " + this.ISBN + "\nCena " + this.cena + "\nEdicija " + this.edicija; 
	}
	
	
}
