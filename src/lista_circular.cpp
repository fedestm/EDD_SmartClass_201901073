#include "../include/lista_circular.h"

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
}

lista_circular::~lista_circular()
{
    //dtor
}
