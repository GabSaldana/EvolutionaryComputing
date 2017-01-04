from Tkinter import *
import math

#******************************** REFERENCE **************************************
#S->e*S*   S->eSS arboles de dos ramas ,S dibuja troncos o ramas S->eSSSS.......
#S->e*S*   S->eS estrellas  e(x0,y0,long,w)  S(x0,y0,long,w+w1) 
#S->e*S*   S->eS caracoles necesitan que le punto inicialx,y sea igualal final

#**********************************************************************************
def arbol_tupido(w,x0,y0,l,an,color):#S() x,y,alto,angulo entre as grande mas espacio entre ramas
    ind=1;    
    if (l > ind ):  
        
        coseno = math.cos(an/57.29578)#coseno de el angulo
        seno = math.sin(an/57.29578)#seno de el angulo
        x1=x0-(l*coseno);
        y1=y0-(l*seno);
        t1=l/1.5
        w.create_line(x0,y0,x1,y1,fill=color)#e() 
        arbol_tupido(w,x1,y1,t1,an-47,color);
        arbol_tupido(w,x1,y1,t1,an+0,color);
        arbol_tupido(w,x1,y1,t1,an+47,color);
  
    return


def arbol_seco(w,x0,y0,l,an,color):#S() x,y,tamano,angulo
    ind=1;    
    if (l > ind ):  
        
        coseno = math.cos(an/57.29578)#coseno de el angulo
        seno = math.sin(an/57.29578)#seno de el angulo
        x1=x0-(l*coseno);
        y1=y0-(l*seno);
  
        t1=l/1.7
        w.create_line(x0,y0,x1,y1,fill=color)#e() 
        arbol_seco(w,x1,y1,t1,an-15,color);
        arbol_seco(w,x1,y1,t1,an+0,color);
        arbol_seco(w,x1,y1,t1,an+15,color);
  
    return

def arbol_pino(w,x0,y0,l,an,color):#S() x,y,tamano,angulo
    ind=1;    
    if (l > ind ):  
        
        coseno = math.cos(an/57.29578)#coseno de el angulo
        seno = math.sin(an/57.29578)#seno de el angulo
        x1=x0-(l*coseno);
        y1=y0-(l*seno);
  
        t1=l/1.55
        w.create_line(x0,y0,x1,y1,fill=color)#e() 
        arbol_pino(w,x1,y1,t1,an-135,color);
        arbol_pino(w,x1,y1,t1,an+0,color);
        arbol_pino(w,x1,y1,t1,an+135,color);
  
    return


def arbusto(w,x0,y0,l,an,color):#S() x,y,alto,angulo
    ind=1;    
    if (l > ind ):  
        
        coseno = math.cos(an/57.29578)#coseno de el angulo
        seno = math.sin(an/57.29578)#seno de el angulo
        x1=x0-(l*coseno);
        y1=y0-(l*seno);
        t1=l/1.3
        w.create_line(x0,y0,x1,y1,fill=color)#e() 
        arbusto(w,x1,y1,t1,an-67,color);
        arbusto(w,x1,y1,t1,an-0,color);
        arbusto(w,x1,y1,t1,an+67,color);
  
    return


def nube_bolitas(w,x0,y0,l,an,ind,color):#S() x,y,alto,angulo
       
    if ind > 0 :
        coseno = math.cos(an/57.29578)#coseno de el angulo
        seno = math.sin(an/57.29578)#seno de el angulo
        x1=x0-(l*coseno);
        y1=y0-(l*seno);
        t1=l/2
        t2=l/1.7
        t3=l/1.5
        w.create_line(x0,y0,x1,y1,fill=color)#e() 
        nube_bolitas(w,x0,y0,t1,an +40,ind-1,color)
        nube_bolitas(w,x1,y1,t2,an + 60, ind-1,color)
        nube_bolitas(w,x1,y1,t3,an + 80, ind-1,color)
    return


