#ifndef LISTA_SALIDA_TAREAS_H
#define LISTA_SALIDA_TAREAS_H
#include "nodo_tareas.h"

class lista_salida_tareas
{
    public:
        lista_salida_tareas();
        virtual ~lista_salida_tareas();
        nodo_tareas *primero;
        nodo_tareas *ultimo;
        int cont;

        void insertar_tarea(int id,string mes,string dia,string carnet,string nombre,string desc,string materia,string fecha,string hora,string estado);
        string salida_tarea();
    protected:

    private:
};

#endif // LISTA_SALIDA_TAREAS_H
