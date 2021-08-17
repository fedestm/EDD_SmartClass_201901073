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

cola::~cola()
{
    //dtor
}