def nube_amplia(w,x0,y0,l,an,ind,color):#S() x,y,alto,angulo
       
    if ind > 0 :
        coseno = math.cos(an/57.29578)#coseno de el angulo
        seno = math.sin(an/57.29578)#seno de el angulo
        x1=x0-(l*coseno);
        y1=y0-(l*seno);
        t1=l/1.7
        t2=l/1.7
        t3=l/1.5
        w.create_line(x0,y0,x1,y1,fill=color)#e() 
        nube_amplia(w,x0,y0,t1,an +30,ind-1,color)
        nube_amplia(w,x1,y1,t2,an + 50, ind-1,color)
        nube_amplia(w,x1,y1,t3,an + 100, ind-1,color)
    return

def river(w,x0,y0,l,an,ind,color):

    if ind >0:
        coseno = math.cos(an/57.29578)#coseno de el angulo
        seno = math.sin(an/57.29578)#seno de el angulo
        x1=x0-(l*coseno);
        y1=y0-(l*seno);
        t1=l/1.2
        t2=l/2.0
        t3=l/1.1
        w.create_line(x0,y0,x1,y1,fill=color)#e() 
        river(w,x1,y1,t1,an + 10,ind-1,color)
        river(w,x1,y1,t2,an + 172, ind-1,color)
        river(w,x1,y1,t3,an + 180, ind-1,color)
    return

def montana(w,x0,y0,l,an,ind,color):

    if ind >0:
        coseno = math.cos(an/57.29578)#coseno de el angulo
        seno = math.sin(an/57.29578)#seno de el angulo
        x1=x0-(l*coseno);
        y1=y0-(l*seno);
        t1=l/1.2
        t2=l/2.0
        t3=l/1.1
        w.create_line(x0,y0,x1,y1,fill=color)#e() 
        montana(w,x1,y1,t1,an + 10,ind-1,color)
        montana(w,x1,y1,t2,an + 172, ind-1,color)
        montana(w,x1,y1,t3,an + 180, ind-1,color)
    return

#********************************  GRAPHICS ************************************
master = Tk()
xmax=1000
ymax=1000
w = Canvas(master, width=xmax, height=ymax)
w.configure(background='#FFCCBC')
w.pack()

#************************************* SKY *********************************************
nube_amplia(w,0,0,300,180,10,'#E3F2FD')#x0 y0 tamano angulo volumen
nube_amplia(w,0,0,250,145,10,'#F5F5F5')#x0 y0 tamano angulo volumen
nube_amplia(w,0,50,200,180,10,'#F5F5F5')#x0 y0 tamano angulo volumen
nube_amplia(w,800,100,200,180,10,'#E3F2FD')#x0 y0 tamano angulo volumen
nube_amplia(w,700,0,300,180,10,'#F5F5F5')#x0 y0 tamano angulo volumen
nube_amplia(w,500,0,200,180,10,'#E3F2FD')#x0 y0 tamano angulo volumen
nube_amplia(w,300,0,270,180,10,'#F5F5F5')#x0 y0 tamano angulo volumen
nube_amplia(w,0,0,200,180,10,'#FFFFFF')#x0 y0 tamano angulo volumen
nube_amplia(w,800,0,200,180,10,'#FFFFFF')#x0 y0 tamano angulo volumen
nube_bolitas(w,600,100,100,270,9,'#FFFFFF')#x0 y0 tamano angulo volumen
nube_bolitas(w,800,260,50,360,9,'#FFFFFF')#x0 y0 tamano angulo volumen
nube_bolitas(w,800,200,50,15,9,'#FFFFFF')#x0 y0 tamano angulo volumen
nube_bolitas(w,1000,130,100,30,9,'#FFFFFF')#x0 y0 tamano angulo volumen
nube_bolitas(w,280,100,100,180,9,'#FFFFFF')#x0 y0 tamano angulo volumen
nube_bolitas(w,260,100,100,80,9,'#FFFFFF')#x0 y0 tamano angulo volumen

