/*animacion de fractales 2*/
/*Fernando Galindo Soria*/

#include <graphics.h>
#include <math.h>
#include <bios.h>

int ind0,ind1,ind3;

void animac(void);
void perro(int,int,int,int,int);
void sonido(int);

void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");

  sonido(700);
  ind0=-72;  ind3=144;
  for (ind1=1;ind1<=360;ind1+=17)
    animac();

  sonido(800);
  for (ind0=-63;ind0<=-36;ind0+=9)
    animac();

  sonido(700);
  ind0=-27;  ind1=6;
  for (ind3=1;ind3<=380;ind3+=37)
    animac();

  sonido(900);
  ind0=7; ind3=346;  ind1=1;
    animac();

  getch();
  closegraph();
}

void animac()
{
   cleardevice();
   gotoxy(2,2);printf("continuo ind0=%d ind1=%d ind3=%d",ind0,ind1,ind3);
   perro(400,250,63,ind0,7);
   delay(500);
}

void perro(int x0,int y0,int l,int an,int ind)
{
  int x1,y1;
  if (bioskey(2)!=0x04)
  if (ind > 0)
  {
    setcolor(ind+1);
    x1=x0-(l*cos(an/57.29578));
    y1=y0-(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    perro(x1,y1,l/1.2,an+ind1,ind-1);
    perro(x1,y1,l/1.55,an+72,ind-1);
    perro(x1,y1,l/1.8,an+ind3,ind-1);
  }
}


void sonido(int son)
{
  sound(son);delay(700);
  nosound();
}

