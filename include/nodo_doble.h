#ifndef NODO_DOBLE_H
#define NODO_DOBLE_H
#include <iostream>

using namespace std;

class nodo_doble
{
    public:
        nodo_doble();
        virtual ~nodo_doble();
        string tarea;
        //Apuntadores
        nodo_doble *anterior;
        nodo_doble *siguiente;


    protected:

    private:
};

#endif // NODO_DOBLE_H
