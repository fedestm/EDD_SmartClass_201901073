#ifndef NODO_COLA_H
#define NODO_COLA_H
#include <iostream>

using namespace std;

class nodo_cola
{
    public:
        nodo_cola();
        virtual ~nodo_cola();
        //Apuntador siguiente
        nodo_cola *siguiente;
        int id;
        string tipo,descripcion;

        nodo_cola(nodo_cola *siguiente,int id,string tipo,string descripion);


    protected:

    private:
};

#endif // NODO_COLA_H
