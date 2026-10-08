#Kaylie L, 203608@gscs.ca, The Robot
#Size of what I will code
size(900,900)
background(0, 0, 255)

#This function will draw the head and ears of the robot with parameter PC which stands for primary colour
#Parameter PC will be applied to the heads and ears to change its colour 
def draw_head(pc):
    
    #this is where the parameter will be used to color the head and ears
    fill(pc)
    
    #the two ears on the head
    ellipse(220, 150, 120, 120)
    ellipse(380, 150, 120, 120)

    #the head
    ellipse(300, 230, 230, 230)

    #this fill will be for the eyes and to change them to black
    fill(0)
    
    #This will draw the robot's two eyes
    ellipse(265, 210, 25, 25)
    ellipse(335, 210, 25, 25)

#This function draws the body of the robot with paramater PC
#Parameter PC will once again be called when the torso has to change its colour
def draw_body(pc):
    
    #parameter applied and only to the torso of the robot
    fill(pc)
    
    #draws the torso
    ellipse(300, 505, 250, 321)
    
    #the three coloured buttons where it changes the color of each one and its circle placement
    fill(0, 0, 255)
    ellipse(300, 500, 20, 20)
    
    fill(255,102,178)
    ellipse(270, 500, 20, 20)

    fill(153, 51, 255)
    ellipse(330, 500, 20, 20)
    
#Function to draw the arms of the robot with four parameters PC and SC which is secondary colour and three times
#The parameter pc will be used for the arms
#The parameter sc1-sc3 will be for the fists and change its colour
def draw_arms(pc, sc1, sc2, sc3):
    
    #Draws the arms with primary colour
    fill(pc)
    rect(100, 400, 130, 35)
    rect(365, 400, 130, 35)
    
    #Draws the fists of each arm with secondary colour which is pink
    fill(sc1, sc2, sc3)
    ellipse(85, 415, 60, 60)
    ellipse(515, 415, 60, 60)
    
#This function draws the legs of the robot with parameters: pc, sc1, sc2, and sc3
#Once again, PC is only applied to the legs portion and sc1-sc3 will be for the feet color
def draw_legs(pc, sc1, sc2, sc3):
    #Draws the legs to primary colour
    fill(pc)
    rect(230, 630, 40, 150)
    rect(320, 630, 40, 150)
    
    #Draws the feet with secondary color
    fill(sc1, sc2, sc3)
    ellipse(248, 800, 60, 60)
    ellipse(338, 800, 60, 60)
    
#This function will be used to draw the robot in its entirety with parameters PC, SC1, SC2, SC3      
def draw_the_robot(pc, sc1, sc2, sc3):
    #draws the robot also put arms and legs first so it wont overlap with the torso to look more natural
    draw_arms(pc, sc1, sc2, sc3)
    draw_legs(pc, sc1, sc2, sc3)
    draw_head(pc)
    draw_body(pc)

#The only place where there is specfic numbers for the pc and sc colours
draw_the_robot(255, 255, 225, 0)

def mouse_clicked():
    background(0, 0, 204)
    draw_the_robot(200, mouse_y, mouse_x, 0)







