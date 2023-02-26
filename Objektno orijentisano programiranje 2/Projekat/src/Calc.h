//Klasa kalkulator, za prosledjeni string racuna njegovu vrednost
//5.1.2022.
//Olivera Radovanovic

#include "std_lib_facilities.h"
#pragma once

template <typename T>
struct Token {
	char kind;
	T value;
	Token(): kind(0), value(0) {};
	Token(char ch) :kind(ch), value(0) { }
	Token(char ch, T val) :kind(ch), value(val) { }
};

template <typename T>
struct Buffer{
	Token<T> buffer;
	bool full;
	Buffer() : buffer(0), full(0) { }
};

template <typename T>
class Calc{
	vector<char> ulazni;
	Token<T> t;
	Buffer<T> b;
	int brojevi[6];
	int nekorisceni[6];

	Token<T> ucitaj(char ch);

	T expression();
	T primary();
	T term();
	T calc(string ulaz);
public:
	void resetBrojevi();
	~Calc();
	Calc() {};
	Calc(int * br);
	T calculate(string ulaz);
};
