#include <iostream>
#include <vector>
using namespace std;

void parniNiz(int niz[], int duzina){
    for (int i = 0; i < duzina; i++){
        if (niz[i] % 2 == 0){
            cout << niz[i] << endl;
        }
    }
}

void parniVektori(vector<int> vektor){
    for (int i = 0; i < vektor.size(); i++){
        if (vektor.at(i) % 2 == 0){
            cout << vektor.at(i) << endl;
        }
    }
}

void unosNiza(){
    int duzina;
    cout << "Unesite duzinu niza -> ";
    cin >> duzina;
    int niz[duzina];

    for (int i = 0; i < duzina; i++){
        cout << "Unesite element niza -> ";
        cin >> niz[i];
    }

    parniNiz(niz, duzina);
}

void unosVektora(){
    int duzina;
    cout << "Unesite broj elemenata -> ";
    cin >> duzina;

    vector<int> vektor;

    for (int i = 0; i < duzina; i++){
        cout << "Unesite element vektora -> ";
        int input;
        cin >> input;
        vektor.push_back(input);
    }

    parniVektori(vektor);
}

int main(){

    unosNiza();
    cout << "\n\n";
    unosVektora();

    return 0;
}