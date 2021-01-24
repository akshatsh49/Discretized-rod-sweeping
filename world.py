import numpy as np
from collections import defaultdict 
import matplotlib.pyplot as plt
import matplotlib.animation as animations
import pickle
import random
import math
from celluloid import Camera

class World():
  def __init__(self,x,y,o):
    self.l=10
    self.x=x
    self.y=y
    self.o=o
    self.orad=self.o*3.1415/180
    self.omin=-90
    self.omax=90
    self.xmin=0
    self.ymin=0

    # boundaries of the environment 
    self.xmax=30
    self.ymax=18

    #bounds of the box
    self.x1=10  
    self.x2=20
    self.y1=0
    self.y2=10

    self.xstep=1
    self.ystep=1
    self.ostep=5
    self.action_space=['xu','xd','yu','yd','ou','od']

  def collide_with_box(self):
    min_x_extent=self.x1
    max_x_extent=self.x2
    min_y_extent=self.y1
    max_y_extent=self.y2
    eps=0.0003

    #first with x=x1 and x2
    if(self.o!=90 and self.o!=-90):
      ysol=self.y+(self.x1-self.x)*math.tan(self.orad)
      xsol=self.x1
      if(xsol>=min_x_extent and xsol<=max_x_extent and ysol>=min_y_extent and ysol<=max_y_extent):
        return 1#,'with x1'
      xsol=self.x2
      ysol=self.y+(self.x2-self.x)*math.tan(self.orad)
      if(xsol>=min_x_extent and xsol<=max_x_extent and ysol>=min_y_extent and ysol<=max_y_extent):
        return 1#,'with x2'

    else:
      if(self.x==self.x1 or self.x==self.x2):
        ypos1=self.y+self.l/2
        ypos2=self.y-self.l/2
        if(ypos1>=0 and ypos2<=0):
          return 1#,3
        if(ypos1>=self.y2 and ypos2<=self.y2):
          return 1#,4
    
    #now with y=y1 and y2
    if(self.o!=0):
      ysol=min_y_extent
      xsol= self.x + (ysol-self.y)/math.tan(self.orad)
      if(xsol>=min_x_extent and xsol<=max_x_extent and ysol>=min_y_extent and ysol<=max_y_extent):
        return 1#,'with y1'
      ysol=max_y_extent
      xsol=(ysol-self.y)/math.tan(self.orad)+self.x
      if(xsol>=min_x_extent and xsol<=max_x_extent and ysol>=min_y_extent and ysol<=max_y_extent):
        return 1#,'with y2'
    
    else:
      if(self.y==self.y1 or self.y==self.y2):
        xpos1=self.x-(self.l)/2
        xpos2=self.x+(self.l)/2
        if(xpos2>=self.x1 and xpos1<=self.x1):
          return 1#,7
        if(xpos2>=self.x2 and xpos1<=self.x2):
          return 1#,8
    return 0

  def within_boundary(self):
    min_x_extent=min(self.x+(self.l)/2*(math.cos(self.orad)),self.x-(self.l)/2*(math.cos(self.orad)))
    max_x_extent=max(self.x+(self.l)/2*(math.cos(self.orad)),self.x-(self.l)/2*(math.cos(self.orad)))
    min_y_extent=min(self.y+(self.l)/2*(math.sin(self.orad)),self.y-(self.l)/2*(math.sin(self.orad)))
    max_y_extent=max(self.y+(self.l)/2*(math.sin(self.orad)),self.y-(self.l)/2*(math.sin(self.orad)))
    eps=0.0003  # tolerance for contact
    if(max_x_extent>self.xmax+eps):
      return 0#,1
    if(min_x_extent<self.xmin-eps):
      return 0#,2
    if(max_y_extent>self.ymax+eps):
      return 0#,3
    if(min_y_extent<self.ymin-eps):
      return 0#,4
    else :
      return 1

  def move(self,a):

    if(a=='xu'):
      nextx=self.x+self.xstep
      nexty=self.y
      nexto=self.o
      temp=World(nextx,nexty,nexto)
      if(temp.collide_with_box() or (not temp.within_boundary())):
        nextx=self.x
    if(a=='xd'):
      nextx=self.x-self.xstep
      nexty=self.y
      nexto=self.o
      temp=World(nextx,nexty,nexto)
      if(temp.collide_with_box() or (not temp.within_boundary())):
        nextx=self.x

    if(a=='yu'):
      nextx=self.x
      nexty=self.y+self.ystep
      nexto=self.o
      temp=World(nextx,nexty,nexto)
      if(temp.collide_with_box() or (not temp.within_boundary())):
        nexty=self.y
    if(a=='yd'):
      nextx=self.x
      nexty=self.y-self.ystep
      nexto=self.o
      temp=World(nextx,nexty,nexto)
      if(temp.collide_with_box() or (not temp.within_boundary())):
        nexty=self.y

    if(a=='ou'):
      nextx=self.x
      nexty=self.y
      nexto=self.o+self.ostep

      #the angle cycles from beyond +90 deg to -90 deg 
      if(nexto>self.omax):
        nexto=self.omin+(nexto-self.omax)
      temp=World(nextx,nexty,nexto)
      if(temp.collide_with_box() or (not temp.within_boundary())):
        nexto=self.o
    if(a=='od'):
      nextx=self.x
      nexty=self.y
      nexto=self.o-self.ostep

      #the angle cycles from beyond -90 deg to +90 deg 
      if(nexto<self.omin):
        nexto=self.omax-(self.omin-nexto)
      temp=World(nextx,nexty,nexto)
      if(temp.collide_with_box() or (not temp.within_boundary())):
        nexto=self.o
      
    if(nextx==30 and nexty==5 and (nexto==90 or nexto==-90)): #terminal state 
      R=0
    else :
      R=-1
    return nextx,nexty,nexto,R

# tough section is over :)