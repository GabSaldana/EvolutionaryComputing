/*Lanzador de pantallas 31/i/98
  se autoriza la distribucion y uso libre de este sistema (freeware)
  Fernando Galindo Soria   Cd. de Mexico*/

#include <graphics.h>
#include <stdlib.h>
#include <time.h>
#include <dos.h>
#include <conio.h>
#include <stdio.h>

void mensaje(void);

char ic,indice[]={'0','1','2','3','4','5','6','7','8','9'
		   ,'q','w','e','r','t','y','u','i','o','p'};
char lista[][14]={"este mensaje","farbol.exe","farbol1.exe","farbol2.exe"
		  ,"farbol3.exe","farbol4.exe","farbol5.exe","carbol.exe"
		  ,"carbol5.exe","cdrago31","cdrago32","cdrago38.exe"
		  ,"fdrag3d1.exe","fdrag3d2.exe","fdrag3d3.exe","fdrago31.exe"
		  ,"paisajes.exe","spiro1.exe","flores.exe","curvas.exe"};
void main()
{
  int i;
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");
  cleardevice();
  randomize();
  i=indice[random(20)];
  while(ic!=27){
   gotoxy(1,1);printf("**para salir del lanzador de pantalla oprime <ESC> dos veces");
   gotoxy(1,3);printf(" para auxilio oprime 0");
   gotoxy(1,5);printf(" para cambiar de funcion oprime letra o numero de los dos primeros renglones");
   gotoxy(1,6);printf("  sino la maquina seleccionara en forma aleatoria");
   delay(1000);
   if (kbhit())ic=getch(); else ic=indice[random(20)];
   if(ic!=27){
     i=0;
     while( i<20 && ic!=indice[i])i++;
     if(i>=20)i=random(20);
     gotoxy(1,8);printf(" Siguiente funcion:\n ic=%c %s",ic,lista[i]);
     delay(500); }

   if(i==0) mensaje(); else system(lista[i]);
 }
  closegraph();
}

void mensaje()
 { int i=0;
   cleardevice();
   gotoxy(5,1); printf("Lanzador de  P a  n t a l l a s");
   gotoxy(10,2); printf("by fractalstic");
   gotoxy(15,3); printf("Mexican Curious Technology");
   gotoxy(2,5); printf("Fernando Galindo Soria     Cd. de Mexico, Enero de 1998");
   gotoxy(2,7); printf("Se autoriza la distribucion y uso libre de este sistema (freeware)");
   gotoxy(1,9);printf("Lista de funciones \n");
   i=0;
   while(i<20){printf(" %c %s\n",indice[i],lista[i]);i++;}
   printf("para continuar oprime una tecla"); getch();
   cleardevice();
 }
