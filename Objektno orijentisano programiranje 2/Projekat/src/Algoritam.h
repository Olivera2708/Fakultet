//Algoritam koji prolazi kroz sve mogucnosti i trazi tacno resenje za zadate brojeve
//5.1.2022.
//Olivera Radovanovic

#include "Calc.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;
#pragma once

class Algoritam{
	Calc<int> calculator;
	int trazeni;
	int brojevi[6];
	int najboljiRez;
	string izraz;

	bool zagrade(int po, int ko, int kz, vector<string> res);
	bool proveri(vector<string> vek);
	string uString(vector<string> vek);
	vector<string> postaviZagrade(vector<string> vek, int zp1, int zk1);
	bool kombinacije_bez(vector<string> &temp, int p, int k, vector<string> &brojevi, vector<string> &operacije);
	bool kombinacije_sa(vector<string> &temp, int p, int k, vector<string> &brojevi, vector<string> &operacije);
	bool napraviIzraz(vector<string> &brojevi_vec, vector<string> &operacije);
public:
	~Algoritam();
	Algoritam();
	Algoritam(int t, int *br);
	string pronadji();
};