#*************************** RIVER *******************************************
river(w,580,580,100,-31,9,'#80CBC4')
river(w,600,580,100,-31,9,'#80CBC4')
river(w,600,580,100,-31,8,'#00695C')
river(w,600,580,100,-31,9,'#E0F2F1')
river(w,600,580,100,-31,8,'#00695C')
river(w,620,580,100,-31,9,'#80CBC4')

#****************************MOUNTAIN*******************************************+
montana(w,800,450,80,131,6,'#757575')
montana(w,800,460,80,141,6,'#757575')
montana(w,800,480,80,161,6,'#757575')
montana(w,1000,450,40,1,6,'#9E9E9E')
montana(w,1000,440,40,1,6,'#757575')
montana(w,1000,430,40,1,6,'#9E9E9E')

montana(w,1000,410,40,1,6,'#9E9E9E')
montana(w,1030,400,40,1,6,'#757575')
montana(w,1030,370,40,1,6,'#757575')
montana(w,1030,360,40,1,6,'#757575')

montana(w,174,430,10,31,6,'#9E9E9E')
montana(w,199,460,10,31,6,'#9E9E9E')
montana(w,216,490,10,31,6,'#9E9E9E')
montana(w,317,370,10,31,6,'#9E9E9E')
montana(w,154,430,10,31,6,'#9E9E9E')
montana(w,279,560,10,31,6,'#9E9E9E')
montana(w,386,390,10,31,6,'#9E9E9E')
montana(w,247,470,10,31,6,'#9E9E9E')

montana(w,405,490,50,21,6,'#9E9E9E')
montana(w,510,430,10,31,6,'#757575')
montana(w,520,480,50,21,6,'#9E9E9E')
montana(w,500,430,10,31,6,'#757575')
montana(w,540,470,60,21,6,'#9E9E9E')
montana(w,515,430,10,31,6,'#757575')
montana(w,560,460,50,21,6,'#9E9E9E')
montana(w,580,490,80,21,6,'#9E9E9E')
montana(w,100,430,60,131,6,'#757575')
montana(w,110,430,60,131,6,'#9E9E9E')
montana(w,120,450,20,131,6,'#757575')
montana(w,125,430,60,131,6,'#9E9E9E')
montana(w,130,480,50,131,6,'#757575')
montana(w,135,430,60,131,6,'#9E9E9E')
montana(w,140,500,60,131,6,'#757575')
montana(w,160,430,60,131,6,'#757575')
montana(w,180,460,60,131,6,'#757575')
montana(w,320,580,40,21,6,'#9E9E9E')
montana(w,340,570,60,21,6,'#9E9E9E')
montana(w,360,560,30,21,6,'#9E9E9E')
montana(w,200,490,60,131,6,'#757575')
montana(w,390,530,30,131,6,'#757575')
montana(w,480,560,30,131,6,'#757575')
montana(w,450,590,30,131,6,'#757575')
montana(w,440,500,10,11,6,'#757575')
montana(w,460,530,10,11,6,'#757575')
montana(w,480,560,10,11,6,'#757575')

montana(w,300,370,10,131,6,'#757575')
montana(w,340,500,10,11,6,'#757575')
montana(w,360,430,10,11,6,'#757575')
montana(w,380,460,10,11,6,'#757575')
montana(w,300,490,10,11,6,'#757575')
montana(w,400,370,10,11,6,'#757575')

#***********************************   ARBOLES **************************************

