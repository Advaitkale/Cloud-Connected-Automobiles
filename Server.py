
import time, socket, sys
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from matplotlib import style

m=[]
g=[]
for i in range(1,9):
    
    for j in range(1,9):
        m.append(j)
        g.append(i)
    
##    m=[]
##    g=[]



##plt.title('Sample Plot')
##plt.show()





style.use('fivethirtyeight')
p=[]
q=[]
l=[]

##def function(p,q):
##    fig.add_subplot(1,1,1).plot(p,q)


plt.ion()


message=""
print("\nWelcome to Chat Room\n")
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
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
#k=1
s_name = conn.recv(1024)
s_name = s_name.decode()

print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())
j=0
i=0



while(i<100):
        

        if(len(l)==0):
            message="Enter Starting Point : "
            
        
        
        elif(l[i]==2):
            message ="True"
            i+=1
                
        else:
            message="False"
            i+=1
        if(i==1):
            message="Enter Destination Point : "    
    
        if (message == "[e]"):
            message = "Left room!"
            conn.send(message.encode())
            print("\n")
            break
        else:
            conn.send(message.encode())
            
            
        message = conn.recv(1024)
        plt.close('all')        
        message = message.decode()
            
        l.append(message)
        x,y=l[i].split(',')
        
        
        p.append(int(x))
        q.append(int(y))
        
        try:
            plt.plot(p,q,g,m,'ro')
           
            #plt.plot(m,g,color='k')
            #ani = animation.FuncAnimation(fig, func=function(p,q), interval=1000)
            plt.show(block=False)
            plt.pause(3)

        except ValueError:
            print("I don't think you have sent number coordinates !! Send again !!")
            i-=1
 
        print(s_name, ":", message)
        print(p)
       
