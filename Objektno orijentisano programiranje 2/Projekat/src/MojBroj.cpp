//Klasa igre moj broj, koja sadzi sve kljucne funkcije da bi igra funkcionisala
//5.1.2022.
//Olivera Radovanovic

#include "MojBroj.h"

//konstruktori
MojBroj::MojBroj(){
	pobednik = 0;
	fupis.open("res/Rezultat.txt");
	r1 = 0;
	r2 = 0;
	trazeni = 0;
	poeni1 = 0;
	poeni2 = 0;
}

//destruktor
MojBroj::~MojBroj(){}

//rad sa fajlom za citanje, ulazna vrednost ime fajla
void MojBroj::otvoriFajl(string ime){
	fotvoren.open("res/" + ime);
	if (fotvoren.fail()){
		cout << "Izabrani fajl ne postoji" << endl;
	}
}

//ucitava brojeve za sledecu rundu iz fajla
bool MojBroj::ucitajSledeci(){
	if (fotvoren.peek() == EOF)
		return false;

	int pom1, pom2, pom3, pom4;

	fotvoren >> trazeni;
	fotvoren >> pom1 >> pom2;
	brojevi[4] = pom1;
	brojevi[5] = pom2;
	fotvoren >> pom1 >> pom2 >> pom3 >> pom4;
	brojevi[0] = pom1;
	brojevi[1] = pom2;
	brojevi[2] = pom3;
	brojevi[3] = pom4;

	return true;
}

//prikaz brojeva na konzoli, kao i broja runde
void MojBroj::prikaz(int runda){
	cout << "------------------------Runda " << runda << "------------------------" << endl;
	cout << "|-----------------------------------------------------|" << endl;
	cout << "| Poeni: " << poeni1 <<"                                   Poeni: "<< poeni2 << " |" << endl;
	cout << "-------------------------------------------------------" << endl;
	cout << "|                         " << trazeni <<"                         |" << endl;
	cout << "|                 -------------------                 |" << endl;
	cout << "|                                                     |" << endl;
	cout << "|       " << brojevi[0] << "   " << brojevi[1] << "   " << brojevi[2] << "   " << brojevi[3] << "   " << "         " << brojevi[4] << "          " << brojevi[5] << "       |" << endl;
	cout << "|                                                     |" << endl;
	cout << "-------------------------------------------------------" << endl;
}

//prikaz krajnjeg rezultata na konzoli
void MojBroj::kraj(){
	cout << "--------------------------Kraj-------------------------" << endl;
	cout << "| Poeni: " << poeni1 <<"                                   Poeni: "<< poeni2 << " |" << endl;
	cout << "-------------------------------------------------------" << endl;
}

//okrisnici unose svoja resenja prima int koji oznacava koji igrac igra prvi
void MojBroj::unosResenja(int naRedu){
	Calc<int> calculator(brojevi);
	resenje1 = "";
	resenje2 = "";
	r1 = 0;
	r2 = 0;

	//trazimo od igraca da unese resenje
	if (naRedu == 1){
		while (true){
			cout << "Resenje od prvog igraca -> ";
			cin >> resenje1;

			//provera da li se resenje moze izracunati
			r1 = calculator.calculate(resenje1 + "=");
			if(r1 == -1)
				cout << "Uneseni izraz nije ispravan!" << endl;
			else break;
		}
		resenje1 += "=" + to_string(r1);

		//ako je tacno kraj runde
		if (r1 == trazeni){
			pobednik = 1;
			poeni1 += 1;
		}
		else{
			while (true){
				//provera jel tacno, ako nije onda
				cout << "Resenje od drugog igraca -> ";
				cin >> resenje2;
				r2 = calculator.calculate(resenje2 + "=");
				if(r2 == -1)
					cout << "Uneseni izraz nije ispravan!" << endl;
				else break;
			}
			//provara ko je blizi
			resenje2 += "=" + to_string(r2);
			if (trazeni - r1 < trazeni - r2){
				poeni1 += 1;
				pobednik = 1;
			}
			else if (trazeni - r1 > trazeni - r2){
				poeni2 += 1;
				pobednik = 2;
			}
			else{
				pobednik = 1;
				poeni1 += 1;
			}
		}
	}
	else{
		while (true){
			cout << "Resenje od drugog igraca -> ";
			cin >> resenje2;

			//provera da li se resenje moze izracunati
			r2 = calculator.calculate(resenje2 + "=");
			if(r2 == -1)
				cout << "Uneseni izraz nije ispravan!" << endl;
			else break;
		}
		resenje2 += "=" + to_string(r2);

		//ako je tacno kraj runde
		if (r2 == trazeni){
			pobednik = 2;
			poeni2 += 1;
		}
		else{
			while (true){
				//provera jel tacno, ako nije onda
				cout << "Resenje od prvog igraca -> ";
				cin >> resenje1;
				r1 = calculator.calculate(resenje1 + "=");
				if(r1 == -1)
					cout << "Uneseni izraz nije ispravan!" << endl;
				else break;
			}
			//provara ko je blizi
			resenje1 += "=" + to_string(r1);
			if (trazeni - r1 < trazeni - r2){
				pobednik = 1;
				poeni1 += 1;
			}
			else if (trazeni - r1 > trazeni - r2){
				pobednik = 2;
				poeni2 += 1;
			}
			else{
				pobednik = 2;
				poeni2 += 1;
			}
		}
	}
}

