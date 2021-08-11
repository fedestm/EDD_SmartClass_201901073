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

        //Metodos para insertar datos en nodo
        //---Lista Circular Doble--------
        void insertar(string carnet,string dpi,string nombre,string carrera,string pass,int creditos,int edad);

        //Graficar Lista
        void graficar();

        //Mostrar Lista en Consola
        void mostrar();


    protected:

    private:
};

#endif // LISTA_CIRCULAR_H
