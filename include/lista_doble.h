#ifndef LISTA_DOBLE_H
#define LISTA_DOBLE_H
#include "nodo_doble.h"


class lista_doble
{
    public:
        lista_doble();
        virtual ~lista_doble();

        //Apuntadores
        nodo_doble *primero;
        nodo_doble *ultimo;  

    protected:

    private:
};

#endif // LISTA_DOBLE_H