arbol_tupido(w,100,500,5,90,'#4CAF50')
arbol_tupido(w,100,490,5,90,'#4CAF50')
arbol_tupido(w,100,480,5,90,'#4CAF50')
arbol_tupido(w,101,490,5,90,'#4CAF50')
arbol_tupido(w,102,480,5,90,'#4CAF50')
arbol_pino(w,101,498,5,90,'#004D40')
arbol_pino(w,102,496,5,90,'#212121')
arbol_pino(w,100,470,5,90,'#212121')
arbol_pino(w,100,450,5,90,'#212121')
arbol_pino(w,100,430,5,90,'#212121')
arbol_pino(w,102,500,5,90,'#004D40')
arbol_pino(w,110,490,5,90,'#004D40')
arbol_tupido(w,105,480,5,90,'#4CAF50')
arbol_tupido(w,109,470,5,90,'#4CAF50')
arbol_tupido(w,111,450,5,90,'#4CAF50')
arbol_tupido(w,117,430,5,90,'#4CAF50')

arbol_tupido(w,118,390,5,90,'#4CAF50')
arbol_tupido(w,120,380,5,90,'#4CAF50')
arbol_tupido(w,123,390,5,90,'#4CAF50')
arbol_tupido(w,128,380,5,90,'#4CAF50')
arbol_pino(w,125,398,5,90,'#004D40')
arbol_pino(w,140,396,5,90,'#004D40')
arbol_pino(w,158,490,5,90,'#004D40')
arbol_pino(w,150,380,5,90,'#004D40')
arbol_pino(w,163,390,5,90,'#004D40')
arbol_tupido(w,168,380,5,90,'#4CAF50')
arbol_tupido(w,175,498,5,90,'#4CAF50')
arbol_tupido(w,180,496,5,90,'#4CAF50')
arbol_tupido(w,191,510,5,90,'#4CAF50')
arbol_tupido(w,218,390,5,90,'#4CAF50')
arbol_tupido(w,220,380,5,90,'#4CAF50')
arbol_tupido(w,223,390,5,90,'#4CAF50')
arbol_pino(w,228,380,5,90,'#004D40')
arbol_tupido(w,225,398,5,90,'#4CAF50')
arbol_tupido(w,240,396,5,90,'#4CAF50')
arbol_tupido(w,258,490,5,90,'#4CAF50')
arbol_tupido(w,250,380,5,90,'#212121')
arbol_tupido(w,263,390,5,90,'#212121')
arbol_tupido(w,268,380,5,90,'#212121')
arbol_tupido(w,275,498,5,90,'#4CAF50')
arbol_tupido(w,280,496,5,90,'#4CAF50')
arbol_tupido(w,291,510,5,90,'#4CAF50')
arbol_pino(w,240,500,5,90,'#004D40')
arbol_pino(w,258,590,5,90,'#004D40')
arbol_pino(w,250,680,5,90,'#004D40')
arbol_pino(w,263,590,5,90,'#004D40')
arbol_pino(w,268,580,5,90,'#004D40')
arbol_tupido(w,275,598,5,90,'#4CAF50')
arbol_tupido(w,280,596,5,90,'#212121')
arbol_tupido(w,291,610,5,90,'#212121')
arbol_tupido(w,310,600,5,90,'#212121')
arbol_tupido(w,318,620,5,90,'#212121')
arbol_tupido(w,320,621,5,90,'#212121')
arbol_tupido(w,323,609,5,90,'#4CAF50')
arbol_tupido(w,358,390,5,90,'#4CAF50')
arbol_tupido(w,350,380,5,90,'#4CAF50')
arbol_tupido(w,363,390,5,90,'#4CAF50')
arbol_pino(w,368,380,5,90,'#004D40')
arbol_tupido(w,375,398,5,90,'#4CAF50')
arbol_tupido(w,380,396,5,90,'#4CAF50')
arbol_tupido(w,410,400,5,90,'#4CAF50')
arbol_tupido(w,418,420,5,90,'#4CAF50')
arbol_tupido(w,420,421,5,90,'#4CAF50')
arbol_tupido(w,423,409,5,90,'#4CAF50')
arbol_tupido(w,440,400,5,90,'#4CAF50')
arbol_tupido(w,458,490,5,90,'#4CAF50')
arbol_tupido(w,450,480,5,90,'#4CAF50')
arbol_tupido(w,463,490,5,90,'#4CAF50')
arbol_pino(w,468,480,5,90,'#004D40')
arbol_pino(w,475,498,5,90,'#004D40')
arbol_pino(w,480,496,5,90,'#004D40')
arbol_pino(w,491,410,5,90,'#004D40')
arbol_pino(w,348,505,5,90,'#004D40')
arbol_pino(w,355,515,5,90,'#004D40')
arbol_tupido(w,320,524,5,90,'#4CAF50')
arbol_tupido(w,361,530,5,90,'#4CAF50')
arbol_tupido(w,310,566,5,90,'#4CAF50')
arbol_tupido(w,320,520,5,90,'#4CAF50')
arbol_tupido(w,368,570,5,90,'#4CAF50')
arbol_tupido(w,350,582,5,90,'#4CAF50')
arbol_tupido(w,363,494,5,90,'#4CAF50')
arbol_pino(w,368,487,5,90,'#004D40')
arbol_tupido(w,375,498,5,90,'#4CAF50')
arbol_tupido(w,380,496,5,90,'#4CAF50')
arbol_tupido(w,391,412,5,90,'#4CAF50')

