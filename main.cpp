#include <iostream>

using namespace std;

int main()
{
    int op;
    while(op!=4){
        printf("-------------Menu------------------\n");
        printf("\t1) Carga de Usuarios\n");
        printf("\t2) Carga de Tareas\n");
        printf("\t3) Ingreso Manual\n");
        printf("\t4) Reportes\n\n");
        printf("Ingrese una opcion: ");
        cin>>op;
    }
    return 0;
}
