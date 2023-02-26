#include <iostream>
#include <vector>
using namespace std;

void prebrojNiz(int* niz, int duzina){
    int parni = 0;
    int neparni = 0;

    for (int i = 0; i < duzina; i++){
        if (niz[i] % 2 == 0)
            parni ++;
        else
            neparni ++;
    }
    cout << "Broj parni elemenata niza je " << parni << endl;
    cout << "Broj neparnih elemenata niza je " << neparni << endl;
}

void prebrojVektor(vector<int> vektor){
    int parni = 0;
    int neparni = 0;

    for (int i = 0; i < vektor.size(); i++){
        if (vektor.at(i) % 2 == 0)
            parni ++;
        else
            neparni ++;
    }
    cout << "Broj parni elemenata vektora je " << parni << endl;
    cout << "Broj neparnih elemenata vektora je " << neparni << endl;
}

int main()
{
    vector<int> vektor;
    vektor.push_back(1);
    vektor.push_back(4);
    vektor.push_back(2);

    int niz[] = {1, 2, 3, 4, 5, 6};
    int duzina = 6;

    prebrojNiz(niz, duzina);
    cout << "\n\n";
    prebrojVektor(vektor);

    return 0;
}
