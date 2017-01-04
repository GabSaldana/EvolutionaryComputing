/*dibuja*/
/*Fernando Galindo Soria*/

#include <graphics.h>
#include <math.h>
#include <bios.h>

int w0,w1,w2,w3,color,xi1,yi1;

void animac(int,int,int);
void animac1(int,int,int);
void dibuja(int,int,int,int,int);
void sonido(int);

void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");

  xi1=400; yi1=230; w2=72;

  sonido(700); w0=-72; w3=144; for (w1=1;w1<=360;w1+=23) animac(1,23,2);

  sonido(800); for (w0=-63;w0<=-36;w0+=9) animac(0,9,1);

  sonido(700); w0=7; w1=6; for (w3=1;w3<=380;w3+=27) animac(3,27,1);

  w2=172;

  sonido(700); w0=-72; w3=144; for (w1=1;w1<=360;w1+=23) animac(1,23,3);

  sonido(800); for (w0=-63;w0<=-36;w0+=9) animac(0,9,1);

  sonido(700); w0=-27; w1=6; for (w3=1;w3<=380;w3+=37) animac(3,37,5);

  sonido(900); w0=7; w1=1; w3=346; for (w2=1;w2<=380;w2+=37) animac(2,37,1);

  cleardevice(); sonido(900);
  yi1=320; xi1=220; w0=7; w1=6; w2=72; w3=345; animac1(1,1,1);
  yi1=300; xi1=250; w0=-27; w1=6; w2=172; w3=1; animac1(2,1,5);
  xi1=290; w0=-27; w1=6; w2=172; w3=1; animac1(2,1,5);
  xi1=340; w0=-27; w1=6; w2=172; w3=186; animac1(3,1,5);
  yi1=120; w0=-72; w1=188; w2=273; w3=144; animac1(4,1,2);

  getch();
  closegraph();
}

void animac(int nw,int salto,int col)
{
   cleardevice();
   gotoxy(2,2);
   printf("Continuo del angulo w%d con saltos de %d w0=%d w1=%d w2=%d w3=%d",
	   nw,salto,w0,w1,w2,w3);
   color=col;
   dibuja(xi1,yi1,63,w0,7);
   delay(500);
}

void animac1(int nw,int salto,int col)
{
   gotoxy(2,2);
   printf("Continuo del angulo w%d con saltos de %d w0=%d w1=%d w2=%d w3=%d",
	   nw,salto,w0,w1,w2,w3);
   color=col;
   dibuja(xi1,yi1,63,w0,7);
}


void dibuja(int x0,int y0,int l,int an,int ind)
{
  int x1,y1;
  if (bioskey(2)!=0x04)
  if (ind > 0)
  {
    setcolor(ind+color);
    x1=x0-(l*cos(an/57.29578));
    y1=y0-(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    dibuja(x1,y1,l/1.2,an+w1,ind-1);
    dibuja(x1,y1,l/1.55,an+w2,ind-1);
    dibuja(x1,y1,l/1.8,an+w3,ind-1);
  }
}


void sonido(int son)
{
  sound(son);delay(700);
  nosound();
}

