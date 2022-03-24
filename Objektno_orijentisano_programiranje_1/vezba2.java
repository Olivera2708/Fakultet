class Main{
    public static void main(String agrs[]){
        // Prvi zadatak
        for (int i = 10; i > 0; i--){
            System.out.println(i);
        }

        // Drugi zadatak
        int br = 0;
        for (float i = -1; i < 1.5; i += 0.25){
            br++;
        }
        System.out.println(br);

        // Treci zadatak
        int niz[] = new int[10];
        for (int i = 0; i < niz.length; i++){
            if (i == 0)
                niz[i] = 10;
            else
                niz[i] = niz[i-1] + 10;
        }

        // Cetvrti zadatak
        for (int i = 0; i < 10; i++){
            for (int j = 0; j < 10; j++){
                System.out.print(" Polje ");
            }
            System.out.println("");
        }

        // Peti zadatak
        int rez = 1;
        for (int i = 10; i < 20; i += 2){
            rez *= i;
        }
        System.out.println(rez);

        // Sedmi zadatak
        int a[] = {-10, 3, 16, 1, 4, -2};
        int min = a[0];
        int max = a[0];
        int sr = 0;
        for (int i = 0; i < a.length; i++){
            if (min > a[i])
                min = a[i];
            if (max < a[i])
                max = a[i];
            sr += a[i];
        }
        System.out.println("Max -> " + max);
        System.out.println("Min -> " + min);
        sr /= a.length;
        for (int i = 0; i < a.length; i++){
            if (sr > a[i]){
                System.out.print(a[i] + " ");
            }
        }
        System.out.println("");

        // Osmi i deveti zadatak
        int suma = 0;
        for (int i = 0; i < 7; i++){
            for (int j = i; j < i + 5; j++){
                System.out.print(" " + j + " ");
                if (i == j)
                suma += j;
            }
            System.out.println("");
        }
        System.out.println(suma);
    }
}
