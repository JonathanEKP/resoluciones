package com.company;

public class Main {

    public static void main(String[] args) {

        //Parte 1
        System.out.println("Parte 1");
        int numerIf = -2;
        if (numerIf>0){
            System.out.println("El numero es positivo");
        }
        else if (numerIf<0){
            System.out.println("El numero es negativo");
        }
        else {
            System.out.println("El numero es 0");
        }

        //Parte 2
        System.out.println("Parte 2");
        int numeroWhile = 0;
        while (numeroWhile<3){
            System.out.println(numeroWhile);
            numeroWhile++;
        }

        //Parte 3
        int numeroWhile2=2;
        System.out.println("Parte 3");
        do {
            System.out.println(numeroWhile2);
            numeroWhile2++;
        }while (numeroWhile<3);

        //Parte 4
        System.out.println("Parte 4");
        int numeroFor=0;
        for (numeroFor=0; numeroFor<=3; numeroFor++){
            System.out.println(numeroFor);
        }
        //Parte 5
        System.out.println("Parte 5");
        var estacion = "invierno";
        switch (estacion){
            case "primavera":
                System.out.println("La estacion es primavera");
                break;
            case "verano":
                System.out.println("La estacion es verano");
                break;
            case "otoño":
                System.out.println("La estacion es otoño");
                break;
            case "invierno":
                System.out.println("La estacion es invierno");
                break;
            default:
                System.out.println("La estacion ingresada no existe");
        }

    }
}
