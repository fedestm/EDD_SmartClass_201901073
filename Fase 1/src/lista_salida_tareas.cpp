#include "lista_salida_tareas.h"

lista_salida_tareas::lista_salida_tareas()
{
    this->primero=nullptr;
    this->ultimo=nullptr;
    this->cont=0;
}

void lista_salida_tareas::insertar_tarea(int id,string mes,string dia,string carnet,string nombre,string desc,string materia,string fecha,string hora,string estado){
    //Se crea un nodo nuevo
    nodo_tareas *nuevo=new nodo_tareas();
    //Se instancian con las variables de dicho nodo
    nuevo->id=cont+1;
    nuevo->mes=mes;
    nuevo->dia=dia;
    nuevo->carnet=carnet;
    nuevo->nombre=nombre;
    nuevo->descripcion=desc;
    nuevo->materia=materia;
    nuevo->fecha=fecha;
    nuevo->hora=hora;
    nuevo->estado=estado;
    nuevo->siguiente=nullptr;
    nuevo->anterior=nullptr;

    //Se valida si el primero nodo esta vacio
    if(this->primero==nullptr){
        this->primero=nuevo;
        this->ultimo=nuevo;
    }else{
        //Si ya se encuentra un dato se guarda en el ultimo nodo
        if(this->primero==this->ultimo){
            this->primero->siguiente=nuevo;
            nuevo->anterior=this->primero;
            this->ultimo=nuevo;
        }else{
            nuevo->anterior=this->ultimo;
            this->ultimo->siguiente=nuevo;
            this->ultimo=nuevo;
        }
    }
    this->cont++;
}


string lista_salida_tareas::salida_tarea(){

    string salida="";
    string nulos="";
    nodo_tareas *temp=this->primero;
    //Se declara contador para la cantidad de nodos
    int cont=0;
    //Se verifica si el nodo siguiente no se encuentre primero
    while(temp!=nullptr){
        if(temp->materia=="-1"){
            if(temp==this->primero){
                nulos+="-1";
            }else if(temp==this->ultimo){
                nulos+="-1";
            }else{
                nulos+="-1";
            }
        }else{
            if(temp==this->primero){
                salida+="\t¿element type=\"task\"?\n";
                salida+="\t\t¿item Carnet = \""+temp->carnet+"\" $?\n";
                salida+="\t\t¿item Nombre = \""+temp->nombre+"\" $?\n";
                salida+="\t\t¿item Descripcion = \""+temp->descripcion+"\" $?\n";
                salida+="\t\t¿item Materia = \""+temp->materia+"\" $?\n";
                salida+="\t\t¿item Fecha = \""+temp->fecha+"\" $?\n";
                salida+="\t\t¿item Hora = \""+temp->hora+"\":00 $?\n";
                salida+="\t\t¿item Estado = \""+temp->estado+"\" $?\n";
                salida+="\t¿$element?\n";
            }else if(temp==this->ultimo){
                salida+="\t¿element type=\"task\"?\n";
                salida+="\t\t¿item Carnet = \""+temp->carnet+"\" $?\n";
                salida+="\t\t¿item Nombre = \""+temp->nombre+"\" $?\n";
                salida+="\t\t¿item Descripcion = \""+temp->descripcion+"\" $?\n";
                salida+="\t\t¿item Materia = \""+temp->materia+"\" $?\n";
                salida+="\t\t¿item Fecha = \""+temp->fecha+"\" $?\n";
                salida+="\t\t¿item Hora = \""+temp->hora+"\":00 $?\n";
                salida+="\t\t¿item Estado = \""+temp->estado+"\" $?\n";
                salida+="\t¿$element?\n";
            }else{
                salida+="\t¿element type=\"task\"?\n";
                salida+="\t\t¿item Carnet = \""+temp->carnet+"\" $?\n";
                salida+="\t\t¿item Nombre = \""+temp->nombre+"\" $?\n";
                salida+="\t\t¿item Descripcion = \""+temp->descripcion+"\" $?\n";
                salida+="\t\t¿item Materia = \""+temp->materia+"\" $?\n";
                salida+="\t\t¿item Fecha = \""+temp->fecha+"\" $?\n";
                salida+="\t\t¿item Hora = \""+temp->hora+"\":00 $?\n";
                salida+="\t\t¿item Estado = \""+temp->estado+"\" $?\n";
                salida+="\t¿$element?\n";

            }
        }

        //Se recorren los nodos
        temp=temp->siguiente;
        cont++;
    }
    return salida;
}



lista_salida_tareas::~lista_salida_tareas()
{
    //dtor
}
