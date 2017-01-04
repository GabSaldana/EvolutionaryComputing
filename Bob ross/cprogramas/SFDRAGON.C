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
int ang1,ang2,car;
void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");
     caracol(350,150,39,0);
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
     caracol(x1,y1,l-15,an+47);
     caracol(x1,y1,l-10,an+127);
     caracol(x1,y1,l-1,an+12);
  }
}