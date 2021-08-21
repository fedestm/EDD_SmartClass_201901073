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
        void insertar(string carnet,string dpi,string nombre,string carrera,string pass,int creditos,int edad,string correo);

        //Graficar Lista
        void graficar();

        //Mostrar Lista en Consola
        void mostrar();
        //Eliminar
        void eliminar_estudiante(string dpi);

        //Buscar Estudiante
        nodo_circular * buscar_estudiante(string dpi);

        //Buscar por carnet
        nodo_circular * buscar_carnet(string carnet);

        //Modificar por dpi
        void modificar_estudiante_carnet(string dpi,string carnet);
        void modificar_estudiante_nombre(string dpi,string nombre);
        void modificar_estudiante_carrera(string dpi,string carrera);
        void modificar_estudiante_pass(string dpi,string pass);
        void modificar_estudiante_creditos(string dpi,int creditos);
        void modificar_estudiante_edad(string dpi,int edad);
        void modificar_estudiante_correo(string dpi,string correo);


    protected:

    private:
};

#endif // LISTA_CIRCULAR_H
