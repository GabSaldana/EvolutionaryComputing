/*fractal de dragon 19/x/96*/
/*Fernando Galindo Soria*/

#include <graphics.h>
#include <math.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <dos.h>

void caracol(int,int,float,int);
void caracoli(int,int,float,int);
int ang1,ang2,car;
void main()
{
  int gd=DETECT,gm,x0,y0,ang0;
  initgraph(&gd,&gm,"");
    randomize();
    while(!kbhit()){
	ang0=random(360);
	x0=200+random(200);
	y0=100+random(200);
	gotoxy(10,1);printf("x0=%d y0=%d ang0=%d",x0,y0,ang0);
	setcolor(1);
	caracol(x0,y0,43,-ang0);
	caracoli(x0,500-y0,43,ang0);
	delay(2000);cleardevice();}
  getch();
  closegraph();
}

void caracol(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    setcolor(3); caracol(x1,y1,l-15,an+47);
    setcolor(2); caracol(x1,y1,l-10,an+127);
    setcolor(1); caracol(x1,y1,l-1,an+12);
  }
}
void caracoli(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    setcolor(3); caracoli(x1,y1,l-15,an-47);
    setcolor(2); caracoli(x1,y1,l-10,an-127);
    setcolor(1); caracoli(x1,y1,l-1,an-12);
  }
}