/*perro*/
/*Fernando Galindo Soria*/

#include <graphics.h>
#include <math.h>
#include <bios.h>

void perro(int,int,int,int,int);

void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");
  perro(300,150,63,-72,9);
  getch();
  closegraph();
}

void perro(int x0,int y0,int l,int an,int ind)
{
  int x1,y1;
  if (bioskey(2)!=0x04)
  if (ind > 0)
  {
    x1=x0-(l*cos(an/57.29578));
    y1=y0-(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    perro(x1,y1,l/1.2,an+51,ind-1);
    perro(x1,y1,l/1.55,an+72,ind-1);
    perro(x1,y1,l/1.8,an+144,ind-1);
  }
}
