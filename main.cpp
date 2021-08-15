#include <iostream>
#include <string>
#include <fstream>
#include <regex>
#include "include/lista_circular.h"

using namespace std;

int main()
{
    lista_circular *lista=new lista_circular();
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

                    //Se compara la cantidad de digitos de carnet y dpi
                    //Carnet: 9 digitos
                    //DPI: 13 digitos
                    if(int(carnet.length())==9 && int(dpi.length()==13)){
                        if(regex_match(correo,regex("([a-z]+)([_.a-z_0-9])([a-z_0-9]+)(@)([a-z]+)(.org|.com|.es)"))){
                            cout<<"*********************************"<<endl;
                            cout<<"Carnet: "<<carnet<<endl;
                            cout<<"DPI: "<<dpi<<endl;
                            cout<<"Nombre: "<<nombre<<endl;
                            cout<<"Carrera: "<<carrera<<endl;
                            cout<<"Password: "<<pass<<endl;
                            cout<<"Creditos: "<<creditos<<endl;
                            cout<<"Edad: "<<edad<<endl;
                            cout<<"Correo: "<<correo<<endl;
                            cout<<"**********************************\n"<<endl;
                            lista->insertar(carnet,dpi,nombre,carrera,pass,stoi(creditos),stoi(edad),correo);
                            lista->graficar();
                        }
                    }
                }
            }
        }
        else if(op==2){
            string ruta_tarea="";
            string linea;
            string mes,dia,hora,carnet,nombre,desc,materia,fecha,estado;

            cout<<"-------------Carga de Tareas----------------"<<endl;
            cout<<"Ingrese ruta de archivo: ";
            cin>>ruta_tarea;

            fstream fs;
            fs.open(ruta_tarea,ios::in);
            getline(fs,linea);


            //Matriz Estatica
            string matriz[5][9][32];

            if(!fs){
                cout<<"Error, no se encontro archivo CSV";

            }else{
                while(true){
                    if(fs.eof()){
                        break;
                    }
                    getline(fs,mes,',');
                    getline(fs,dia,',');
                    getline(fs,hora,',');
                    getline(fs,carnet,',');
                    getline(fs,nombre,',');
                    getline(fs,desc,',');
                    getline(fs,materia,',');
                    getline(fs,fecha,',');
                    getline(fs,estado,'\n');
                }
            }

        }




    }
}
