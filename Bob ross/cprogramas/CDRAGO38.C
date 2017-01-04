/*fractal de dragon 19/x/96*/
/*modificado para manejar varios tipos de objetos: puntos,circulos,lineas
  y para encimar varios objetos  14/x11/97*/
/*Fernando Galindo Soria     Cd. de Mexico*/

#include <graphics.h>
#include <math.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <dos.h>
#include "tgrafica.fgs"

void caracol0(int,int,float,int);
void caracol(int,int,float,int);
int ang1,ang2,ang3,car,c1,c2,c3,c11,ran;
int br,bg,bb,ba,j,k,k1=0;
void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");

  randomize();
  while(car!=27){
    randomize();
    setbkcolor(0);
    br=random(10)+1;
    bg=random(44)+1;
    ba=random(9)+3;
    bb=random(64);
    ang1=7+random(360);
    ang2=3+random(360);
    ang3=-35+random(76);
/*    gotoxy(1,1);printf("fractal de dragon32 ang1=%d ang2=%d",ang1,ang2);
    gotoxy(1,2);printf("ang3=%d",ang3);    */
    c1=random(15)+1;
    c2=random(15)+1;
    c3=random(15)+1;
    ran=random(5);
    setcolor(c3);
    caracol0(250,250,30+random(22),0);
    if (kbhit())car=getch();
    else
     {
      while((random(30)!=2) && (kbhit()==0)){
      k=k+random(7)-2;
      for(j=1;j<16;j++){
	 escrcolordac16(16-j,br+(j+k)*3,bg+j+1+k,bb);
	 delay(10);}}}
      for(j=1;j<16;j++)
	escrcolordac16(16-j,br+(j+k)*3,bg+j+1+k,bb);
     if(random(24)==1) cleardevice();
  }
  closegraph();
}

void caracol0(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    caracol(x1,y1,l-1,an);
  }
}

void caracol(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/57.29578)*2.7);
    y1=y0+(l*sin(an/57.29578)*2.7);
    if(ran==0) putpixel(x0,y0,l*13);
    if(ran==1) putpixel(x0,y0,random(16)+1);
    if(ran==2) circle(x0,y0,.1);
    if(ran==3) putpixel(x1,y1,l*19);
    if(ran==4) {setcolor(0); line(x0,y0,x1,y1);}
    if(ran!=0) setcolor(c3+l*13);
    if(random(1000)==3)
    for(j=1;j<16;j++){
	escrcolordac16(16-j,l+(j+x1)*3,y1+j+1+x1,y0);
	if(random(3)==2)escrcolordac16(16-j,0,0,0);
	if(random(3)==0)escrcolordac16(16-j,random(64),random(64),random(64));
	delay(20);}
    caracol(x0,y0,l-.51,an+ang1);
    if(ran!=0) setcolor(c2-l*13);
    caracol0(x1,y1,l-10,an+ang2);
  }
}