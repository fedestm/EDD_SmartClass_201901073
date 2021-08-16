#include "lista_doble.h"
#include <fstream>

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
        }else{
            nuevo->anterior=this->ultimo;
            this->ultimo->siguiente=nuevo;
            this->ultimo=nuevo;
        }
    }
}

void lista_doble::graficar_tarea(){

    ofstream ofs("lista_doblemente_enlazada.dot");
    //Sintaxis basica de archivos dot
    ofs<<"digraph Lista_Doble{\n"<<endl;
    ofs<<"rankdir = LR;"<<endl;
    ofs<<"node [style=filled];"<<endl;
    ofs<<"label=\"Lista Doblemente Enlazada\""<<endl;
    ofs<<"color=black"<<endl;
    ofs<<"}"<<endl;
    ofs.close();
}

lista_doble::~lista_doble()
{
    //dtor
}
