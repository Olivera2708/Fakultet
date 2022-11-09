package zadatak1;

public class Tacka implements Comparable<Tacka> {
	int x;
	int y;
	int z;
	float rastojanje;
	
	public Tacka(int x, int y, int z) {
		this.x = x;
		this.y = y;
		this.z = z;
		rastojanje();
	}
	
	public void rastojanje() {
		this.rastojanje = (float) Math.sqrt(this.x*this.x + this.y*this.y + this.z*this.z);
	}
	
	public float getRastojanje() {
		return this.rastojanje;
	}
	
	public String[] niz() {
		String[] niz = {String.valueOf(x), String.valueOf(y), String.valueOf(z), String.valueOf(rastojanje)};
		return niz;
	}

	public int getX() {
		return x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		this.y = y;
	}

	public int getZ() {
		return z;
	}

	public void setZ(int z) {
		this.z = z;
	}
	
	@Override
	public int compareTo(Tacka t) {
		if (this.rastojanje < t.getRastojanje()) return 1;
		if (this.rastojanje > t.getRastojanje()) return -1;
		return 0;
	}
}
