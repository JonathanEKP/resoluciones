package com.company;

public class Main {

    public static void main(String[] args) {
       //Parte uno
        float resultado =  suma(10, 15,20);
        System.out.print("Resultado de la suma: ");
        System.out.println(resultado);
        //Parte dos
        Coche miCoche = new Coche();
        miCoche.AgregarPuertas();
        System.out.print("Numero de puertas: ");
        System.out.println(miCoche.puertas);
    }

    public static int suma (int a, int b, int c){
        return a+b+c;
    }


}

class Coche{
    int puertas = 2;

    public void AgregarPuertas(){
        this.puertas++;
    }
}