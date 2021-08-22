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

        void insertar_tarea(int id,string mes,string dia,string carnet,string nombre,string desc,string materia,string fecha,string hora,string estado);

        void mostrar();

        void graficar_tarea();

        //Buscar tarea por medio de id
        nodo_doble *buscar_tarea(int id);

        //Eliminar tarea por id
        void eliminar_tarea(int id);

        //Modificar Tarea
        void modificar_tarea_carnet(int id,string carnet);
        void modificar_tarea_nombre(int id,string nombre);
        void modificar_tarea_desc(int id,string desc);
        void modificar_tarea_materia(int id,string materia);
        void modificar_tarea_fecha(int id,string fecha);
        void modificar_tarea_hora(int id,string hora);
        void modificar_tarea_estado(int id,string estado);

        //Busqueda en estructura linealizada
        nodo_doble *buscar_estructura(string mes,string dia,string hora);

        //Busqueda de posicion en estructura linealizada
        nodo_doble *buscar_posicion(string mes,string dia,string hora);

        string salida_tarea();

    protected:

    private:
};

#endif // LISTA_DOBLE_H
