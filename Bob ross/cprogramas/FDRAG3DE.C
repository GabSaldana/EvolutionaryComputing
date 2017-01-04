/*fractal de dragon 3d con manejo de paleta de colores 4/v/97*/
/*modificado el 14/vi/97 y el 15/vi/97*/
/*Fernando Galindo Soria*/

#include <graphics.h>
#include <math.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <dos.h>
#include "tgrafica.fgs"

void caracol0(int,int,float,int);
void caraco0(int,int,float,int);

void caracol1(int,int,float,int);
void caraco1(int,int,float,int);

void caracol2(int,int,float,int);
void caraco2(int,int,float,int);

void caracol3(int,int,float,int);
void caraco3(int,int,float,int);

void caracol4(int,int,float,int);

int ang1,ang2,ang3,car,c1,c2,c3,c11;
void main()
{
  int br,bg,bb,ba,j,tam=35,k,k1=0;
  int selecc;
  int gd=DETECT,gm,s=3,i=0;
  initgraph(&gd,&gm,"");

  randomize();
  setbkcolor(0);
  br=random(10)+1;
  bg=random(44)+1;
  ba=random(9)+3;
  bb=random(64);
  escrcolordac16(0,0,0,ba);
  for(j=1;j<16;j++)
     escrcolordac16(16-j,br+j*3,bg+j+1,bb);

  while(car!=27){
    ang1=7+random(360);
    ang2=3+random(360);
    ang3=-35+random(76);

    selecc=random(6);
    if(random(2)==1)s=-s;

    c1=random(15)+1;
    c2=random(15)+1;
    c3=random(15)+1;
    br=random(10)+1;
    bg=random(44)+1;
    bb=random(64);

    while((random(11)!=4) && (kbhit()==0)){
      tam=tam+random(3)-1;
      i++;
      c1+=3;
      c2+=4;
      c3--;
      setcolor(c3);
    if(selecc==0) caracol0(150+i*s,250-i,tam,0);

    if(selecc==1) caracol1(150+i*s,250-i,tam,0);

    if(selecc==2) caracol2(150+i*s,250-i,tam,0);

    if(selecc==3) caracol3(150+i*s,250-i,tam,0);

    if(selecc==4) caracol4(150+i*s,250-i,tam,0);

    if(selecc==5) caraco3(150+i*s,250-i,tam,0);

    if(selecc==0) caracol0(350+i*s,250-i,tam,0);

    if(selecc==1) caracol1(350+i*s,250-i,tam,0);

    if(selecc==2) caracol2(350+i*s,250-i,tam,0);

    if(selecc==3) caracol3(350+i*s,250-i,tam,0);

    if(selecc==4) caracol4(350+i*s,250-i,tam,0);

    if(selecc==5) caraco3(350+i*s,250-i,tam,0);

    for(j=1;j<16;j++)
       escrcolordac16(16-j,br+(j+k)*3,bg+j+1+k,bb);
    while((random(40)!=2) && (kbhit()==0)){
      escrcolordac16(0,k1/97,k1/197,ba-k1/297); k1++;
      k=k+random(7)-2;
      for(j=1;j<16;j++)
	 escrcolordac16(16-j,br+(j+k)*3,bg+j+1+k,bb);
	 delay(200);}
    }

    while((random(150)!=3) && (kbhit()==0)){
      escrcolordac16(0,k1/97,k1/197,ba-k1/297); k1++;
      k=k+random(7)-2;
      for(j=1;j<16;j++)
	escrcolordac16(16-j,br+(j+k)*3,bg+j+1+k,bb);
      delay(200);}

    if (kbhit())car=getch();
    i=0;
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
    caraco0(x1,y1,l-1,an);
    caraco0(x1,y1,l-7,an+ang1);
  }
}

void caraco0(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578)*1.7);
    y1=y0+(l*sin(an/57.29578)*1.7);
    line(x0,y0,x1,y1);
    setcolor(c1+l); caraco0(x0,y0,l-.81,an+ang1);
    setcolor(c2+l); caracol0(x1,y1,l-15,an+ang2);
    setcolor(c3+l); caracol0(x1,y1,l-7,an+ang3);
  }
}

void caracol1(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    caraco1(x1,y1,l-1,an);
  }
}

void caraco1(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578)*2.7);
    y1=y0+(l*sin(an/57.29578)*2.7);
    line(x0,y0,x1,y1);
    setcolor(c3+l); caraco1(x0,y0,l-.51,an+ang1);
    setcolor(c2+l); caracol1(x1,y1,l-10,an+ang2);
  }
}

void caracol2(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    caraco2(x1,y1,l-1,an);
  }
}

void caraco2(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578)*1.7);
    y1=y0+(l*sin(an/57.29578)*1.7);
    line(x0,y0,x1,y1);
    setcolor(c3+l); caraco2(x0,y0,l-.81,an+ang1);
    setcolor(c2+l); caracol2(x1,y1,l-15,an+ang2);
    setcolor(c1+l); caracol2(x1,y1,l-7,an+ang3);
  }
}

void caracol3(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    setcolor(c3+l); caraco3(x1,y1,l-15,an+ang1);
    setcolor(c2+l); caraco3(x1,y1,l-7,an+ang2);
    setcolor(c1+l); caraco3(x1,y1,l-1,an+ang3);
  }
}

void caracol4(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    caraco3(x1,y1,l-1,an+ang1);
  }
}

void caraco3(int x0,int y0,float l,int an)
{
  int x1,y1;
  if (!kbhit())
  if (l >=1 )               //47, 127, 12
  {
    x1=x0+(l*cos(an/57.29578));
    y1=y0+(l*sin(an/57.29578));
    line(x0,y0,x1,y1);
    setcolor(c3+c11+l); caraco3(x1,y1,l-15,an+ang1);
    setcolor(c2+c11+l); caraco3(x1,y1,l-7,an+ang2);
    setcolor(c1+c11+l); caraco3(x1,y1,l-1,an+ang3);
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
