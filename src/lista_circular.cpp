#include "../include/lista_circular.h"
#include <fstream>

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

    //Se valida sin el primer nodo esta vacio
    if(this->primero==NULL){
        nuevo->siguiente=nuevo;
        nuevo->anterior=nuevo;
        primero=nuevo;
        cout<<"Se inserto estudiante"<<endl;
    }else{
        //Si ya se encuentra un dato se guarda en el ultimo nodo
        ultimo=primero->anterior;
        //Se agregan los datos a dicho nodo
        nuevo->carnet=carnet;
        nuevo->dpi=dpi;
        nuevo->nombre=nombre;
        nuevo->carrera=carrera;
        nuevo->pass=pass;
        nuevo->creditos=creditos;
        nuevo->edad=edad;
        nuevo->correo=correo;
        nuevo->siguiente=primero;
        primero->anterior=nuevo;    //El puntero anterior se va al primero
        nuevo->anterior=ultimo;     //El puntero que se encuentra antes del ultimo se convierte en un nodo nuevo
        ultimo->siguiente=nuevo;    //El puntero siguiente se convierte en un nodo nuevo despues del puntero anterior
    }
}

void lista_circular::graficar(){
    ofstream ofs("lista_circular_doble.dot");
    //Sintaxis inicial de archivos dot
    ofs<<"digraph G{"<<endl;
    //Posicion Horizontal de nodos
    ofs<<"rankdir = LR;"<<endl;
    //Nodos con forma cuadrada, color verde
    ofs<<"node [shape=record,color=black fillcolor=\"#00ff005f\"];"<<endl;
    ofs<<"label=\"Lista doble circular\""<<endl;
    ofs<<"color=black"<<endl;

    //Se declara una variable auxiliar para recorrer los nodos
    //por medio del apuntador siguiente 
    //Hara uso tanto de dichos apuntadores como de los datos del estudiante
    nodo_circular *aux=this->primero;

    //Se declara contador para la cantidad de nodos
    int cont=0;
    //Se verifica si el nodo siguiente no se encuentre primero
    while(aux->siguiente!=primero){
        //Se crea codigo unico de cada nodo
        //Se guardan los datos en un label
        ofs<<"n_"<<cont<<"[label=\"Carnet:"<<aux->carnet<<"\nDPI: "<<aux->dpi<<"\nNombre: "<<aux->nombre
        <<"\nCarrera: "<<aux->carrera<<"\nPassword: "<<aux->pass<<"\nCreditos: "<<aux->edad
        <<"\nEdad: "<<aux->edad<<"\nCorreo: "<<aux->correo<<"\"];"<<endl;
        //Se recorren los nodos
        aux=aux->siguiente;
        cont++;
    }

    //Nodo en la ultima posicion
    ofs<<"n_"<<cont<<"[label=\"Carnet:"<<aux->carnet<<"\nDPI: "<<aux->dpi<<"\nNombre: "<<aux->nombre
    <<"\nCarrera: "<<aux->carrera<<"\nPassword: "<<aux->pass<<"\nCreditos: "<<aux->edad
    <<"\nEdad: "<<aux->edad<<"\nCorreo: "<<aux->correo<<"\"];"<<endl;

    int cont_ultimo;

    //Se recorren los nodos a los que van a apuntar
    for(int i=0;i<cont-1;i++){
    }
    

}

lista_circular::~lista_circular()
{
    //dtor
}
