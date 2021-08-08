#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    int op=0;
    while(op!=4){

        cout<<"\n\t---------------- Menu---------------------\n";
        cout<<"\t|\t1) Carga de Usuarios             |\n";
        cout<<"\t|\t2) Carga de Tareas               |\n";
        cout<<"\t|\t3) Ingreso Manual                |\n";
        cout<<"\t|\t4) Reportes                      |\n";
        cout<<"\t------------------------------------------\n";
        cout<<"\tIngrese una opcion: ";
        cin>>op;
        cout<<"\n"<<endl;

        if(op==1){
            string ruta="";
            string primer_linea;
            string carnet,dpi,nombre,carrera,pass,correo;
            int creditos,edad;

            cout<<"-------------Carga de Usuarios----------------"<<endl;
            cout<<"Ingrese ruta de archivo: ";
            cin>>ruta;

            fstream fs;
            fs.open(ruta,ios::in);
            getline(fs,primer_linea);

            if(!fs){
                cout<<"Error, no se encontro archivo CSV";
            }

        }
    }
}
