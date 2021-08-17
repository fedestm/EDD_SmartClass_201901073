#include "cola.h"

cola::cola()
{
    //ctor
    this->primero=nullptr;
    this->ultimo=nullptr;
    this->cont=0;
}

int cola::cola_vacia(){
    return this->primero==nullptr;
}

void cola::encolar(int id,string tipo,string descripcion){
    nodo_cola *nuevo=new nodo_cola(nullptr,id,tipo,descripcion);
    if(this->cola_vacia()){
        this->primero=nuevo;
        this->ultimo=nuevo;
    }else{
        this->ultimo->siguiente=nuevo;
        this->ultimo=nuevo;
    }
    this->cont++;
}

cola::~cola()
{
    //dtor
}
