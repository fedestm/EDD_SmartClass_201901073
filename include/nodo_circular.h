#ifndef NODO_CIRCULAR_H
#define NODO_CIRCULAR_H
#include <iostream>
using namespace std;

class nodo_circular
{
    public:
        nodo_circular();
        virtual ~nodo_circular();
        string carnet,dpi,nombre,carrera,pass;
        int creditos,edad;

        //Apuntadores de nodos
        //nodo-><-nodo-><-nodo
        nodo_circular *siguiente;
        nodo_circular *anterior;

    protected:

    private:
};

#endif // NODO_CIRCULAR_H
