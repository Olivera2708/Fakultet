class Main {
    public static void main(String args[]){
        // Prvi zadatak
        String string = obrnislova("Obrni ovaj tekst");
        System.out.println(string);

        string = obrnireci("Obrni ovaj tekst");
        System.out.println(string);

        // Drugi zadatak
        System.out.println("ZADATAK KOJI GLEDAM");
        String[][] matrica = kreirajMatricu("4,3,2,1;0,1,0;1,2,3,4");

        for (int i = 0; i < matrica.length; i++){
            for (int j = 0; j < matrica[i].length; j++){
                System.out.print(matrica[i][j] + " ");
            }
            System.out.println("");
        }

        // Cetvrti zadatak
        int[] a = {2, 5, 7, 9, 12};
        int[] b = {6, 8, 23, 4, 9};
        int[] c = saberi(a, b);

        for (int el : c){
            System.out.print(el + " ");
        }
    }

    static String obrnireci(String tekst){
        String novi = "";
        String[] lista = tekst.split(" ");
        for (int i = lista.length - 1; i >= 0; i--){
            novi += lista[i] + " ";
        }
        return novi;
    }

    static String obrnislova(String tekst){
        String novi = "";
        for (int i = tekst.length() - 1; i >= 0; i--){
            novi += tekst.charAt(i);
        }
        return novi;
    }

    static String[][] kreirajMatricu(String string){
        String niz[] = string.split(";");
        int kolone = 0;
        for (int i = 0; i < niz.length; i++){
            if (kolone < niz[i].split(",").length)
                kolone = niz[i].split(",").length;
        }
        String[][] mat = new String[niz.length][kolone];
        for (int i = 0; i < niz.length; i++){
            String[] podela = niz[i].split(",");
            for (int j = 0; j < kolone; j++){
                try{
                    mat[i][j] = podela[j];
                }
                catch (Exception e){
                    mat[i][j] = "";
                }
            }
        }
        return mat;
    }

    static int[] saberi(int[] a, int[] b){
        int[] c = new int[a.length];
        for (int i = 0; i<a.length; i++){
            c[i] = a[i] + b[i];
        }
        return c;
    }
}