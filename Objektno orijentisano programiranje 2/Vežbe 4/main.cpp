#include <iostream>
#include <fstream>
#include <string>
#include "myComplex.h"
using namespace std;

void upisi(string resenje) {
	ofstream ofs("izlaz.txt", ios::app);
	ofs << resenje;
	ofs.close();
}

void izracunaj(string prvi, string oper, string treci) {
	Complex p, d;
	int znakIp, znakId;

	if ((znakIp = prvi.find("+")) != string::npos) {
		p = Complex(stoi(prvi.substr(0, znakIp)), stoi(prvi.substr(znakIp, prvi.length() - 1)));
	}
	else if ((znakIp = prvi.find("-")) != string::npos) {
		int num = stoi(prvi.substr(znakIp, prvi.length() - 1));
		p = Complex(stoi(prvi.substr(0, znakIp)),  -num);
	}
	else if ((znakIp = prvi.find("i")) != string::npos) {
		int num = stoi(prvi.substr(0, znakIp));
		p = Complex(0,  num);
	}
	else{
		p = Complex(stoi(prvi), 0);
	}


	if ((znakId = treci.find("+")) != string::npos) {
		d = Complex(stoi(treci.substr(0, znakId)), stoi(treci.substr(znakId, treci.length() - 1)));
	}
	else if ((znakId = treci.find("-")) != string::npos) {
		int num = stoi(treci.substr(znakId, treci.length() - 1));
		d = Complex(stoi(treci.substr(0, znakId)), num);
	}
	else if ((znakId = treci.find("i")) != string::npos) {
		int num = stoi(treci.substr(0, znakId));
		d = Complex(0,  num);
	}
	else{
		d = Complex(stoi(treci), 0);
	}

	string s;
	Complex a;

	if (oper.compare("ADD") == 0) {
		a = p + d;
	}
	else if (oper.compare("SUB") == 0) {
		a = p - d;
	}
	else if (oper.compare("MUL") == 0) {
		a = p * d;
	}

	if (a.getImag() > 0)
		s = "= " + to_string(int(a.getReal())) + "+" + to_string(int(a.getImag())) + "i\n";
	else
		s = "= " + to_string(int(a.getReal())) + to_string(int(a.getImag())) + "i\n";

	upisi(s);
}

void ucitaj() {
	ifstream ifs("ulaz.txt");
	string prvi, drugi, treci;
	string linija = "";

	while (ifs >> prvi >> drugi >> treci)
		izracunaj(prvi, drugi, treci);

	ifs.close();

}

int main(int argc, char** argv) {
	ucitaj();

	return 0;
}

