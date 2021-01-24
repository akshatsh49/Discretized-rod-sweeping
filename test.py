from agent import *

# load agent 
f='agent.sav'
file=open(f,'rb')
agent=pickle.load(file)
file.close()

max_len=2000
w=World(0,5,90)
x=[]
y=[]
o=[]
for step in range(max_len):
    x.append(w.x)
    y.append(w.y)
    o.append(w.o)
    a=agent.e_greedy(w.x,w.y,w.o)
    nextx,nexty,nexto,R=w.move(a)
    a2=agent.e_greedy(nextx,nexty,nexto)
    agent.update(w.x,w.y,w.o,a,R,nextx,nexty,nexto,a2)
    w.x=nextx
    w.y=nexty
    w.o=nexto
    if(R==0):
        x.append(w.x)
        y.append(w.y)
        o.append(w.o)
        break

print(step)

#animate the episode 
fig=plt.figure()
cam=Camera(fig)

# plot each rod instant
for i in range(len(x)):
    plt.plot([w.x1,w.x1] , [w.y1,w.y2], 'b')
    plt.plot([w.x2,w.x2] , [w.y1,w.y2] , 'b')
    plt.plot([w.x1,w.x2] , [w.y1,w.y1] , 'b')
    plt.plot([w.x1,w.x2] , [w.y2,w.y2] ,'b')
    plt.xlim(w.xmin-1,w.xmax+1)
    plt.ylim(w.ymin,w.ymax)
    plt.tick_params(axis='both',which='both',bottom=False,top= False,labelbottom=False,right=False,left=False,labelleft=False)
    x1=x[i]-w.l/2*math.cos(o[i]*3.141/180)
    x2=x[i]+w.l/2*math.cos(o[i]*3.141/180)
    y1=y[i]-w.l/2*math.sin(o[i]*3.141/180)
    y2=y[i]+w.l/2*math.sin(o[i]*3.141/180)
    plt.plot([x1,x2],[y1,y2],'r')
    cam.snap()

# highlight terminal state if episode finishes
if(step<max_len-1):
    for i in range(100):
        plt.plot([w.x1,w.x1] , [w.y1,w.y2], 'b')
        plt.plot([w.x2,w.x2] , [w.y1,w.y2] , 'b')
        plt.plot([w.x1,w.x2] , [w.y1,w.y1] , 'b')
        plt.plot([w.x1,w.x2] , [w.y2,w.y2] ,'b')
        plt.xlim(w.xmin-1,w.xmax+1)
        plt.ylim(w.ymin,w.ymax)
        plt.tick_params(axis='both',which='both',bottom=False,top= False,labelbottom=False,right=False,left=False,labelleft=False)
        plt.plot([30,30], [0,10] ,'r')
        cam.snap()

anim=cam.animate(interval = 30, repeat = True, repeat_delay = 500)
anim.save('episode.mp4')

file=open(f,'wb')
pickle.dump(agent,file)
file.close()