arbol_pino(w,301,451,5,90,'#004D40')
arbol_pino(w,305,455,5,90,'#004D40')
arbol_pino(w,309,456,5,90,'#212121')
arbol_pino(w,310,458,5,90,'#212121')
arbol_pino(w,313,460,5,90,'#212121')
arbol_pino(w,321,459,5,90,'#212121')
arbol_pino(w,325,462,5,90,'#004D40')
arbol_pino(w,330,452,5,90,'#004D40')
arbol_pino(w,341,432,5,90,'#004D40')
arbol_pino(w,346,434,5,90,'#004D40')
arbol_pino(w,354,436,5,90,'#004D40')
arbol_pino(w,358,438,5,90,'#004D40')

arbol_tupido(w,110,500,5,90,'#4CAF50')
arbol_tupido(w,118,490,5,90,'#4CAF50')
arbol_pino(w,120,480,5,90,'#004D40')
arbol_tupido(w,123,490,5,90,'#4CAF50')
arbol_tupido(w,128,480,5,90,'#4CAF50')
arbol_tupido(w,125,498,5,90,'#4CAF50')
arbol_tupido(w,140,496,5,90,'#212121')
arbol_tupido(w,140,500,5,90,'#212121')
arbol_tupido(w,158,490,5,90,'#212121')
arbol_tupido(w,150,480,5,90,'#212121')
arbol_tupido(w,163,490,5,90,'#212121')
arbol_tupido(w,168,480,5,90,'#4CAF50')
arbol_tupido(w,175,498,5,90,'#4CAF50')
arbol_tupido(w,180,496,5,90,'#4CAF50')
arbol_tupido(w,191,510,5,90,'#4CAF50')
arbol_tupido(w,210,500,5,90,'#4CAF50')
arbol_tupido(w,218,520,5,90,'#4CAF50')
arbol_pino(w,220,521,5,90,'#004D40')
arbol_pino(w,223,509,5,90,'#004D40')
arbol_pino(w,228,505,5,90,'#004D40')
arbol_pino(w,225,515,5,90,'#004D40')
arbol_pino(w,230,524,5,90,'#004D40')
arbol_pino(w,231,470,5,90,'#004D40')
arbol_pino(w,240,496,5,90,'#004D40')
arbol_tupido(w,240,500,5,90,'#4CAF50')
arbol_tupido(w,258,490,5,90,'#4CAF50')
arbol_tupido(w,250,480,5,90,'#4CAF50')
arbol_tupido(w,263,490,5,90,'#4CAF50')
arbol_tupido(w,268,480,5,90,'#4CAF50')
arbol_tupido(w,275,498,5,90,'#4CAF50')
arbol_tupido(w,280,496,5,90,'#4CAF50')
arbol_tupido(w,291,510,5,90,'#4CAF50')
arbol_pino(w,310,500,5,90,'#004D40')
arbol_pino(w,318,520,5,90,'#004D40')
arbol_pino(w,320,521,5,90,'#004D40')
arbol_pino(w,323,509,5,90,'#004D40')
arbol_pino(w,340,496,5,90,'#004D40')
arbol_pino(w,340,500,5,90,'#004D40')
arbol_tupido(w,358,490,5,90,'#4CAF50')
arbol_tupido(w,350,480,5,90,'#4CAF50')
arbol_tupido(w,363,490,5,90,'#4CAF50')
arbol_tupido(w,368,480,5,90,'#4CAF50')
arbol_tupido(w,375,498,5,90,'#4CAF50')
arbol_tupido(w,380,496,5,90,'#4CAF50')
arbol_tupido(w,391,510,5,90,'#4CAF50')
arbol_tupido(w,410,500,5,90,'#4CAF50')
arbol_tupido(w,418,520,5,90,'#4CAF50')
arbol_tupido(w,420,521,5,90,'#4CAF50')
arbol_tupido(w,423,509,5,90,'#4CAF50')

