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

        //Funci�n que verifica que la cola no este vac�a
        int cola_vacia();

        //Metodo para encolar
        void encolar(int id,string tipo,string descripcion);

        //Metodo para desencolar
        void desencolar();

        //Metodo para graficar
        void graficar_cola();

    protected:

    private:
};

#endif // COLA_H
