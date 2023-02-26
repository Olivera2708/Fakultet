#include "Algoritam.h"
#include "Calc.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;
#pragma once

class MojBroj{
    ifstream fotvoren;
    ofstream fupis;
	int trazeni;
	int brojevi[6];
	int pobednik;

	string najboljeResenje;
	string resenje1;
	string resenje2;

	int r1; //rezultat prvog
	int r2; //rezultat drugog

	int poeni1; //onaj igrac koji igra neparno prvi
	int poeni2; //onaj igrac koji igra parno prvi

	bool ucitajSledeci();

	//igra
	void prikaz(int runda);
	void kraj();
	void unosResenja(int naRedu);
	void upisiRezultat(int runda);
	void upisiKraj();

public:
	//konstruktori
	MojBroj();
	//desturktor
	~MojBroj();
	//funkcija za pokretanje igre
	void pokreniIgru();
	//rad sa fajlom iz kog se cita
	void otvoriFajl(string ime);
};
