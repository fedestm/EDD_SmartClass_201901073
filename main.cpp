#include <iostream>
#include <string>
#include <fstream>
#include <regex>
#include "include/lista_circular.h"
#include "include/lista_doble.h"

using namespace std;

int main()
{
    lista_circular *lista=new lista_circular();
    lista_doble *l_doble=new lista_doble();
    int op=0;
    string matriz[5][9][32];
    string carnet_tarea,nombre_tarea,desc_tarea,materia_tarea,fecha_tarea,estado_tarea,hora_tarea;

    while(true){

        cout<<"\n\t---------------- Menu---------------------\n";
        cout<<"\t|\t1) Carga de Usuarios             |\n";
        cout<<"\t|\t2) Carga de Tareas               |\n";
        cout<<"\t|\t3) Ingreso Manual                |\n";
        cout<<"\t|\t4) Reportes                      |\n";
        cout<<"\t|\t5) Salir                         |\n";
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
            //cin>>ruta;

            fstream fs;     //Se encarga de leer el archivo de entrada
            fs.open("C:/Users/User/Documents/GitHub/EDD_SmartClass_201901073/Estudiantes.csv",ios::in);  //Abre el contenido
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
                            /*
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
                            */
                            lista->insertar(carnet,dpi,nombre,carrera,pass,stoi(creditos),stoi(edad),correo);

                        }
                    }
                }
                cout<<"Se insertaron correctamente los estudiantes"<<endl;
            }
        }
        else if(op==2){
            string ruta_tarea="";
            string linea;
            string datos;
            string mes,dia,hora,carnet,nombre,desc,materia,fecha,estado;

            cout<<"-------------Carga de Tareas----------------"<<endl;
            //cout<<"Ingrese ruta de archivo: ";
            //cin>>ruta_tarea;

            fstream fs;
            fs.open("C:/Users/User/Documents/GitHub/EDD_SmartClass_201901073/Tareas.csv",ios::in);
            getline(fs,linea);

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

                    /*
                    cout<<"*********************************"<<endl;
                    cout<<"Mes: "<<mes<<endl;
                    cout<<"Dia: "<<dia<<endl;
                    cout<<"Hora: "<<hora<<endl;
                    cout<<"Carnet: "<<carnet<<endl;
                    cout<<"Nombre: "<<nombre<<endl;
                    cout<<"Descripcion: "<<desc<<endl;
                    cout<<"Materia: "<<materia<<endl;
                    cout<<"Fecha: "<<fecha<<endl;
                    cout<<"Estado: "<<estado<<endl;
                    cout<<"**********************************\n"<<endl;
                    */
                    //Se recorre la matriz y se insertan los valores
                    datos=carnet+","+nombre+","+desc+","+materia+","+fecha+","+hora+","+estado;
                    for(int i=0;i<5;i++){
                        for(int j=0;j<9;j++){
                            for(int k=0;k<32;k++){
                                //Se insertan los datos correspondientes a su indice
                                //Se ignoran los valores nulos
                                matriz[stoi(mes)-7][stoi(hora)-8][stoi(dia)-1]=datos;
                                
                                cout<<"Insertando tareas...\n";
                            }
                        }
                    }
                }
                cout<<"Se insertaron las tareas en la matriz estatica"<<endl;

            }
        }
        else if(op==3){

        }

        else if(op==4){
            cout<<"\n****************************Reportes*****************************"<<endl;
            int opcion=0;
            while(opcion!=4){
                cout<<"\t1) Lista Usuarios\n";
                cout<<"\t2) Linealización de Tareas\n";
                cout<<"\t3) Reporte Linealización\n";
                cout<<"\t4) Regresar\n";
                cout<<"\tIngrese una opción: ";
                cin>>opcion;
                cout<<"\n";
                if(opcion==1){
                    lista->graficar();
                }else if(opcion==2){
                    int cont=0;
                    for(int i=0;i<(sizeof(matriz[0][0])/sizeof(*matriz[0][0]));i++){
                        for(int j=0;j<(sizeof(matriz[0])/sizeof(*matriz[0]));j++){
                            for(int k=0;k<(sizeof(matriz)/sizeof(*matriz));k++){
                                //cout<<"Linealizando....\n";
                                cont++;
                                cout<<matriz[k][j][i]<<endl;
                                if(matriz[k][j][i]==""){
                                    l_doble->insertar_tarea("","","","-1","","","");
                                }else{
                                    //l_doble->insertar_tarea(matriz[k][j][i]);
                                    istringstream is(matriz[k][j][i]);
                                    while(true){
                                        if(is.eof()){
                                            break;
                                        }
                                        getline(is,carnet_tarea,',');
                                        getline(is,nombre_tarea,',');
                                        getline(is,desc_tarea,',');
                                        getline(is,materia_tarea,',');
                                        getline(is,fecha_tarea,',');
                                        getline(is,hora_tarea,',');
                                        getline(is,estado_tarea,'\n');
                                        l_doble->insertar_tarea(carnet_tarea,nombre_tarea,desc_tarea,materia_tarea,fecha_tarea,hora_tarea,estado_tarea);
                                    }

                                }

                            }
                        }
                    }
                }else if(opcion==3){
                    l_doble->graficar_tarea();
                }
            }

        }else if(op==5){
            cout<<"Saliendo..."<<endl;
            exit(-1);
        }
        else{
            cout<<"\nOpcion invalida"<<endl;
        }
    }
}
