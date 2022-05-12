package com.company;

public class Main {

    public static void main(String[] args) {
        Persona persona = new Persona();

        persona.setNombre("Jose Perez");
        persona.setEdad(20);
        persona.setTelefono(77644433);

        System.out.println("Nombre: "+persona.getNombre());
        System.out.println("Edad: "+persona.getEdad());
        System.out.println("Telefono: "+persona.getTelefono());


    }
}

class Persona{
    private  int edad;
    private String nombre;
    private int telefono;

    public void setEdad(int edad){
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