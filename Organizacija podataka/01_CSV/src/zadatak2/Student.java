package zadatak2;

public class Student {
	String indeks;
	String ime;
	String prezime;
	int brojOcene;

	public Student(String indeks, String ime, String prezime, int brojOcene) {
		this.indeks = indeks;
		this.ime = ime;
		this.prezime = prezime;
		this.brojOcene = brojOcene;
	}
	
	public int getBrojOcene() {
		return brojOcene;
	}

	public void setBrojOcene(int brojOcene) {
		this.brojOcene = brojOcene;
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
	
	public String[] write() {
		String[] niz = {this.indeks, this.ime, this.prezime, String.valueOf(this.brojOcene)};
		return niz;
	}
}
