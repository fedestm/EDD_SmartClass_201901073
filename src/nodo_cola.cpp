#include "nodo_cola.h"

nodo_cola::nodo_cola()
{
    this->siguiente=nullptr;
    this->id=0;
    this->tipo="";
    this->descripcion="";
}

nodo_cola::nodo_cola(nodo_cola *siguiente,int id,string tipo,string descripcion){
    this->siguiente=siguiente;
    this->id=id;
    this->tipo=tipo;
    this->descripcion=descripion;
}

nodo_cola::~nodo_cola()
{
    //dtor
}
