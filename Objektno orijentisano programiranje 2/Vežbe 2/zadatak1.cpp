#include <iostream>
#include <vector>
using namespace std;

void obrniNiz(int* niz, int duzina){
    for (int i = duzina - 1; i >= 0; i--){
        cout << niz[i] << endl;
    }
}

void obrniVektor(vector<int> vektor){
    for (int i = vektor.size() - 1; i >= 0; i--){
        cout << vektor.at(i) << endl;
    }
}

int main()
{
    vector<int> vektor;
    vektor.push_back(1);
    vektor.push_back(4);
    vektor.push_back(2);

    int niz[] = {1, 2, 3, 4, 5, 6};
    int duzina = 6;

    obrniNiz(niz, duzina);
    cout << "\n\n";
    obrniVektor(vektor);

    return 0;
}
