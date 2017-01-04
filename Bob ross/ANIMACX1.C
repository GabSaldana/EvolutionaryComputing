/*perro*/
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

  ind0=-72;
  while(!kbhit()){
      for(ind3=1;ind3<360;ind3+=37)
	  for(ind1=1;ind1<=360;ind1+=57)animac();
  ind0+=9;
  }
  getch();

  closegraph();
}

void animac()
{
   cleardevice();
//   gotoxy(2,2);printf("continuo ind0=%d ind1=%d ind3=%d",ind0,ind1,ind3);
   perro(300,200,43,ind3,7);
   delay(200);
}

void perro(int x0,int y0,int l,int an,int ind)
{
  int x1,y1;
  if (!kbhit())
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

