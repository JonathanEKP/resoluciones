package com.company;

public class Main {

    public static void main(String[] args) {

        Cliente cliente = new Cliente();
        cliente.setEdad(20);
        cliente.setNombre("Jose Perez");
        cliente.setTelefono(78855145);
        cliente.setCredito(250.4);

        System.out.println("Edad del cliente: "+cliente.getEdad());
        System.out.println("Nombre del cliente: "+cliente.getNombre());
        System.out.println("Telefono del cliente: "+cliente.getTelefono());
        System.out.println("Credito del cliente: "+cliente.getCredito());
        System.out.println("");
        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(30);
        trabajador.setNombre("Maria Sanchez");
        trabajador.setTelefono(65847835);
        trabajador.setSalario(1150.4);

        System.out.println("Edad del trabajador: "+trabajador.getEdad());
        System.out.println("Nombre del trabajador: "+trabajador.getNombre());
        System.out.println("Telefono del trabajador: "+trabajador.getTelefono());
        System.out.println("Salario del trabajador: "+trabajador.getSalario());

    }
}


class Persona{
    int edad;
    String nombre;
    int telefono;

    public void setEdad(int edad) {
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getNombre(){
        return this.nombre;
    }

    public void setTelefono(int telefono){
        this.telefono = telefono;
    }
    public int getTelefono(){
        return this.telefono;
    }
}

class Cliente extends Persona{
    double credito;

    public void setCredito(double credito){
        this.credito = credito;
    }
    public double getCredito(){
        return this.credito;
    }
}

class Trabajador extends Persona{
    double salario;

    public void setSalario(double salario){
        this.salario = salario;
    }
    public double getSalario(){
        return this.salario;
    }
}