arbol_tupido(w,103,509,10,90,'#4CAF50')
arbol_tupido(w,300,429,10,90,'#4CAF50')
arbol_tupido(w,425,480,10,90,'#4CAF50')
arbol_tupido(w,103,609,11,90,'#4CAF50')
arbol_tupido(w,110,580,12,90,'#4CAF50')
arbol_pino(w,208,409,10,90,'#004D40')
arbol_pino(w,307,329,10,90,'#004D40')
arbol_pino(w,429,580,10,90,'#004D40')
arbol_pino(w,110,609,11,90,'#004D40')
arbol_pino(w,215,580,12,90,'#004D40')

arbol_pino(w,500,580,10,90,'#212121')
arbol_pino(w,501,580,5,90,'#212121')
arbol_pino(w,505,580,5,90,'#212121')
arbol_pino(w,509,580,5,90,'#004d40')
arbol_pino(w,510,580,10,90,'#004d40')
arbol_pino(w,516,580,5,90,'#004d40')
arbol_pino(w,513,540,5,90,'#004d40')
arbol_pino(w,524,500,5,90,'#004d40')
arbol_pino(w,535,550,5,90,'#004d40')
arbol_pino(w,528,505,5,90,'#004d40')
arbol_pino(w,530,524,5,90,'#212121')
arbol_pino(w,520,532,5,90,'#004d40')
arbol_pino(w,522,540,10,90,'#212121')

arbol_pino(w,533,540,10,90,'#212121')
arbol_pino(w,544,560,10,90,'#004d40')
arbol_pino(w,538,570,5,90,'#004D40')
arbol_pino(w,548,544,5,90,'#004D40')
arbol_pino(w,550,561,5,90,'#004D40')
arbol_pino(w,547,537,5,90,'#004D40')
arbol_pino(w,552,530,10,90,'#212121')

arbol_pino(w,607,560,10,90,'#212121')
arbol_pino(w,602,530,10,90,'#004d40')
arbol_pino(w,610,605,10,90,'#000000')
arbol_pino(w,347,610,10,90,'#212121')
arbol_pino(w,352,630,10,90,'#004d40')
arbol_pino(w,346,613,10,90,'#212121')
arbol_pino(w,356,608,10,90,'#000000')

arbol_pino(w,400,620,10,90,'#004d40')
arbol_pino(w,405,630,10,90,'#004d40')
arbol_pino(w,410,605,10,90,'#000000')
arbol_pino(w,427,610,10,90,'#212121')
arbol_pino(w,432,625,10,90,'#004d40')
arbol_pino(w,440,614,10,90,'#212121')
arbol_pino(w,453,606,10,90,'#004d40')


