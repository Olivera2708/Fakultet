package zadatak2;

public class StudentOcena {
	String indeks;
	String ime;
	String prezime;
	String predmet;
	int ocena;
	
	public StudentOcena(String indeks, String ime, String prezime, String predmet, int ocena) {
		this.indeks = indeks;
		this.ime = ime;
		this.prezime = prezime;
		this.predmet = predmet;
		this.ocena = ocena;
	}

	public String getIndeks() {
		return indeks;
	}

	public void setIndeks(String indeks) {
		this.indeks = indeks;
	}

	public String getIme() {
		return ime;
	}

	public void setIme(String ime) {
		this.ime = ime;
	}

	public String getPrezime() {
		return prezime;
	}

	public void setPrezime(String prezime) {
		this.prezime = prezime;
	}

	public String getPredmet() {
		return predmet;
	}

	public void setPredmet(String predmet) {
		this.predmet = predmet;
	}

	public int getOcena() {
		return ocena;
	}

	public void setOcena(int ocena) {
		this.ocena = ocena;
	}
}
