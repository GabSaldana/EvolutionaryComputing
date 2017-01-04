/*paisaje marzo de 1995*/
/*Fernando Galindo Soria*/

#include <graphics.h>
#include <math.h>
#include <bios.h>

int w0,w1,w2,w3,color;

void dibuja(int,int,int,int,int);
void estrella(int,int,int,int,int);
void recta(int,int,int,int,int*,int*);

void main()
{
  int gd=DETECT,gm;
  registerbgidriver(EGAVGA_driver);
  initgraph(&gd,&gm,"");

/*estrella*/ color=3; w1=37;  estrella(450,90,1,27,47);

/*nube   */ color=2; w1=238; w2=273; w3=144;  dibuja(100,80,37,-72,9);

/*nube   */ color=2; w1=188; w2=243; w3=144;  dibuja(340,110,59,-72,9);

/*nube   */ color=2; w1=238; w2=273; w3=125;  dibuja(550,80,23,-23,7);

/*nube   */ color=2; w1=287; w2=103; w3=144;  dibuja(190,60,19,-92,9);

/*monta¤a*/ color=3; w1=6; w2=172; w3=186;  dibuja(425,350,63,173,7);

/*monta¤a*/ color=5; w1=6; w2=172; w3=1 ;  dibuja(210,320,63,169,7);

/*monta¤a*/ color=9; w1=6; w2=172; w3=186;  dibuja(280,325,63,-8,7);

/*monta¤a*/ color=6; w1=6; w2=172; w3=1 ;w0=172; dibuja(380,335,63,w0,7);

/*monta¤a*/ color=6; w1=6; w2=172; w3=1 ;w0=173; dibuja(380,335,63,w0,7);

/*arboles*/ color=1; w1=8; w2=72; w3=17;  dibuja(225,315,43,-17,7);

/*arboles*/ color=1; w1=-12; w2=352; w3=97;  dibuja(340,315,43,15,7);

/*arboles*/ color=1; w1=8; w2=72; w3=351;  dibuja(443,340,43,0,7);

  getch();
  closegraph();
}

void dibuja(int x0,int y0,int l,int an,int ind)
{
  int x1,y1;
  if (ind > 0)
  {
    setcolor(ind+color);
    recta(x0,y0,l,an,&x1,&y1);
    dibuja(x1,y1,l/1.2,an+w1,ind-1);
    dibuja(x1,y1,l/1.55,an+w2,ind-1);
    dibuja(x1,y1,l/1.8,an+w3,ind-1);
  }
}

void estrella(int x0,int y0,int l,int an,int ind)
{
  int x1,y1;
  if (bioskey(2)!=0x04)
  if (ind > 0)
  {
/*    setcolor(ind+color); */
    recta(x0,y0,l,an,&x1,&y1);
    estrella(x0,y0,l+1,an+w1,ind-1);
  }
}

void recta(int x0,int y0,int l,int an,int *x1,int *y1)
{
  *x1=x0-(l*cos(an/57.29578));
  *y1=y0-(l*sin(an/57.29578));
  line(x0,y0,*x1,*y1);
}