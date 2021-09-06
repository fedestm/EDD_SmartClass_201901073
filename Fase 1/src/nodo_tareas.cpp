#include "nodo_tareas.h"

nodo_tareas::nodo_tareas()
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
    this->id=0;
    this->mes="";
    this->dia="";
}

nodo_tareas::~nodo_tareas()
{
    //dtor
}
