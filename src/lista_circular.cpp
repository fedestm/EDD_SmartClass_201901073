#include "../include/lista_circular.h"
#include <fstream>

lista_circular::lista_circular()
{
    this->primero=NULL;
    this->ultimo=NULL;
}

void lista_circular::insertar(string carnet,string dpi,string nombre,string carrera,string pass,int creditos,int edad,string correo){
    nodo_circular *nuevo=new nodo_circular();
    nuevo->carnet=carnet;
    nuevo->dpi=dpi;
    nuevo->nombre=nombre;
    nuevo->carrera=carrera;
    nuevo->pass=pass;
    nuevo->creditos=creditos;
    nuevo->edad=edad;
    nuevo->correo=correo;
    nuevo->siguiente=NULL;
    nuevo->anterior=NULL;

    //Se valida sin el primer nodo esta vacio
    if(this->primero==NULL){
        nuevo->siguiente=nuevo;
        nuevo->anterior=nuevo;
        primero=nuevo;
        cout<<"Se inserto estudiante"<<endl;
    }else{
        //Si ya se encuentra un dato se guarda en el ultimo nodo
        ultimo=primero->anterior;
        //Se agregan los datos a dicho nodo
        nuevo->carnet=carnet;
        nuevo->dpi=dpi;
        nuevo->nombre=nombre;
        nuevo->carrera=carrera;
        nuevo->pass=pass;
        nuevo->creditos=creditos;
        nuevo->edad=edad;
        nuevo->correo=correo;
        nuevo->siguiente=primero;
        primero->anterior=nuevo;    //El puntero anterior se va al primero
        nuevo->anterior=ultimo;     //El puntero que se encuentra antes del ultimo se convierte en un nodo nuevo
        ultimo->siguiente=nuevo;    //El puntero siguiente se convierte en un nodo nuevo despues del puntero anterior
    }
}

void lista_circular::graficar(){
    ofstream fs("lista_circular_doble.dot");
}

lista_circular::~lista_circular()
{
    //dtor
}
