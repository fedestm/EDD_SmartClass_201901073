#include "../include/lista_circular.h"
#include <fstream>

lista_circular::lista_circular()
{
    this->primero=nullptr;
    this->ultimo=nullptr;
}

void lista_circular::insertar(string carnet,string dpi,string nombre,string carrera,string pass,int creditos,int edad,string correo){
    //Se crea un nuevo nodo
    nodo_circular *nuevo=new nodo_circular();
    //Se instancian las variables
    nuevo->carnet=carnet;
    nuevo->dpi=dpi;
    nuevo->nombre=nombre;
    nuevo->carrera=carrera;
    nuevo->pass=pass;
    nuevo->creditos=creditos;
    nuevo->edad=edad;
    nuevo->correo=correo;
    nuevo->siguiente=nullptr;
    nuevo->anterior=nullptr;

    //Se valida si el primer nodo esta vacio
    if(this->primero==nullptr){
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
    ofs<<"node [style=filled,color=\"#63EA30\"];"<<endl;
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
        ofs<<"n_"<<cont<<"[label=\"Carnet:"<<aux->carnet<<"\\nDPI: "<<aux->dpi<<"\\nNombre: "<<aux->nombre
        <<"\\nCarrera: "<<aux->carrera<<"\\nPassword: "<<aux->pass<<"\\nCreditos: "<<aux->edad
        <<"\\nEdad: "<<aux->edad<<"\\nCorreo: "<<aux->correo<<"\",shape=box];"<<endl;
        //Se recorren los nodos
        aux=aux->siguiente;
        cont++;
    }

    //Nodo en la ultima posicion
    ofs<<"n_"<<cont<<"[label=\"Carnet:"<<aux->carnet<<"\\nDPI: "<<aux->dpi<<"\\nNombre: "<<aux->nombre
    <<"\\nCarrera: "<<aux->carrera<<"\\nPassword: "<<aux->pass<<"\\nCreditos: "<<aux->edad
    <<"\\nEdad: "<<aux->edad<<"\\nCorreo: "<<aux->correo<<"\",shape=box];"<<endl;

    //Se recorren los nodos a los que van a apuntar
    for(int i=0;i<cont-1;i++){
        ofs<<"n_"<<i<<"->"<<"n_"<<i+1<<";"<<endl;
        ofs<<"n_"<<i+1<<"->"<<"n_"<<i<<";"<<endl;
    }

    ofs<<"n_"<<cont-1<<" ->"<<"n_"<<cont<<";"<<endl;
    ofs<<"n_"<<cont<<" ->"<<"n_"<<cont-1<<";"<<endl;

    ofs<<"n_0"<<" ->"<<"n_"<<cont<<":n"<<";"<<endl;
    ofs<<"n_"<<cont<<" ->"<<"n_0:s"<<";"<<endl;
    cout<<cont;

    ofs<<"}"<<endl;
    ofs.close();

    system("dot -Tpng lista_circular_doble.dot -o lista_circular_estudiantes.png");
    system("lista_circular_estudiantes.png &");

}

nodo_circular *lista_circular::buscar_estudiante(string dpi){
    if(this->primero==nullptr){
        cout<<"No hay datos en la lista"<<endl;
        return nullptr;
    }else{
        nodo_circular *temp=this->primero;
        while(temp->siguiente!=primero){
            if(temp->dpi==dpi){
                return temp;
            }else{
                temp=temp->siguiente;
            }
        }
        cout<<"No se encontro el estudiante"<<endl;
        return nullptr;
        }
}

nodo_circular *lista_circular::buscar_carnet(string carnet){
    if(this->primero==nullptr){
        cout<<"No hay datos en la lista"<<endl;
        return nullptr;
    }else{
        nodo_circular *temp=this->primero;
        while(temp->siguiente!=primero){
            if(temp->carnet==carnet){
                return temp;
            }else{
                temp=temp->siguiente;
            }
        }
        cout<<"No se encontro el estudiante"<<endl;
        return nullptr;
        }
}

void lista_circular::eliminar_estudiante(string dpi){
    //Se crea un nuevo nodo
    nodo_circular *temp=this->buscar_estudiante(dpi);

    if(temp!=nullptr){
        if(this->primero==this->ultimo){
            this->primero=nullptr;
            this->ultimo=nullptr;
        }else if(temp==this->primero){ //Se valida si el primero
            this->primero=temp->siguiente;
            //Se elimina la variable temporal
            temp->siguiente->anterior=nullptr;
        }else if(temp==this->ultimo){   //Se valida si es el ultimo
            this->ultimo=temp->anterior;
            temp->anterior->siguiente=nullptr;
        }else{
            temp->anterior->siguiente=temp->siguiente;
            temp->siguiente->anterior=temp->anterior;
        }

        temp->siguiente=nullptr;
        temp->anterior=nullptr;
        delete(temp);
        cout<<"Se borro el estudiante "<<dpi<<endl;
    }
}

lista_circular::~lista_circular()
{
    //dtor
}