arbol_pino(w,300,620,10,90,'#004D40')
arbol_pino(w,305,630,10,90,'#004D40')
arbol_pino(w,310,605,10,90,'#000000')
arbol_pino(w,327,610,10,90,'#004D40')
arbol_pino(w,332,625,10,90,'#004D40')
arbol_pino(w,340,614,10,90,'#004D40')
arbol_pino(w,353,606,10,90,'#004d40')

arbol_pino(w,200,620,10,90,'#004D40')
arbol_pino(w,205,630,10,90,'#004D40')
arbol_pino(w,210,605,10,90,'#212121')
arbol_pino(w,227,610,10,90,'#004D40')
arbol_pino(w,232,625,10,90,'#004d40')
arbol_pino(w,240,614,10,90,'#004D40')
arbol_pino(w,253,606,10,90,'#212121')

arbol_pino(w,100,620,10,90,'#004D40')
arbol_pino(w,105,630,10,90,'#004D40')
arbol_pino(w,110,605,10,90,'#212121')
arbol_pino(w,127,610,10,90,'#004D40')
arbol_pino(w,132,625,10,90,'#004d40')
arbol_pino(w,140,614,10,90,'#004D40')
arbol_pino(w,153,606,10,90,'#212121')
arbol_pino(w,100,520,10,90,'#004D40')
arbol_pino(w,105,530,10,90,'#004D40')
arbol_pino(w,110,535,10,90,'#212121')
arbol_pino(w,127,540,10,90,'#004D40')
arbol_pino(w,132,545,10,90,'#004d40')
arbol_pino(w,140,550,10,90,'#004D40')
arbol_pino(w,153,553,10,90,'#212121')
arbol_pino(w,100,560,10,90,'#004D40')
arbol_pino(w,135,566,10,90,'#004D40')
arbol_pino(w,140,579,10,90,'#212121')
arbol_pino(w,147,680,10,90,'#004D40')
arbol_pino(w,152,673,10,90,'#004d40')
arbol_pino(w,150,685,10,90,'#004D40')
arbol_pino(w,160,690,10,90,'#212121')

arbol_pino(w,95,566,10,90,'#004D40')
arbol_pino(w,80,579,10,90,'#212121')
arbol_pino(w,77,680,10,90,'#004D40')
arbol_pino(w,62,673,10,90,'#004d40')
arbol_pino(w,50,685,10,90,'#004D40')
arbol_pino(w,58,690,10,90,'#212121')
arbol_pino(w,95,666,10,90,'#004D40')
arbol_pino(w,80,679,10,90,'#212121')
arbol_pino(w,77,650,10,90,'#004D40')
arbol_pino(w,62,633,10,90,'#004d40')
arbol_pino(w,50,625,10,90,'#004D40')
arbol_pino(w,58,510,10,90,'#212121')
arbol_pino(w,77,580,10,90,'#004D40')
arbol_pino(w,62,573,10,90,'#004d40')
arbol_pino(w,50,585,10,90,'#004D40')
arbol_pino(w,58,590,10,90,'#212121')
arbol_pino(w,95,566,10,90,'#004D40')
arbol_pino(w,80,579,10,90,'#212121')
arbol_pino(w,77,550,10,90,'#004D40')
arbol_pino(w,62,533,10,90,'#004d40')
arbol_pino(w,10,525,10,90,'#004D40')
arbol_pino(w,18,510,10,90,'#212121')
arbol_pino(w,12,690,10,90,'#212121')
arbol_pino(w,5,666,10,90,'#004D40')
arbol_pino(w,8,679,10,90,'#212121')
arbol_pino(w,17,650,10,90,'#004D40')
arbol_pino(w,22,633,10,90,'#004d40')
arbol_pino(w,30,625,10,90,'#004D40')
arbol_pino(w,38,510,10,90,'#212121')
arbol_pino(w,47,580,10,90,'#004D40')
arbol_pino(w,22,573,10,90,'#004d40')
arbol_pino(w,35,585,10,90,'#004D40')
arbol_pino(w,14,590,10,90,'#212121')
arbol_pino(w,1,566,10,90,'#004D40')
arbol_pino(w,6,579,10,90,'#212121')
arbol_pino(w,50,673,10,90,'#004d40')
arbol_pino(w,45,685,10,90,'#004D40')
arbol_pino(w,34,690,10,90,'#212121')
arbol_pino(w,58,666,10,90,'#004D40')
arbol_pino(w,40,679,10,90,'#212121')
arbol_pino(w,40,530,10,90,'#004d40')
arbol_pino(w,40,535,10,90,'#004d40')
arbol_pino(w,40,550,10,90,'#004d40')
arbol_pino(w,40,650,10,90,'#212121')
arbol_pino(w,10,600,10,90,'#004d40')
arbol_pino(w,50,600,10,90,'#212121')
arbol_pino(w,90,600,10,90,'#004d40')

