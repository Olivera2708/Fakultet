#include <iostream>

using namespace std;
#pragma once

class Complex {
private:
	double real, imag;

public:
	Complex();
	Complex(double a, double b);

	const double getReal();
	const double getImag();
	void setReal(double r);
	void setImag(double i);
	const Complex& add(Complex& c);
	const Complex& sub(Complex& c);
	const Complex& mul(Complex& c);
	const Complex& mul(int s);
	const Complex& conj();

	friend istream& operator >> (istream &_in, Complex &_c);
	friend ostream& operator << (ostream &_out, Complex &_c);

	Complex operator+(Complex _c);
	Complex operator-(Complex _c);
	Complex operator*(Complex _c);
	Complex operator*(int s);
	Complex operator~();

	friend Complex operator*(int s, Complex& _c);
};
