//Klasa kalkulator, za prosledjeni string racuna njegovu vrednost
//5.1.2022.
//Olivera Radovanovic

#include "Calc.h"

//destruktor
template <typename T>
Calc<T>::~Calc(){
}

//konstruktori
template <typename T>
Calc<T>::Calc(int * br){
	for (int i = 0; i < 6; i++){
		brojevi[i] = br[i];
		nekorisceni[i] = br[i];
	}
}

//za prosledjeni karakter pravi token i vraca ga
//moze doci do izuzetka ako karakter nije jedan od ocekivanih
//ili ako se nalazi broj koji se ne sme koristiti
template <typename T>
Token<T> Calc<T>::ucitaj(char ch)
{
	if (b.full) { b.full=false; return b.buffer; }
	switch (ch) {
	case '(':
	case ')':
	case '+':
	case '-':
	case '*':
	case '/':
	case '=':{
		ulazni.pop_back();
		return Token<T>(ch);
	}
	case '0':
	case '1':
	case '2':
	case '3':
	case '4':
	case '5':
	case '6':
	case '7':
	case '8':
	case '9':
	{
		ulazni.pop_back();
		int broj = int(ch) - '0';
		int m = 10;
		//ako je dvocifreni broj
		while (true){
			char pom = ulazni.back();
			if (int(pom) > 47 and int(pom) < 58){
				broj = broj*m + (int(pom) - '0');
				ulazni.pop_back();
			}
			else{
				break;
			}
		}
		//provera jel postoji taj broj u izboru
		for (int i = 0; i < 6; i ++){
			if (nekorisceni[i] == broj){
				nekorisceni[i] = -1;
				return Token<T>('8', broj);
			}
		}
		error("Number does not exist");
		break;
	}
	default:
		error("Bad token");
	}
	return Token<T>(0);
}

template <typename T> T
Calc<T>::primary()
{
	t = ucitaj(ulazni.back());
	switch (t.kind) {
	case '(':
	{	double d = expression();
		t = ucitaj(ulazni.back());
		if (t.kind != ')') error("'(' expected");
		return d;
	}
	case '-':
		return - primary();
	case '8':
		return t.value;
	default:
		error("primary expected");
		return 0;
	}
}

template <typename T> T
Calc<T>::term()
{
	T left = primary();
	while(true) {
		t = ucitaj(ulazni.back());
		switch(t.kind) {
		case '*':
			left *= primary();
			break;
		case '/':
		{	double d = primary();
			if (d == 0) error("divide by zero");
			if (std::is_same<T, int>::value or std::is_same<T, short>::value or std::is_same<T, long>::value){
				if (int(left) % int(d) != 0){
					error("D");
				}
			}
			left /= d;
			break;
		}
		default:
			b.buffer = t;
			b.full = true;
			return left;
		}
	}
}

template <typename T>
T Calc<T>::expression()
{
	T left = term();
	while(true) {
		t = ucitaj(ulazni.back());
		switch(t.kind) {
		case '+':
			left += term();
			break;
		case '-':
			left -= term();
			break;
		default:
			b.buffer = t;
			b.full = true;
			return left;
		}
	}
}

//od stringa pravi vektor karaktera i poziva funkciju za racunanje
//cuva prvi ucitani u bafer
//izuzetak ako nemamo isti broj otvorenih i zatvorenih zagrada
template <typename T>
T Calc<T>::calc(string ulaz)
{
	int otvorene = 0;
	int zatvorene = 0;
	//unesen string u vector
	char niz_ulaz[ulaz.length() + 1];
	strcpy(niz_ulaz, ulaz.c_str());
	for (int i = ulaz.length()-1; i >= 0; i--){
		if (niz_ulaz[i] == '(')
			otvorene ++;
		if (niz_ulaz[i] == ')')
			zatvorene ++;
		ulazni.push_back(niz_ulaz[i]);
	}

	if (otvorene != zatvorene)
		error("Nejednak broj zagrada!");

	//ucitamo prvi u token i u baffer
	t = ucitaj(ulazni.back());

	b.buffer = t;
	b.full = true;

	return expression();
}

//resetujem brojeve da su svi nekorisceni
template <typename T>
void Calc<T>::resetBrojevi(){
	for (int i = 0; i < 6; i++){
		nekorisceni[i] = brojevi[i];
	}
}

//funkcija koja prima string i vraca najbolji rezultat
//oslanja se na sve ostale funkcije
template <typename T>
T Calc<T>::calculate(string ulaz){
	resetBrojevi();
	try {
		T rez = calc(ulaz);
		b = Buffer<T>();
		return rez;
	}
	catch (exception& e){
		if (e.what()[0] == 'D'){
			return -2;
		}
		return -1;
	}
}