arbol_pino(w,506,640,10,90,'#212121')
arbol_pino(w,512,650,10,90,'#212121')
arbol_pino(w,530,662,10,90,'#004d40')
arbol_pino(w,547,653,10,90,'#004d40')
arbol_pino(w,549,670,10,90,'#004d40')
arbol_pino(w,570,675,10,90,'#004d40')
arbol_pino(w,584,680,10,90,'#212121')

arbol_pino(w,600,650,10,90,'#212121')
arbol_pino(w,610,640,10,90,'#212121')
arbol_pino(w,620,630,10,90,'#212121')
arbol_pino(w,635,620,10,90,'#212121')
arbol_pino(w,640,610,10,90,'#004d40')
arbol_pino(w,650,624,10,90,'#004d40')
arbol_pino(w,660,617,10,90,'#004d40')

arbol_pino(w,700,617,10,90,'#004d40')
arbol_pino(w,660,617,10,90,'#004d40')
arbol_pino(w,660,617,10,90,'#004d40')
arbol_pino(w,660,617,10,90,'#004d40')

arbol_pino(w,800,617,10,90,'#212121')
arbol_pino(w,780,580,10,90,'#212121')
arbol_pino(w,790,622,10,90,'#212121')
arbol_pino(w,810,594,10,90,'#212121')
arbol_pino(w,830,680,10,90,'#212121')
arbol_pino(w,800,697,10,90,'#212121')
arbol_pino(w,780,670,10,90,'#004d40')
arbol_pino(w,790,685,10,90,'#004d40')
arbol_pino(w,610,693,10,90,'#004d40')
arbol_pino(w,630,700,10,90,'#004d40')
arbol_pino(w,610,594,10,90,'#004d40')
arbol_pino(w,630,680,10,90,'#004d40')
arbol_pino(w,600,697,10,90,'#004d40')
arbol_pino(w,680,670,10,90,'#212121')
arbol_pino(w,690,685,10,90,'#212121')
arbol_pino(w,610,693,10,90,'#212121')
arbol_pino(w,630,700,10,90,'#212121')

arbol_pino(w,900,800,200,90,'#004D40')
arbol_pino(w,800,800,100,90,'#004D40')
arbol_pino(w,100,800,170,90,'#004D40')
arbol_pino(w,300,800,100,90,'#004D40')
arbol_pino(w,200,800,100,90,'#00796B')
arbol_pino(w,700,800,100,90,'#004D40')
arbol_pino(w,300,800,70,90,'#26a69a')
arbol_pino(w,100,800,70,90,'#26a69a')
arbol_pino(w,900,800,70,90,'#26A69A')
arbol_pino(w,700,800,70,90,'#26A69A')
arbol_pino(w,800,800,100,90,'#26A69A')

#arbusto(w,100,800,30,90,'#64DD17')
#arbol_pino(w,230,500,75,90,'004D400')
mainloop()


#tutorias de metodos: http://formaciontutorias.ipn.mx