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
            string primer_linea;    //Cadena encargada de guardar primera linea
            string carnet,dpi,nombre,carrera,pass,correo;
            string creditos,edad;

            cout<<"-------------Carga de Usuarios----------------"<<endl;
            cout<<"Ingrese ruta de archivo: ";
            cin>>ruta;

            fstream fs;     //Se encarga de leer el archivo de entrada
            fs.open(ruta,ios::in);  //Abre el contenido
            getline(fs,primer_linea);   //Ignora la primera linea del archivo

            //cout<<primer_linea;

            if(!fs){    //Se verifica que el archivo exista
                cout<<"Error, no se encontro archivo CSV";
            }else{
                while(true)
                {   
                    //Finaliza al terminar de leer el archivo
                    if(fs.eof()){
                        break;
                    }
                    //Se separan los datos por medio comas 
                    //Las variables asignadas almacenan los datos separados por columnas
                    getline(fs,carnet,',');
                    getline(fs,dpi,',');
                    getline(fs,nombre,',');
                    getline(fs,carrera,',');
                    getline(fs,pass,',');
                    getline(fs,creditos,',');
                    getline(fs,edad,',');
                    getline(fs,correo,'\n');
                }
            }
                
        }
    }
}

