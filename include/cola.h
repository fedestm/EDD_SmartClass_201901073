#ifndef COLA_H
#define COLA_H
#include "nodo_cola.h"

class cola
{
    public:
        cola();
        virtual ~cola();
        nodo_cola *primero;
        nodo_cola *ultimo;
        int cont;

        //Función que verifica que la cola no este vacía
        int cola_vacia();

        //Metodo para encolar
        void encolar(int id,string tipo,string descripcion);

        //Metodo para desencolar
        void desencolar();

        //Metodo para graficar
        void graficar_colar();

    protected:

    private:
};

#endif // COLA_H
