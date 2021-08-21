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
        int cont;

        void insertar_tarea(int id,string carnet,string nombre,string desc,string materia,string fecha,string hora,string estado);

        void mostrar();

        void graficar_tarea();

        //Buscar tarea por medio de id
        nodo_doble *buscar_tarea(int id);

        //Eliminar tarea por id
        void eliminar_tarea(int id);

        //Modificar Tarea
        void modificar_tarea(int id,string carnet,string nombre,string desc,string materia,string fecha,string hora,string estado);

    protected:

    private:
};

#endif // LISTA_DOBLE_H
