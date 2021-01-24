# Discretized-rod-sweeping

## Brief Description Of The Task
An implementation of Reinforcement learning on the task of moving a rod from one end of the room to the other.

## The Environment 
<img src="https://github.com/akshatsh49/Discretized-rod-sweeping/blob/master/saved_fig.png" width=300 class="" />
The rod is restricted to stay within the boundaries of the room and not collide with the obstacle.
The starting and terminal positions are vertical rods on the left and right respectively.</br>
Every non-terminal transition generates a (-1) reward

## The Agent
The action space of the agent comprises of six possible actions : each changing some variable (x coordinate , y coordinate , angle of rod) by a predetermined step size. </br>
The agent follows a simple Sarsa algorithm for learning.

## Results 
<img src="https://github.com/akshatsh49/Discretized-rod-sweeping/blob/master/episode.gif" width=300 />
I extrapolated the ending of the episode to highlight the agent reaching the terminal state.

## Future Work
* Implementing a general 'box' class which contains :
  * a render method to display the obstacle
  * a collision method to detect if the rod collides with the obstacle
  * Integrating changes with world.move() method.
* Using queuing techniques like priority sweeping 
* Use function approximations or Deep RL techniques which are known to work better than space discretization.
