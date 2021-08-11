#ifndef LISTA_CIRCULAR_H
#define LISTA_CIRCULAR_H
#include "nodo_circular.h"

class lista_circular
{
    public:
        lista_circular();
        virtual ~lista_circular();

        //Apuntadores Primero y Ultimo
        nodo_circular *primero;
        nodo_circular *ultimo;

    protected:

    private:
};

#endif // LISTA_CIRCULAR_H
