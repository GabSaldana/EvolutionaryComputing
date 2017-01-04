/*fractal de dragon 3d con manejo de paleta de colores 4/v/97
 modificado de fdrag3db (suma fracciones a los colores) 20/ix/97*/
/*Fernando Galindo Soria*/

#include <graphics.h>
#include <math.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <dos.h>
#include "tgrafica.fgs"

void caracol0(int,int,float,int,int);
void caraco0(int,int,float,int,int);

void caracol1(int,int,float,int,int);
void caraco1(int,int,float,int,int);

void caracol2(int,int,float,int,int);
void caraco2(int,int,float,int,int);

void caracol3(int,int,float,int,int);
void caraco3(int,int,float,int,int);

void caracol4(int,int,float,int,int);
int ang0,ang1,ang2,ang3,car,c1,c2,c3,c11,tam,capa,iz;
void main()
{
  int br,bg,bb,j,i=0;
  int selecc;
  int gd=DETECT,gm,s=3;
  initgraph(&gd,&gm,"");

  randomize();
  setbkcolor(0);
  while(car!=27){
    ang0=random(360);
    ang1=7+random(360);
    ang2=3+random(360);
    ang3=-35+random(76);
    selecc=random(6);
    gotoxy(1,1);printf("fractal de dragon%d ang0=%d ang1=%d ang2=%d ang3=%d"
			,selecc,ang0,ang1,ang2,ang3);
    if(random(2)==1)s=-s;
    c1=1;
    c2=1;
    c3=15;
    br=random(10)+1;
    bg=random(44)+1;
    bb=random(64);
    escrcolordac16(0,0,0,5);
    tam=40; capa=25;
    while((iz++)<capa){
      gotoxy(1,3);printf("tam=%d z=%d",tam,capa-iz);
      for(j=1;j<16;j++)
       escrcolordac16(16-j,br,bg,bb+j*3+iz*16/capa);
      c1+=.36;
      c2+=.47;
      c3-=.37;
      setcolor(c3);
    if(selecc==0) caracol0(350+iz*s,250-iz,tam,ang0,0);

    if(selecc==1) caracol1(350+iz*s,250-iz,tam,ang0,0);

    if(selecc==2) caracol2(350+iz*s,250-iz,tam,ang0,0);

    if(selecc==3) {tam=35; caracol3(350+iz*s,250-iz,tam,ang0,0);}

    if(selecc==4) {tam=35; caracol4(350+iz*s,250-iz,tam,ang0,0);}

    if(selecc==5) {tam=35; caraco3(350+iz*s,250-iz,tam,ang0,0);}
    }
    if (kbhit())car=getch();
    else {delay(4000);
      i=0;
      while((random(2000)!=3) && (kbhit()==0)){
	for(j=1;j<16;j++){
	   escrcolordac16(16-j,br+j*3-i/96,bg+j+1-i/64,bb+i/32);
	   delay(1);}
	i++;
      } }
    iz=0;
    cleardevice();
  }
  closegraph();
}

void caracol0(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    caraco0(x1,y1,l-1,an,nivel+1);
    caraco0(x1,y1,l-7,an+ang1,nivel+1);
  }
}

void caraco0(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578)*1.7);
    y1=y0+(l*sin(an/57.29578)*1.7);
    if(iz>nivel)moveto(x1,y1); else line(x0,y0,x1,y1);
    setcolor(c1); caraco0(x0,y0,l-.81,an+ang1,nivel+1);
    setcolor(c2); caracol0(x1,y1,l-15,an+ang2,nivel+1);
    setcolor(c3); caracol0(x1,y1,l-7,an+ang3,nivel+1);
  }
}

void caracol1(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    caraco1(x1,y1,l-1,an,nivel+1);
  }
}

void caraco1(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578)*2.7);
    y1=y0+(l*sin(an/57.29578)*2.7);
    if(iz*l/capa>l)moveto(x1,y1); else line(x0,y0,x1,y1);
    setcolor(c3); caraco1(x0,y0,l-.51,an+ang1,nivel+1);
    setcolor(c2); caracol1(x1,y1,l-10,an+ang2,nivel+1);
  }
}

void caracol2(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    caraco2(x1,y1,l-1,an,nivel+1);
  }
}

