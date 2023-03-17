#Assignment: Delivery Robot
#Marks[3%]
#Classes: BIT (A + B) & BCS(A +B) Individual presentation
#Start State: o103
#Goal:  (Given individually)
#Deadline: 27 Nov. 2021
########################################################################

from agentMiddle import Rob_middle_layer
from agents import Environment

class Rob_top_layer(Environment):
    ## meelaha soo daabacmaayo ee screenka
    def __init__(self, middle, timeout=160, locations = {'o103':(0,0), 
                          'o109':(50,10), 'o119':(65,50),'r123':(40,51),'BCS12-B':(34,22), 'Goal':(30,-10)} ):
        """middle is the middle layer
        timeout is the number of steps the middle layer goes before giving up
        locations is a loc:pos dictionary
            where loc is a named location, and pos is an (x,y) position.
        """
        self.middle = middle
        self.timeout = timeout  # number of steps before the middle layer should give up
        self.locations = locations
        
    def do(self,plan):
        """carry out actions.
        actions is of the form {'visit':list_of_locations}
        It visits the locations in turn.
        """
        to_do = plan['visit']
        for loc in to_do:
            position = self.locations[loc]
            arrived = self.middle.do({'go_to':position, 'timeout':self.timeout})
            self.display(1,"Arrived at",loc,arrived)

import matplotlib.pyplot as plt

class Plot_env(object):
    def __init__(self, body,top):
        """sets up the plot
        """
        self.body = body
        plt.ion()
        plt.clf()
        plt.axes().set_aspect('equal')
        for wall in body.env.walls:
            ((x0,y0),(x1,y1)) = wall
            plt.plot([x0,x1],[y0,y1],"-k",linewidth=3)
        for loc in top.locations:
            (x,y) = top.locations[loc]
            plt.plot([x],[y],"k<")
            plt.text(x+1.0,y+0.5,loc) # print the label above and to the right
        plt.plot([body.rob_x],[body.rob_y],"go")
        plt.draw()
        plt.title('Assignment : Delivery Robot [3% Marks]. Deadline : 27 Nov. Classes:IT & CS ')
       


    def plot_run(self):
        """plots the history after the agent has finished.
        This is typically only used if body.plotting==False
        """
        xs,ys = zip(*self.body.history)
        plt.plot(xs,ys,"go")
        wxs,wys = zip(*self.body.wall_history)
        plt.plot(wxs,wys,"ro")
        plt.draw()

from agentEnv import Rob_body, Rob_env
## Xariiqooyinka la sawiraayo
env = Rob_env({((20,0),(30,20)), ((70,-5),(70,25))})
body = Rob_body(env)
middle = Rob_middle_layer(body)
top = Rob_top_layer(middle)

#try:
pl=Plot_env(body,top)
## Meelaha lasoo booqan doono
top.do({'visit':['o103','o109','o119','r123','BCS12-B','Goal']})
# You can directly control the middle layer:

#Meesha Goalka eh ee ugu dambeenta la gaaraayo
middle.do({'go_to':(30,-10), 'timeout':160})
# Can you make it crash?

# Robot Trap for which the current controller cannot escape:
trap_env = Rob_env({((10,-21),(10,0)), ((10,10),(10,31)), ((30,-10),(30,0)),
                    ((30,10),(30,20)),  ((50,-21),(50,31)), ((10,-21),(50,-21)),
                    ((10,0),(30,0)),  ((10,10),(30,10)),  ((10,31),(50,31))})
trap_body = Rob_body(trap_env,init_pos=(-1,0,90))
trap_middle = Rob_middle_layer(trap_body)
trap_top = Rob_top_layer(trap_middle,locations={'goal':(71,0)})

#Robot trap exercise:
#pl=Plot_env(trap_body,trap_top)
#trap_top.do({'visit':['goal']})