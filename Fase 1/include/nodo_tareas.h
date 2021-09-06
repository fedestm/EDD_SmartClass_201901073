#ifndef NODO_TAREAS_H
#define NODO_TAREAS_H
#include <iostream>
using namespace std;

class nodo_tareas
{
    public:
        nodo_tareas();
        virtual ~nodo_tareas();
        int id;
        string carnet,nombre,descripcion,materia,fecha,hora,estado,mes,dia;
        //Apuntadores
        nodo_tareas *anterior;
        nodo_tareas *siguiente;

    protected:

    private:
};

#endif // NODO_TAREAS_H
