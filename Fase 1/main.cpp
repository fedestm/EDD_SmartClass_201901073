#include <iostream>
#include <string>
#include <fstream>
#include <regex>
#include "include/lista_circular.h"
#include "include/lista_doble.h"
#include "include/cola.h"
#include "include/lista_salida_tareas.h"

using namespace std;

int main()
{
    lista_circular *lista=new lista_circular();
    lista_doble *l_doble=new lista_doble();
    lista_salida_tareas *l_tareas=new lista_salida_tareas();
    cola *col=new cola();
    int op=0;
    string matriz[5][9][32];
    string mes_tarea,dia_tarea,carnet_tarea,nombre_tarea,desc_tarea,materia_tarea,fecha_tarea,estado_tarea,hora_tarea;

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
                    if(int(carnet.length())==9){
                        if(int(dpi.length())==13){
                            if(regex_match(correo,regex("([a-zA-Z]+)([_.a-zA-Z_0-9]*)([a-zA-Z_0-9]+)(@)([a-zA-Z]+)([.a-zA-Z]+)(.org|.com|.es)"))){
                                lista->insertar(carnet,dpi,nombre,carrera,pass,creditos,edad,correo);

                            }else{
                                col->encolar(0,"Estudiante","Carnet: "+carnet+"\nError en correo");
                    }
                        }else{
                        col->encolar(0,"Estudiante","Carnet: "+carnet+"\nError en el rango de dpi");
                    }
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
*/                   }else{
                        col->encolar(0,"Estudiante","Carnet: "+carnet+"\nError en rango de carnet");
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
            cout<<"Ingrese ruta de archivo: ";
            cin>>ruta_tarea;

            fstream fs;
            fs.open(ruta_tarea,ios::in);
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
                    if(lista->buscar_carnet(carnet)){
                        //Se recorre la matriz y se insertan los valores
                        datos=mes+","+dia+","+carnet+","+nombre+","+desc+","+materia+","+fecha+","+hora+","+estado;
                        for(int i=0;i<5;i++){
                            for(int j=0;j<9;j++){
                                for(int k=0;k<32;k++){
                                    //Se insertan los datos correspondientes a su indice
                                    //Se ignoran los valores nulos
                                    matriz[stoi(mes)-7][stoi(hora)-8][stoi(dia)-1]=datos;

                                    //cout<<"Insertando tareas...\n";
                                }
                            }
                        }

                    }else{
                        col->encolar(0,"Tarea","Carnet: "+carnet+"\n no encontrado");
                    }

                    }

                cout<<"Se insertaron las tareas en la matriz estatica"<<endl;

            }
        }
        else if(op==3){
            int op=0;
            while(op!=3){
                cout<<"1) Usuarios\n";
                cout<<"2) Tareas\n";
                cout<<"3) Regresar\n";
                cout<<"Ingrese opción: ";
                cin>>op;

                if(op==1){
                    while(op!=4){
                        string carnet,dpi,nombre,carrera,pass,correo,creditos,edad;
                        cout<<"1) Ingresar\n";
                        cout<<"2) Modificar\n";
                        cout<<"3) Eliminar\n";
                        cout<<"4) Salir\n";
                        cout<<"\n\nIngrese opción: ";
                        cin>>op;
                        if(op==1){
                            cout<<"-----Ingreso de estudiantes manualmente-----"<<endl;
                            cout<<"Ingrese carnet: ";
                            cin>>carnet;
                            cout<<"Ingrese dpi: ";
                            cin>>dpi;
                            cout<<"Ingrese nombre: ";
                            cin.ignore();
                            getline(cin,nombre);
                            cout<<"Ingrese carrera: ";
                            getline(cin,carrera);
                            cout<<"Ingrese contraseña: ";
                            cin>>pass;
                            cout<<"Ingrese creditos: ";
                            cin>>creditos;
                            cout<<"Ingrese edad: ";
                            cin>>edad;
                            cout<<"Ingrese correo: ";
                            cin>>correo;
                            lista->insertar(carnet,dpi,nombre,carrera,pass,creditos,edad,correo);
                            cout<<"\nSe inserto estudiante"<<endl;
                        }else if(op==2){
                            cout<<"\n-----Modificar estudiante-----"<<endl;
                            cout<<"Ingrese dpi: ";
                            cin>>dpi;
                            cout<<"\n";

                            while(op!=8){
                                cout<<"\n1) Carnet\n";
                                cout<<"2) Nombre\n";
                                cout<<"3) Carrera\n";
                                cout<<"4) Contraseña\n";
                                cout<<"5) Creditos\n";
                                cout<<"6) Edad\n";
                                cout<<"7) Correo\n";
                                cout<<"8) No deseo modificar\n";
                                cout<<"Ingrese una opcion: ";
                                cin>>op;
                                cout<<"\n"<<endl;

                                    if(op==1){
                                        cout<<"Ingrese carnet: ";
                                        cin>>carnet;
                                        lista->modificar_estudiante_carnet(dpi,carnet);
                                    }else if(op==2){
                                        cout<<"Ingrese nombre: ";
                                        cin.ignore();
                                        getline(cin,nombre);
                                        lista->modificar_estudiante_nombre(dpi,nombre);
                                    }else if(op==3){
                                        cout<<"Ingrese carrera: ";
                                        getline(cin,carrera);
                                        lista->modificar_estudiante_carrera(dpi,carrera);
                                    }else if(op==4){
                                        cout<<"Ingrese contraseña: ";
                                        cin>>pass;
                                        lista->modificar_estudiante_pass(dpi,pass);
                                    }else if(op==5){
                                        cout<<"Ingrese creditos: ";
                                        cin>>creditos;
                                        lista->modificar_estudiante_creditos(dpi,creditos);
                                    }else if(op==6){
                                        cout<<"Ingrese edad: ";
                                        cin>>edad;
                                        lista->modificar_estudiante_edad(dpi,edad);
                                    }else if(op==7){
                                        cout<<"Ingrese correo: ";
                                        cin>>correo;
                                        lista->modificar_estudiante_correo(dpi,correo);
                                    }
                                }

                        }else if(op==3){
                            cout<<"\n-----Eliminar estudiante------"<<endl;
                            cout<<"Ingrese DPI: ";
                            cin.ignore();
                            getline(cin,dpi);
                            if(lista->buscar_estudiante(dpi)){
                                lista->eliminar_estudiante(dpi);
                                cout<<"Se elimino estudiante"<<endl;
                            }
                        }
                    }

                }else if(op==2){
                    while(op!=4){
                        cout<<"1) Ingresar\n";
                        cout<<"2) Modificar\n";
                        cout<<"3) Eliminar\n";
                        cout<<"4) Salir\n";
                        cout<<"Ingrese opción: ";
                        cin>>op;
                        if(op==1){
                            cout<<"\n------Ingreso de tareas manualmente----------"<<endl;

                        string mes,dia,hora,carnet,nombre,descripcion,materia,fecha,estado;
                        cout<<"\nIngrese mes: ";
                        cin>>mes;
                        cout<<"\nIngrese dia: ";
                        cin>>dia;
                        cout<<"\nIngrese hora: ";
                        cin>>hora;
                        cout<<"\nIngrese carnet: ";
                        cin>>carnet;
                        cout<<"\nIngrese nombre: ";
                        cin.ignore();
                        getline(cin,nombre);
                        cout<<"\nIngrese descripcion: ";
                        getline(cin,descripcion);
                        cout<<"\nIngrese materia: ";
                        getline(cin,materia);
                        cout<<"\nFecha: ";
                        cin>>fecha;
                        cout<<"\nEstado: ";
                        cin>>estado;

                        if(lista->buscar_carnet(carnet)){
                        //Se recorre la matriz y se insertan los valores
                        string datos_manual=mes+","+dia+","+carnet+","+nombre+","+descripcion+","+materia+","+fecha+","+hora+","+estado;
                        for(int i=0;i<5;i++){
                            for(int j=0;j<9;j++){
                                for(int k=0;k<32;k++){
                                    //Se insertan los datos correspondientes a su indice
                                    //Se ignoran los valores nulos
                                    matriz[stoi(mes)-7][stoi(hora)-8][stoi(dia)-1]=datos_manual;

                                    //cout<<"Insertando tareas...\n";
                                }
                            }
                        }

                    }else{
                        col->encolar(0,"Tarea","Carnet: "+carnet+"\n no encontrado");
                    }
                        }else if(op==2){
                            int id;
                            string carnet,nombre,desc,materia,fecha,hora,estado;
                            cout<<"\n------Modificar tarea------"<<endl;
                            cout<<"Ingrese id a buscar: ";
                            cin>>id;
                            if(l_doble->buscar_tarea(id)){
                                while(op!=8){
                                    cout<<"1) Carnet\n";
                                    cout<<"2) Nombre\n";
                                    cout<<"3) Descripcon\n";
                                    cout<<"4) Materia\n";
                                    cout<<"5) Fecha\n";
                                    cout<<"6) Hora\n";
                                    cout<<"7) Estado\n";
                                    cout<<"8) No deseo modificar\n";
                                    cout<<"Ingrese una opcion: ";
                                    cin>>op;
                                    cout<<"\n";
                                    if(op==1){
                                        cout<<"Ingrese carnet: ";
                                        cin>>carnet;
                                        l_doble->modificar_tarea_carnet(id,carnet);
                                        cout<<"\nSe modifico carnet"<<endl;
                                    }else if(op==2){
                                        cout<<"Ingrese nombre: ";
                                        cin.ignore();
                                        getline(cin,nombre);
                                        l_doble->modificar_tarea_nombre(id,nombre);
                                        cout<<"\nSe modifico el nombre"<<endl;
                                    }else if(op==3){
                                        cout<<"Ingrese descripcion: ";
                                        cin.ignore();
                                        getline(cin,desc);
                                        l_doble->modificar_tarea_desc(id,desc);
                                        cout<<"\nSe modifico la descripcion"<<endl;
                                    }else if(op==4){
                                        cout<<"Ingrese materia: ";
                                        cin.ignore();
                                        getline(cin,materia);
                                        l_doble->modificar_tarea_materia(id,materia);
                                        cout<<"\nSe modifico materia"<<endl;
                                    }else if(op==5){
                                        cout<<"Ingrese fecha: ";
                                        cin>>fecha;
                                        l_doble->modificar_tarea_fecha(id,fecha);
                                        cout<<"\nSe modifico fecha"<<endl;
                                    }else if(op==6){
                                        cout<<"Ingrese hora: ";
                                        cin>>hora;
                                        l_doble->modificar_tarea_hora(id,hora);
                                        cout<<"\nSe modifico hora"<<endl;
                                    }else if(op==7){
                                        cout<<"Ingrese estado: ";
                                        cin>>estado;
                                        l_doble->modificar_tarea_estado(id,estado);
                                        cout<<"\nSe modifico estado"<<endl;
                                    }
                                }
                            }else{
                                cout<<"No se encontro la tarea"<<endl;
                            }
                        }else if(op==3){
                            int id;
                            cout<<"\n------Eliminar tarea--------"<<endl;
                            cout<<"Ingrese id a eliminar: ";
                            cin>>id;
                            l_doble->eliminar_tarea(id);
                            cout<<"Se elimino tarea"<<endl;
                        }
                    }

                }
            }

        }

        else if(op==4){
            cout<<"\n****************************Reportes*****************************"<<endl;
            int opcion=0;
            while(opcion!=8){
                cout<<"\t1) Lista de estudiantes\n";
                cout<<"\t2) Linealización de Tareas\n";
                cout<<"\t3) Reporte Linealización\n";
                cout<<"\t4) Busqueda de estructura linealizada\n";
                cout<<"\t5) Busqueda de posicion en lista linelizada\n";
                cout<<"\t6) Reporte de Errores\n";
                cout<<"\t7) Codigo generado de Salida\n";
                cout<<"\t8) Regresar\n";
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
                                    l_doble->insertar_tarea(0,"","","","","-1","","","","");
                                }else{
                                    //l_doble->insertar_tarea(matriz[k][j][i]);
                                    istringstream is(matriz[k][j][i]);
                                    while(true){
                                        if(is.eof()){
                                            break;
                                        }
                                        getline(is,mes_tarea,',');
                                        getline(is,dia_tarea,',');
                                        getline(is,carnet_tarea,',');
                                        getline(is,nombre_tarea,',');
                                        getline(is,desc_tarea,',');
                                        getline(is,materia_tarea,',');
                                        getline(is,fecha_tarea,',');
                                        getline(is,hora_tarea,',');
                                        getline(is,estado_tarea,'\n');
                                        l_doble->insertar_tarea(0,mes_tarea,dia_tarea,carnet_tarea,nombre_tarea,desc_tarea,materia_tarea,fecha_tarea,hora_tarea,estado_tarea);
                                        l_tareas->insertar_tarea(0,mes_tarea,dia_tarea,carnet_tarea,nombre_tarea,desc_tarea,materia_tarea,fecha_tarea,hora_tarea,estado_tarea);
                                    }

                                }

                            }
                        }
                    }
                }else if(opcion==3){
                    l_doble->graficar_tarea();
                }else if(opcion==4){
                    cout<<"\n-------------------Busqueda de Estructura Linealizada------------"<<endl;
                    string mes,dia,hora;
                    cout<<"Ingrese mes: ";
                    cin>>mes;
                    cout<<"\nIngrese dia: ";
                    cin>>dia;
                    cout<<"\nIngrese hora: ";
                    cin>>hora;
                    l_doble->buscar_estructura(mes,dia,hora);
                    cout<<"\n"<<endl;

                }else if(opcion==5){
                    cout<<"\n-------------------Busqueda de Posicion en Estructura Linealizada------------"<<endl;
                    string mes,dia,hora;
                    cout<<"Ingrese mes: ";
                    cin>>mes;
                    cout<<"\nIngrese dia: ";
                    cin>>dia;
                    cout<<"\nIngrese hora: ";
                    cin>>hora;
                    l_doble->buscar_posicion(mes,dia,hora);
                    cout<<"\n"<<endl;

                }else if(opcion==6){
                    col->graficar_cola();
                }else if(opcion==7){
                    cout<<"\n---------------------Codigo de Salida------------------------------"<<endl;
                    ofstream ofs("Estudiantes.txt");
                    ofs<<"¿Elements?"<<endl;
                    ofs<<lista->salida_estudiantes();
                    ofs<<l_tareas->salida_tarea()<<endl;
                    ofs<<"¿$Elements?"<<endl;
                    ofs.close();
                    cout<<"Se genero archivo de salida\n"<<endl;
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
