#include "cola.h"
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
    nodo_cola *nuevo=new nodo_cola(nullptr,cont+1,tipo,descripcion);
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

        int cont_cola=0;
        temp=this->primero;
        while(temp!=nullptr){
            //Mostrar el primer nodo
            if(temp==this->primero){
                fs<<"\tn_"<<cont_cola<<"[label=\"Id: "<<temp->id<<"\\nTipo: "<<temp->tipo<<
                "\\nDescripción: "<<temp->descripcion<<"\",shape=box,color=\"#F1350C\",fontcolor=white];\n"<<endl;
            }else if(temp==this->ultimo){   //Mostrar el ultimo nodo
                fs<<"\tn_"<<cont_cola<<"[label=\"Id: "<<temp->id<<"\\nTipo: "<<temp->tipo<<
                "\\nDescripción: "<<temp->descripcion<<"\",shape=box,color=\"#F1350C\",fontcolor=white];\n"<<endl;
            }else{  //Mostrar los nodos que estan en medio
                fs<<"\tn_"<<cont_cola<<"[label=\"Id: "<<temp->id<<"\\nTipo: "<<temp->tipo<<
                "\\nDescripción: "<<temp->descripcion<<"\",shape=box,color=\"#F1350C\",fontcolor=white];\n"<<endl;
            }
            temp=temp->siguiente;
            cont_cola++;
        }

        for(int i=0;i<cont_cola-1;i++){
            fs<<"n_"<<i<<"->"<<"n_"<<i+1<<endl;
        }

        fs<<"\t}\n"<<endl;
        fs.close();

        system("dot -Tpng cola.dot -o cola_errores.png");
        system("cola_errores.png &");
    }
}

cola::~cola()
{
    //dtor
}
