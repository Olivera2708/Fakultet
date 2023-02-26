#include "MojBroj.h"
#include "Calc.h"
using namespace std;


int main(int argc, char** argv) {
	MojBroj mojBroj;
	mojBroj.otvoriFajl(argv[1]);
	mojBroj.pokreniIgru();
}
