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
