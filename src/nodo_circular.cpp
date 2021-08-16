#include "../include/nodo_circular.h"

nodo_circular::nodo_circular()
{
    //Se inicializan las variables
    this->carnet="";
    this->dpi="";
    this->nombre="";
    this->carrera="";
    this->pass="";
    this->creditos=0;
    this->edad=0;
    this->correo="";

    //Apuntadores
    this->siguiente=nullptr;
    this->anterior=nullptr;
}

nodo_circular::~nodo_circular()
{
    //dtor
}
