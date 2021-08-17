#include "include/cola.h"
#include <fstream>

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

void cola::desencolar(){
    nodo_cola *temp;
    if(this->cola_vacia()){
        cout<<"No hay datos en la cola"<<endl;
    }else{
        temp=this->primero;
        this->primero=temp->siguiente;
        temp=nullptr;
        this->cont--;
    }
}

void cola::graficar_cola(){
    nodo_cola *temp;
    if(this->cola_vacia()){
        cout<<"No hay datos en la cola"<<endl;
    }else{
        ofstream fs("cola.dot");
        fs<<"digraph Cola {"<<"\n"<<endl;
        fs << "rankdir = LR;\n" <<endl;
        fs << "\tnode [style=filled];" <<endl;
        fs << "label = \"Cola de Errores\"; \n"<<endl;
        fs << "color= black \n"<<endl;

        fs<<"\t}\n"<<endl;
        fs.close();
    }
}

cola::~cola()
{
    //dtor
}
