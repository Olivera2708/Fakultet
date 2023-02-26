//Algoritam koji prolazi kroz sve mogucnosti i trazi tacno resenje za zadate brojeve
//5.1.2022.
//Olivera Radovanovic

#include "Algoritam.h"
#include "Calc.cpp"

Algoritam::~Algoritam(){
}

Algoritam::Algoritam(int t, int *br){
	calculator = Calc<int>(br);
	trazeni = t;
	for (int i = 0; i < 6; i++){
		brojevi[i] = br[i];
	}
	najboljiRez = 0;
}

Algoritam::Algoritam(){
	trazeni = 0;
	najboljiRez = 0;
}

//postavlja zagrade na zadata mesta u vektoru
//prosledimo mesta gde zelimo da se stave zagrade i vektor u koji da stavi
//vraca vektor sa zagradama na zadatim mestima
vector<string> Algoritam::postaviZagrade(vector<string> vek, int zp1 = -1, int zk1 = -1){
	vector<string>::iterator it;

	if (zp1 != -1) {
		vek.insert(vek.begin() + zp1, "(");
		vek.insert(vek.begin() + zk1, ")");
	}

	return vek;
}

//pretvara vektor u string
//prosledjujemo vektor i dobijamo string
string Algoritam::uString(vector<string> vek){
	string s;
	vector<string>::iterator it;

	for (it = vek.begin(); it != vek.end(); it++){
		s += *it;
	}

	s += "=";
	return s;
}

//izracunava vrednost izraza na osnovu vektora koji je prosledjen
//vraca bool, true ako je resenje tacno, false ako nije
bool Algoritam::proveri(vector<string> vek){
	string s = uString(vek);
	int broj = calculator.calculate(s);
	s += to_string(int(broj));

//	cout << s << endl;

	//provera jel tacan
	if (abs(trazeni - broj) == 0){
		najboljiRez = broj;
		izraz = s;
		return true;
	}
	if (abs(trazeni - broj) < abs(trazeni - najboljiRez)){
		najboljiRez = broj;
		izraz = s;
	}
	return false;
}

//odredjuje mesta za zagrade koja su u opticaju kao i vektor
//vraca bool, true ako je nasao mesto koje daje tacan rezultat, inace false
bool Algoritam::zagrade(int po, int ko, int kz, vector<string> res){
	for (int za = po; za < ko; za+=2){
		for (int zk = za + 4; zk < kz; zk+=2){
			if (zk > res.size()+1)
				return false;

			vector<string> vek = postaviZagrade(res, za, zk);

			if (za == po and zk >= kz-1)
				continue;

			if (proveri(vek))
				return true;

			//postavljanje zagrada unutar ovih
			if (zk-za > 4){
				if (zagrade(za+1, zk-2, zk+2, vek))
					return true;
			}

			if (zagrade(zk+2, ko+2, kz+3, vek))
				return true;

		}
	}
	return false;
}

//prolazi kroz sve mogucnosti za brojeve
bool Algoritam::kombinacije_bez(vector<string> &temp, int p, int k, vector<string> &brojevi_vec, vector<string> &operacije){
	bool t;
	if (k == 0){
		vector<string> temp1;
		do{
			t = kombinacije_sa(temp1, 0, temp.size()-1, temp, operacije);
			if (t)
				return true;
		} while (std::next_permutation(temp.begin(), temp.end()));
	}
	for (int i = p; i < brojevi_vec.size(); i++){
		temp.push_back(brojevi_vec.at(i));

		t = kombinacije_bez(temp, i+1, k-1, brojevi_vec, operacije);
		if (t)
			return true;

		temp.pop_back();
	}
	return false;
}

//prolazi kroz sve mogucnosti za operacije
bool Algoritam::kombinacije_sa(vector<string> &temp, int p, int k, vector<string> &brojevi_vec, vector<string> &operacije){
	bool t;
	if (k == 0){
		do{
			t = napraviIzraz(brojevi_vec, temp);
			if (t)
				return true;
		} while (std::next_permutation(temp.begin(), temp.end()));
	}
	else {
		for (int i = p; i < operacije.size(); i++){
			temp.push_back(operacije.at(i));
			t = kombinacije_sa(temp, i, k-1, brojevi_vec, operacije);
			if (t)
				return true;

			temp.pop_back();
		}
	}
	return false;
}

//spaja vektore brojeva i operacija i poziva funkcije za pretvaranje u string,
//racunanje izraza i dodavanje zagrada, vraca true ako je pronadjeno tacno resenje
bool Algoritam::napraviIzraz(vector<string> &brojevi_vec, vector<string> &oper){
	vector<string> res;

	for (int i = 0; i < brojevi_vec.size(); i++){
		res.push_back(brojevi_vec.at(i));
		if (i != brojevi_vec.size()-1)
			res.push_back(oper.at(i));
	}

	if (proveri(res))
		return true;

	if (res.size() > 3) {
		int d_br = brojevi_vec.size();
		for (int i = 0; i < brojevi_vec.size()-3; i++){
			d_br++;
		}

		if (zagrade(0, d_br, d_br+4, res))
			return true;
	}
	return false;
}

//funkcija koja prolazi kroz sve slucajeve i trazi tacno resenje
//povratna vrednost je izraz koji dovodi do resenja
string Algoritam::pronadji(){
	vector<string> operacije;
	operacije.push_back("*");
	operacije.push_back("+");
	operacije.push_back("-");
	operacije.push_back("/");

	vector<string> brojevi_vec;
	vector<string> temp;

	for (int i = 0; i < 6; i++){
		brojevi_vec.push_back(to_string(brojevi[i]));
	}
	sort(brojevi_vec.begin(), brojevi_vec.end());
	bool t;

	for (int i = 1; i < 7; i++){
		t = kombinacije_bez(temp, 0, i, brojevi_vec, operacije);
		if (t)
			return izraz;
	}

	return izraz;
}
