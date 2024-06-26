#include "../include/lista_doble.h"
#include <fstream>

lista_doble::lista_doble()
{
    this->primero=nullptr;
    this->ultimo=nullptr;
    this->cont=0;
}

void lista_doble::insertar_tarea(int id,string mes,string dia,string carnet,string nombre,string desc,string materia,string fecha,string hora,string estado){
    //Se crea un nodo nuevo
    nodo_doble *nuevo=new nodo_doble();
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

nodo_doble * lista_doble::buscar_tarea(int id){
    if(this->primero==nullptr){
        cout<<"No hay tareas en la lista"<<endl;
        return nullptr;
    }else{
        nodo_doble *temp=this->primero;
        while(temp!=nullptr){
            if(temp->id==id){
                cout<<"Carnet: "<<temp->carnet<<endl;
                return temp;
            }else{
                temp=temp->siguiente;
            }
        }
        cout<<"No existe la tarea"<<endl;
        return nullptr;
    }
}
nodo_doble *lista_doble::buscar_estructura(string mes,string dia,string hora){
    if(this->primero==nullptr){
        cout<<"No hay tareas en la lista"<<endl;
        return nullptr;
    }else{
        nodo_doble *temp=this->primero;
        while(temp!=nullptr){
            if(temp->mes==mes && temp->dia==dia && temp->hora==hora){

                cout<<"\n----------Informacion de Tarea------------\nCarnet: "<<temp->carnet<<"\n";
                cout<<"Nombre: "<<temp->nombre<<"\n";
                cout<<"Descripcion: "<<temp->descripcion<<"\n";
                cout<<"Materia: "<<temp->materia<<"\n";
                cout<<"Fecha: "<<temp->fecha<<"\n";
                cout<<"Hora: "<<temp->hora<<"\n";
                cout<<"Estado: "<<temp->estado<<"\n";
                cout<<"************************************************************"<<endl;
                return temp;
            }else{
                temp=temp->siguiente;
            }
        }
        cout<<"No existe la tarea"<<endl;
        return nullptr;
    }
}

nodo_doble *lista_doble::buscar_posicion(string mes,string dia,string hora){
    if(this->primero==nullptr){
        cout<<"No hay tareas en la lista"<<endl;
        return nullptr;
    }else{
        nodo_doble *temp=this->primero;
        while(temp!=nullptr){
            if(temp->mes==mes && temp->dia==dia &&temp->hora==hora){
                cout<<"\n-----------Posicion----------------------"<<endl;
                cout<<"\nPosicion: "<<temp->id<<endl;
                return temp;
            }else{
                temp=temp->siguiente;
            }
        }
        cout<<"No existe la tarea"<<endl;
        return nullptr;
    }
}

void lista_doble::modificar_tarea_carnet(int id,string carnet){
    nodo_doble *nuevo=this->buscar_tarea(id);
    if(nuevo==this->primero){
        nuevo->carnet=carnet;
    }else if(this->primero==this->ultimo){
        nuevo->carnet=carnet;
    }else{
        nuevo->carnet=carnet;
    }
}

void lista_doble::modificar_tarea_nombre(int id,string nombre){
    nodo_doble *nuevo=this->buscar_tarea(id);
    if(nuevo==this->primero){
        nuevo->nombre=nombre;
    }else if(this->primero==this->ultimo){
        nuevo->nombre=nombre;
    }else{
        nuevo->nombre=nombre;
    }
}
void lista_doble::modificar_tarea_desc(int id,string desc){
    nodo_doble *nuevo=this->buscar_tarea(id);
    if(nuevo==this->primero){
        nuevo->descripcion=desc;
    }else if(this->primero==this->ultimo){
        nuevo->descripcion=desc;
    }else{
        nuevo->descripcion=desc;
    }
}
void lista_doble::modificar_tarea_materia(int id,string materia){
    nodo_doble *nuevo=this->buscar_tarea(id);
    if(nuevo==this->primero){
        nuevo->materia=materia;
    }else if(this->primero==this->ultimo){
        nuevo->materia=materia;
    }else{
        nuevo->materia=materia;
    }
}
void lista_doble::modificar_tarea_fecha(int id,string fecha){
    nodo_doble *nuevo=this->buscar_tarea(id);
    if(nuevo==this->primero){
        nuevo->fecha=fecha;
    }else if(this->primero==this->ultimo){
        nuevo->fecha=fecha;
    }else{
        nuevo->fecha=fecha;
    }
}
void lista_doble::modificar_tarea_hora(int id,string hora){
    nodo_doble *nuevo=this->buscar_tarea(id);
    if(nuevo==this->primero){
        nuevo->hora=hora;
    }else if(this->primero==this->ultimo){
        nuevo->hora=hora;
    }else{
        nuevo->hora=hora;
    }
}

void lista_doble::modificar_tarea_estado(int id,string estado){
    nodo_doble *nuevo=this->buscar_tarea(id);
    if(nuevo==this->primero){
        nuevo->estado=estado;
    }else if(this->primero==this->ultimo){
        nuevo->estado=estado;
    }else{
        nuevo->estado=estado;
    }
}



void lista_doble::eliminar_tarea(int id){
    nodo_doble *temp=this->buscar_tarea(id);
    if(temp!=nullptr){
        if(this->primero==this->ultimo){
            this->primero=nullptr;
            this->ultimo=nullptr;
        }else if(temp==this->primero){
            this->primero=temp->siguiente;
            temp->siguiente->anterior=nullptr;
        }else if(temp==this->ultimo){
            this->ultimo=temp->anterior;
            temp->anterior->siguiente=nullptr;
        }else{
            temp->anterior->siguiente=temp->siguiente;
            temp->siguiente->anterior=temp->anterior;
        }
        temp->siguiente=nullptr;
        temp->anterior=nullptr;
        delete(temp);
    }
}


void lista_doble::graficar_tarea(){

    ofstream ofs("lista_doblemente_enlazada.dot");
    //Sintaxis basica de archivos dot
    ofs<<"digraph Lista_Doble{\n"<<endl;
    ofs<<"rankdir = LR;"<<endl;
    ofs<<"node [style=filled];"<<endl;
    ofs<<"label=\"Lista Doblemente Enlazada\""<<endl;
    ofs<<"color=black"<<endl;
    //Contador
    int cont=0;
    //Se declara una variable auxiliar para recorrer los nodos
    nodo_doble *temp=this->primero;
    while(temp!=nullptr){
        if(temp->descripcion=="-1"){
            if(temp==this->primero){
                ofs<<"n_"<<cont<<"[label=\"-1"<<"\",shape=box,shape=box,color=\"#3396FF\"];"<<endl;
            }else if(temp==this->ultimo){
                ofs<<"n_"<<cont<<"[label=\"-1"<<"\",shape=box,shape=box,color=\"#3396FF\"];"<<endl;
            }else{
                ofs<<"n_"<<cont<<"[label=\"-1"<<"\",shape=box,shape=box,color=\"#3396FF\"];"<<endl;
        }
        }else{
            if(temp==this->primero){
            ofs<<"n_"<<cont<<"[label=\"Carnet: "<<temp->carnet<<"\\nNombre: "<<temp->nombre<<"\\nDescripcion: "<<temp->descripcion
            <<"\\nMateria: "<<temp->materia<<"\\nFecha: "<<temp->fecha<<"\\nHora: "<<temp->hora
            <<"\\nEstado: "<<temp->estado<<"\",shape=box,shape=box,color=\"#3396FF\"];"<<endl;
        }else if(temp==this->ultimo){
            ofs<<"n_"<<cont<<"[label=\"Carnet: "<<temp->carnet<<"\\nNombre: "<<temp->nombre<<"\\nDescripcion: "<<temp->descripcion
            <<"\\nMateria: "<<temp->materia<<"\\nFecha: "<<temp->fecha<<"\\nHora: "<<temp->hora
            <<"\\nEstado: "<<temp->estado<<"\",shape=box,shape=box,color=\"#3396FF\"];"<<endl;
        }else{
            ofs<<"n_"<<cont<<"[label=\"Carnet: "<<temp->carnet<<"\\nNombre: "<<temp->nombre<<"\\nDescripcion: "<<temp->descripcion
            <<"\\nMateria: "<<temp->materia<<"\\nFecha: "<<temp->fecha<<"\\nHora: "<<temp->hora
            <<"\\nEstado: "<<temp->estado<<"\",shape=box,shape=box,color=\"#3396FF\"];"<<endl;
        }
        }

        cont++;
        temp=temp->siguiente;
    }
    for(int i=0;i<cont-1;i++){
        ofs<<"n_"<<i<<"->"<<"n_"<<i+1<<endl;
        ofs<<"n_"<<i+1<<"->"<<"n_"<<i<<endl;
    }

    ofs<<"}"<<endl;
    ofs.close();
    system("dot -Tsvg lista_doblemente_enlazada.dot -o lista_doble_tareas.svg");
    system("lista_doble_tareas.svg &");
}

lista_doble::~lista_doble()
{
    //dtor
}
