#include "nodo_doble.h"

nodo_doble::nodo_doble()
{
    this->anterior=nullptr;
    this->siguiente=nullptr;
    this->carnet="";
    this->nombre="";
    this->descripcion="";
    this->materia="";
    this->fecha="";
    this->hora="";
    this->estado="";
}

nodo_doble::~nodo_doble()
{
    //dtor
}
