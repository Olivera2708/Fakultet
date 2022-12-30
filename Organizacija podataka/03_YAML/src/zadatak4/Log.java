package zadatak4;

import java.util.Date;
import java.util.List;

public class Log {
	Date datum;
	String korisnik;
	String greska;
	String opis;
	List<Object> stak;
	
	public Log(Date datum, String korisnik, String greska, String opis, List<Object> stak) {
		this.datum = datum;
		this.korisnik = korisnik;
		this.greska = greska;
		this.opis = opis;
		this.stak = stak;
	}
	
	public Log(Date datum, String korisnik, String greska, String opis) {
		this.datum = datum;
		this.korisnik = korisnik;
		this.greska = greska;
		this.opis = opis;
	}

	public Date getDatum() {
		return datum;
	}

	public void setDatum(Date datum) {
		this.datum = datum;
	}

	public String getKorisnik() {
		return korisnik;
	}

	public void setKorisnik(String korisnik) {
		this.korisnik = korisnik;
	}

	public String getGreska() {
		return greska;
	}

	public void setGreska(String greska) {
		this.greska = greska;
	}

	public String getOpis() {
		return opis;
	}

	public void setOpis(String opis) {
		this.opis = opis;
	}

	public List<Object> getStak() {
		return stak;
	}

	public void setStak(List<Object> stak) {
		this.stak = stak;
	}
}
