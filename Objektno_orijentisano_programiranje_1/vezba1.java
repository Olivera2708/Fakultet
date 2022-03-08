import java.util.Scanner;

class Main{
    public static void main(String[] args){
        // Prvi zadatak
        System.out.print("A\nB\n\tB.1\n\t\tB.1.1\n\tB.2\nC\n\n");

        // Drugi zadatak
        int pov_kvadrata = 16, a_a = 4, b_b = 6;
        double kva = Math.sqrt(pov_kvadrata);
        double ha = Math.sqrt(b_b*b_b-a_a*a_a/4);
        double pov_trougla = a_a*ha/2;
        System.out.printf("Stranica kvadrata = %f\nPovrsina trougla = %f\n", kva, pov_trougla);

        // Treci zadatak
        Scanner input = new Scanner(System.in);
        System.out.print("Unesite godinu -> ");
        int godina = input.nextInt();
        if (godina < 1538)
            System.out.println("Greska");
        else {
            if (prestupna(godina)) 
                System.out.printf("Godina %d. je prestupna\n", godina);
            else
                System.out.printf("Godina %d. nije prestupna\n", godina);
        }

        // Cetvrti zadatak
        System.out.print("Unesite rastojanje u centimetrima -> ");
        int cm = input.nextInt();
        int m = (int) cm / 100;
        int dm = (int) cm / 10;
        System.out.printf("Metara: %d\nDecimetara: %d\n", m, dm);
        
        // Peti zadatak
        int a_kv = 3, b_kv = 4, c_kv = 5;
        int povrsina = 2*(a_kv*b_kv + a_kv*c_kv + b_kv*c_kv);
        int zapremina = a_kv*b_kv*c_kv;
        System.out.printf("Povrsina = %d\nZapremina = %d\n", povrsina, zapremina);

        // Sesti zadatak
        int r_kupe = 6, h_kupe = 4;
        double s_kupe = Math.sqrt(r_kupe*r_kupe + h_kupe*h_kupe);
        double pov_kupe = r_kupe*Math.PI*(s_kupe + r_kupe);
        System.out.printf("Povrsina kupe je %f\n", pov_kupe);

        // Sedmi zadatak
        System.out.print("Unesite x -> ");
        int x = input.nextInt();
        System.out.print("Unesite y -> ");
        int y = input.nextInt();
        double z_izlaz = 0;
        if (x < y)
            z_izlaz = (double) Math.max(x, y)/(1 + Math.abs(Math.min(x, y)));
        else
            z_izlaz = (double) Math.max(x, y)/(1 + Math.min(x, y));
        System.out.printf("z = %f\n", z_izlaz);

        // Osmi zadatak
        System.out.print("Unesite a -> ");
        int a = input.nextInt();
        System.out.print("Unesite b -> ");
        int b = input.nextInt();
        System.out.print("Unesite c -> ");
        int c = input.nextInt();
        double rez1, rez2;

        double d = b*b - 4*a*c;
        if (d > 0) {
            rez1 = (-b + Math.sqrt(d))/(2 * a);
            rez2 = (-b - Math.sqrt(d))/(2 * a);
            System.out.printf("Postoje dva resenja i ona su:\nx1 = %f\nx2 = %f\n", rez1, rez2);
        }
        else if (d == 0){
            rez1 = (-b)/(2 * a);
            System.out.printf("Postoji jedno resenje i ono je:\nx1 = %f\n", rez1);
        }
        else {
            System.out.print("Ne postoje realna resenja\n");
        }
        
        input.close();
    }

    public static boolean prestupna(int godina) {
        if ((godina % 400 == 0) || ((godina % 100 != 0) && (godina % 4 == 0))) {
            return true;
        }
        return false;
    }
}