//upisuje rezultat u datoteku Rezultat.txt
void MojBroj::upisiRezultat(int runda){
	fupis << "------------------------Runda " << runda << "------------------------" << endl;
	fupis << "|                                                     |" << endl;
	fupis << "|                         " << trazeni <<"                         |" << endl;
	fupis << "|                 -------------------                 |" << endl;
	fupis << "|                                                     |" << endl;
	fupis << "|       " << brojevi[0] << "   " << brojevi[1] << "   " << brojevi[2] << "   " << brojevi[3] << "   " << "         " << brojevi[4] << "          " << brojevi[5] << "       |" << endl;
	fupis << "|                                                     |" << endl;
	fupis << "-------------------------Igrac 1----------------------|" << endl;
	fupis << "|           " << resenje1 << "            | Odstupanje " << trazeni - r1 << " |" <<endl;
	fupis << "-------------------------Igrac 2----------------------|" << endl;
	fupis << "|           " << resenje2 << "            | Odstupanje " << trazeni - r2 << " |" <<endl;
	fupis << "--------------------Najbolje resenje------------------|" << endl;
	fupis << "|                                                     |" << endl;
	fupis << "|                 " << najboljeResenje << "                 |" <<endl;
	fupis << "|                                                     |" << endl;
	fupis << "-----------------------Pobednik------------------------" << endl;
	fupis << "|                                                     |" << endl;
	fupis << "|                       Igrac " << pobednik <<"                       |" << endl;
	fupis << "|                 -------------------                 |" << endl;
	fupis << "-------------------------------------------------------" << endl << endl;
}

//upisuje informacije na kraju igre u datoteku
void MojBroj::upisiKraj(){
	string p;
	if (poeni1 > poeni2)
		p = "Igrac 1";
	else if (poeni1 < poeni2)
		p = "Igrac 2";
	else
		p = "Nereseno";

	fupis << endl;
	fupis << "--------------------------Kraj-------------------------" << endl;
	fupis << "| Poeni igraca 1: " << poeni1 <<"                 Poeni igraca 2: "<< poeni2 << " |" << endl;
	fupis << "-------------------------------------------------------" << endl;
	fupis << "-----------------------Pobednik------------------------" << endl;
	fupis << "|                                                     |" << endl;
	fupis << "|                       " << p <<"                       |" << endl;
	fupis << "|                 -------------------                 |" << endl;
	fupis << "-------------------------------------------------------" << endl << endl;
}

//funkcija koja spaja sve ostale
void MojBroj::pokreniIgru(){
	int runda = 1;
	bool nijeKraj = true;

	if (trazeni != 0){
		cout << "Igra je zavrsena!" << endl;
		return ;
	}

	Algoritam algoritam;

	while (true){
		//ucitamo liniju iz fajla u objekat
		nijeKraj = ucitajSledeci();
		if (not nijeKraj)
			break;

		int naRedu = (runda-1)%2;

		if (naRedu == 1)
			naRedu = 2;
		else
			naRedu = 1;

		//ispis svih brojeva
		prikaz(runda);

		//unos resenja
		unosResenja(naRedu);

		//ispis najboljeg resenja
		algoritam = Algoritam(trazeni, brojevi);
		najboljeResenje = algoritam.pronadji();
		cout << "Najbolje resenje je -> " << najboljeResenje << endl;

		//upis u rezultati.txt
		upisiRezultat(runda);

		cout << endl;
		runda ++;
	}
	//upisi kraj u fajl
	upisiKraj();

	//prikaz kraja na konzoli
	kraj();

	fotvoren.close();
	fupis.close();
}




