#include <iostream>
#include "myComplex.h";

Complex::Complex() : real(0.0), imag(0.0) {}
Complex::Complex(double a, double b) : real(a), imag(b) {}

const double Complex::getReal() {
	return this->real;
}
const double Complex::getImag() {
	return this->imag;
}

void Complex::setReal(double r) {
	this->real = r;
}
void Complex::setImag(double i) {
	this->imag = i;
}

const Complex& Complex::add(Complex& c) {
	Complex res(this->real + c.getReal(), this->imag + c.getImag());

	return res;
}

const Complex& Complex::sub(Complex& c) {
	Complex res(this->real - c.getReal(), this->imag - c.getImag());

	return res;
}

const Complex& Complex::mul(Complex& c) {
	Complex res((this->real * c.getReal() - this->imag * c.getImag()), (this->real * c.getImag() + this->imag * c.getReal()));

	return res;
}

const Complex& Complex::mul(int s) {
	Complex res((this->real * s), (this->imag * s));

	return res;
}

const Complex& Complex::conj() {
	Complex res(this->real, -(this->imag));

	return res;
}

istream& operator >> (istream &_in, Complex &_c) {
	double real;
	double imag;
	_in >> real;
	_in >> imag;
	_c.setReal(real);
	_c.setImag(imag);
	return _in;
}

ostream& operator << (ostream &_out, Complex &_c) {
	float real;
	float imag;
	_out << "(" << _c.getReal() << ", " << _c.getImag() << "i)";
	return _out;
}

Complex Complex::operator+(Complex _c) {
	return this->add(_c);
}

Complex Complex::operator-(Complex _c) {
	return this->sub(_c);
}

Complex Complex::operator*(Complex _c) {
	return this->mul(_c);
}

Complex Complex::operator*(int s) {
	return this->mul(s);
}

Complex Complex::operator~() {
	return this->conj();
}

Complex operator*(int s, Complex& _c) {
	return _c.mul(s);
}
