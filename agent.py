from world import *

class Agent():
  def __init__(self,alpha=0.01,gamma=1,eps=0.1):
    self.alpha=alpha
    self.gamma=gamma
    self.eps=eps
    self.q=defaultdict(int)
    self.action_space=['xu','xd','yu','yd','ou','od']

  def greedy(self,x,y,o):
    best='xu'
    m=self.q[x,y,o,best]
    for a in self.action_space:
      if(self.q[x,y,o,a]>m):
        m=self.q[x,y,o,a]
        best=a
    return best

  def e_greedy(self,x,y,o):
    if(np.random.random()>=self.eps):
      return self.greedy(x,y,o)
    else :
      return random.choice(self.action_space)

  def update(self,x,y,o,a,R,x1,y1,o1,a1):
    # a simple Sarsa update 
    if(x1==30 and y1==5 and (o1==90 or o1==-90)):
      nq=0
    else :
      nq=self.q[x1,y1,o1,a1]
    self.q[x,y,o,a]+=self.alpha*(R+self.gamma*(nq)-self.q[x,y,o,a])