void caraco2(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578)*1.7);
    y1=y0+(l*sin(an/57.29578)*1.7);
    if(iz*l/capa>l)moveto(x1,y1); else line(x0,y0,x1,y1);
    setcolor(c3); caraco2(x0,y0,l-.81,an+ang1,nivel+1);
    setcolor(c2); caracol2(x1,y1,l-15,an+ang2,nivel+1);
    setcolor(c1); caracol2(x1,y1,l-7,an+ang3,nivel+1);
  }
}

void caracol3(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    if(iz*l/capa>l)moveto(x1,y1); else line(x0,y0,x1,y1);
    setcolor(c3); caraco3(x1,y1,l-15,an+ang1,nivel+1);
    setcolor(c2); caraco3(x1,y1,l-7,an+ang2,nivel+1);
    setcolor(c1); caraco3(x1,y1,l-1,an+ang3,nivel+1);
  }
}

void caracol4(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    caraco3(x1,y1,l-1,an+ang1,nivel+1);
  }
}

void caraco3(int x0,int y0,float l,int an,int nivel)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    if(iz*l/capa>l)moveto(x1,y1); else line(x0,y0,x1,y1);
    setcolor(c3+c11); caraco3(x1,y1,l-15,an+ang1,nivel+1);
    setcolor(c2+c11); caraco3(x1,y1,l-7,an+ang2,nivel+1);
    setcolor(c1+c11); caraco3(x1,y1,l-1,an+ang3,nivel+1);
  }
}


/*
void caracol(int,int,float,int);

float angbx=1.,angby=1.;
void main()
{
int x0=200,y0=200,l0=20,ang0=1,incx=0,incy=0,borra=1;
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");
  randomize();

  angbx=1.;
  angby=1.;
  setcolor(random(15)+1);
  while (!kbhit())
  {
    angbx+=incx;
    angby+=incy;
    if(random(20)==3)
    { x0=100+random(200);y0=100+random(100);l0=20+random(10);ang0=1+random(10);}
    if(random(5)==1)
    { angbx=random(1000)+1;angby=random(1000)+1;setcolor(random(15)+1);
      incx=random(10);incy=random(10); if(random(5)==2)borra*=-1;}
//    gotoxy(8,1);printf("%f",angbx); gotoxy(29,1);printf("%f",angby);
    caracol(x0,y0,l0,ang0);
    if((random(30)==2) || (borra==1))cleardevice();
  }
  getch();
  closegraph();
}

void caracol(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/angbx));   //57.29578
    y1=y0+(l*sin(an/angby));
    line(x0,y0,x1,y1);
    caracol(x1,y1,l-.1,an+35);
  }
}

void caracol(int,int,float,int);
int ang1,ang2,car,c1,c2,angbx;
void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");

  randomize();
  while(car!=27){
    ang2=random(360);
    ang1=ang2+random(146)+17;
    gotoxy(1,1);printf("fractal de dragon ang1=%d ang2=%d",ang1,ang2);
    c1=random(15)+1;
    c2=random(16);
    setcolor(c1);
    caracol(290,140,60,91);
    if (kbhit())car=getch();
    else delay(2000);
    cleardevice();
  }

  closegraph();
}

void caracol(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    setcolor(c1); caracol(x1,y1,l-15,an+ang1);     //127, 117, 47
    setcolor(c2); caracol(x1,y1,l-1,an+ang2);     //12, 22
  }


void caracol(int,int,float,int);
int ang1,ang2,car;
void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");


    setcolor(1);
    caracol(250,150,45,0);

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

void caracol(int,int,float,int);
void caracol1(int,int,float,int);
int ang1,ang2,car;
void main()
{
  int gd=DETECT,gm;
  initgraph(&gd,&gm,"");

    setcolor(1); caracol(560,200,50,90);
    setcolor(1); caracol1(180,390,50,270);

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
    setcolor(3); caracol(x1,y1,l-12,an+47);
    setcolor(1); caracol(x1,y1,l-1,an+12);
  }
}

void caracol1(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    setcolor(3); caracol(x1,y1,l-12,an-47);
    setcolor(1); caracol(x1,y1,l-1,an-12);
  }
}       */
