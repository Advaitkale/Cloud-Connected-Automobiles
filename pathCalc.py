
import math
class Path:

    def __init__(self):
        sx=0
        sy=0
        dx=0
        dy=0
        
    def setStartingPoints(self,sx,sy):
        self.sx=sx
        self.sy=sy
    def setDestinationPoints(self,dx,dy):
        self.dx=dx
        self.dy=dy

    def calc_path(self):
        x=[]
        y=[]
 #       if((self.dx!=self.sx) and (self.dy!=self.sy)):
        for i in range(max(abs(self.dx-self.sx),abs(self.dy-self.sy))):
            if((self.dx-self.sx)>=(self.dy-self.sy)):
                if((self.dx>self.sx) and (self.dy>self.sy)):
                    x.append(self.sx+i)
                    y.append(self.sy+i)
##                      if(self.dy==self.sy+i):
##                          break
                elif((self.dx>self.sx) and (self.dy<self.sy)):
                    x.append(self.sx+i)
                    y.append(self.sy-i)
##                      if(self.dy==self.sy-i):
##                          break
                elif((self.dx<self.sx) and (self.dy>self.sy)):
                    x.append(self.sx-i)
                    y.append(self.sy+i)
##                      if(self.dy==self.sy+i):
##                          break
                elif((self.dx<self.sx) and (self.dy<self.sy)):
                    x.append(self.sx-i)
                    y.append(self.sy-i)
##                      if(self.dy==self.sy-i):
##                          break

                        
                elif((self.dx==self.sx) and (self.dy<self.sy)):
                    x.append(self.sx)
                    y.append(self.sy-i)
##                      if(self.dy==self.sy-i):
##                          break
                elif((self.dx==self.sx) and (self.dy>self.sy)):
                    x.append(self.sx)
                    y.append(self.sy+i)
##                      if(self.dy==self.sy+i):
##                          break
                elif((self.dx<self.sx) and (self.dy==self.sy)):
                    x.append(self.sx-i)
                    y.append(self.sy)
##                      if(self.dy==self.sy-i):
##                          break
                elif((self.dx>self.sx) and (self.dy==self.sy)):
                    x.append(self.sx+i)
                    y.append(self.sy)
##                      if(self.dy==self.sy+i):
##                          break


                        
            elif((self.dx-self.sx)<(self.dy-self.sy)):
                    
                if((self.dx>self.sx) and (self.dy>self.sy)):
                    x.append(self.sx+i)
                    y.append(self.sy+i)
##                      if(self.dx==self.sx+i):
##                          break
                elif((self.dx>self.sx) and (self.dy<self.sy)):
                    x.append(self.sx+i)
                    y.append(self.sy-i)
##                      if(self.dx==self.sx-i):
##                          break
                elif((self.dx<self.sx) and (self.dy>self.sy)):
                    x.append(self.sx-i)
                    y.append(self.sy+i)
##                      if(self.dx==self.sx+i):
##                          break
                elif((self.dx<self.sx) and (self.dy<self.sy)):
                    x.append(self.sx-i)
                    y.append(self.sy-i)
##                      if(self.dx==self.sx-i):
##                          break

                        
                elif((self.dx==self.sx) and (self.dy<self.sy)):
                    x.append(self.sx)
                    y.append(self.sy-i)
##                      if(self.dx==self.sx-i):
##                          break
                elif((self.dx==self.sx) and (self.dy>self.sy)):
                    x.append(self.sx)
                    y.append(self.sy+i)
##                      if(self.dx==self.sx+i):
##                          break
                elif((self.dx<self.sx) and (self.dy==self.sy)):
                    x.append(self.sx-i)
                    y.append(self.sy)
##                      if(self.dx==self.sx-i):
##                          break
                elif((self.dx>self.sx) and (self.dy==self.sy)):
                    x.append(self.sx+i)
                    y.append(self.sy)
##                      if(self.dx==self.sx+i):
##                          break
            elif(((self.dx-self.sx)==(self.dy-self.sy)) and (self.dy>self.sy)):
                x.append(self.sx+i)
                y.append(self.sy+i) 
                
            elif(((self.dx-self.sx)==(self.dy-self.sy)) and (self.dy<self.sy)):
                x.append(self.sx-i)
                y.append(self.sy-i) 
                
                    
        x.append(self.dx)
        y.append(self.dy)
        return x,y
        
p=Path()
p.setStartingPoints(1,6)
p.setDestinationPoints(1,2)          
v,w=p.calc_path()

