

import time, socket, sys
import matplotlib.pyplot as plt

from matplotlib import style

from pathCalc import Path

v=[]
w=[]
m=[]
g=[]

for i in range(1,9):
    
    for j in range(1,9):
        m.append(j)
        g.append(i)
    
style.use('fivethirtyeight')
p=[]
q=[]
l=[]
dx=0
dy=0
path=Path()
flag=0
plt.ion()


message=""
print("\nWelcome to the Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections from the client...\n")
conn, addr = s.accept()
print("Received connection from client  ", addr[0], "(", addr[1], ")\n")
s_name = conn.recv(1024)
s_name = s_name.decode()

print(s_name, "has connected to the chat room\nEnter 'e' to exit chat room\n")
conn.send(name.encode())
j=0
i=0

while(i<100):

        if(len(l)==0):
            message="Enter Starting Point : "
            flag=2
            
                
        else:
            message="True"
            i+=1
           
            
        if(i==1):
            message="Enter Destination Point : "
            flag=1
            
    
        if (message == "e"):
            message = "Left the room!"
            conn.send(message.encode())
            print("\n")
            flag=3
            break
        
        else:
            
            conn.send(message.encode())
            
        message = conn.recv(1024)
        plt.close('all')        
        message = message.decode()    
        l.append(message)

        
        
        x,y=l[i].split(',')


        if(flag==1):

            dx=int(x)
            dy=int(y)
            path.setDestinationPoints(int(x),int(y))
            
            v,w=path.calc_path()
            flag=3
            n=1
        elif(flag==2):
            
            path.setStartingPoints(int(x),int(y))
            p.append(int(x))
            q.append(int(y))
            
        if((int(x) in v )and (int(y) in w) and (i!=1)):
            if((int(x) == v[n] )and (int(y) == w[n])):
                if(int(x)==dx and int(y)==dy):
                    
                    conn.send('Reached Destination'.encode())
                    p.append(int(dx))
                    q.append(int(dy))
                else:
                    p.append(int(x))
                    q.append(int(y))
                    n+=1
                
                
            else:
        
                conn.send('Shortest Path Not Chosen'.encode())
                
                del l[i]
                i-=1
        
        try:
            plt.plot(p,q,g,m,'ro') 
            plt.show(block=False)
            
            plt.pause(3)
            

        except ValueError:
            
            print("I don't think you have sent number coordinates !! Send again !!")
            i-=1
 
        print(s_name, ":", message)
        print(v)
        print(w)

       
