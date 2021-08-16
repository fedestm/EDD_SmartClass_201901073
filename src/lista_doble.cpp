#include "lista_doble.h"

lista_doble::lista_doble()
{
    this->primero=nullptr;
    this->ultimo=nullptr;
}

void lista_doble::insertar_tarea(string tarea){

    //Se crea un nodo nuevo
    nodo_doble *nuevo=new nodo_doble();
    //Se instancian con las variables de dicho nodo
    nuevo->tarea=tarea;
    nuevo->siguiente=nullptr;
    nuevo->anterior=nullptr;

    //Se valida si el primero nodo esta vacio
    if(this->primero==nullptr){
        this->primero=nuevo;
        this->ultimo=nuevo;
    }else{
        //Si ya se encuentra un dato se guarda en el ultimo nodo
        if(this->primero==this->ultimo){
            this->primero->siguiente=nuevo;
            nuevo->anterior=this->primero;
            this->ultimo=nuevo;
        }
    }
}

lista_doble::~lista_doble()
{
    //dtor
}
