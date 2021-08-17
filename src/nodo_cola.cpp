#include "nodo_cola.h"

nodo_cola::nodo_cola()
{
    this->siguiente=nullptr;
    this->id=0;
    this->tipo="";
    this->descripcion="";
}

nodo_cola::~nodo_cola()
{
    //dtor
}
