from agent import *

training_num=2000
max_len=5000
agent=Agent()

for episode in range(training_num):
  w=World(0,5,90)
  for step in range(max_len):
    a=agent.e_greedy(w.x,w.y,w.o)
    nextx,nexty,nexto,R=w.move(a)
    a2=agent.e_greedy(nextx,nexty,nexto)
    agent.update(w.x,w.y,w.o,a,R,nextx,nexty,nexto,a2)
    w.x=nextx
    w.y=nexty
    w.o=nexto
    if(R==0):
      break
  
  if(episode%100==0):
    print(episode)

f='agent.sav'
file=open(f,'wb')
pickle.dump(agent,file)
file.close()