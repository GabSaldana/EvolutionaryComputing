/*fractal de dragon 19/x/96*/
/*Fernando Galindo Soria*/

#include <graphics.h>
#include <math.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <dos.h>

void caracol0(int,int,float,int);
void caracol1(int,int,float,int);
void caracol(int,int,float,int);
int ang1,ang2,ang3,car,c1,c2,c3,c11;
void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");

  randomize();
  while(car!=27){
    ang1=-30-random(330);
    ang2=30+random(330);
    ang3=random(360);
    gotoxy(1,1);printf("fractal de dragon34 ang1=%d ang2=%d",ang1,ang2);
    gotoxy(1,2);printf("ang3=%d",ang3);
    c1=random(15)+1;
    c2=random(15)+1;
    c3=random(15)+1;
    setcolor(c3);
    caracol0(350,400,35,-90);
    if (kbhit())car=getch();
    else delay(2000);
    cleardevice();
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
    caracol(x1,y1,l/5.3,an-ang1);
    caracol1(x1,y1,l/1.3,an);
    caracol(x1,y1,l/5.3,an+ang1);
  }
}

void caracol(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578)*3);
    y1=y0+(l*sin(an/57.29578)*3);
    //line(x0,y0,x1,y1);
    setcolor(c3); caracol(x1,y1,l/1.3,an);
    setcolor(c2); caracol1(x1,y1,l/1.3,an-ang2);
    setcolor(c1); caracol1(x1,y1,l/1.3,an+ang2);
  }
}
void caracol1(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578)*3);
    y1=y0+(l*sin(an/57.29578)*3);
    line(x0,y0,x1,y1);
    setcolor(c3); caracol1(x1,y1,l/1.3,an);
    setcolor(c2); caracol0(x1,y1,l/1.3,an-ang3);
    setcolor(c1); caracol0(x1,y1,l/1.3,an+ang3);
  }
}