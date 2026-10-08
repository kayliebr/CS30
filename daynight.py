#Kaylie L, 203608@gscs.ca, Day/night Scene

#The function will set up the code to the day scene automatically with the canvas also starting it
def setup():
    #The size of the canvas
    size(600,600)
    
    #The blue background
    background(51, 153, 255)
    
    #This will make the shapes not have their black outline and make it look natural
    no_stroke()
    
    #All the shapes below will now be formatted with their color then shape
    #The yellow light
    fill(255, 255, 0)
    ellipse(290, 50, 60, 60)
    
    #The brown base at the bottom
    fill(204, 102, 0)
    rect(0, 500, 600, 120)
    
    #The three boxes 
    fill(255, 128, 0)
    rect(60, 400, 100, 100)
    
    fill(255, 0, 255)
    rect(240, 400, 100, 100)
    
    fill(0, 255, 0)
    rect(420, 400, 100, 100)
    
#This function will be called when any key is pressed and will change the following code underneath it to change its colour to the night scene
def key_pressed():
    #The new background that is a darker shade of blue
    background(0,51,102)
    
    #The new white light
    fill(255)
    ellipse(290, 50, 60, 60)
    
    #The new dark brown base
    fill(102, 51, 0)
    rect(0, 500, 600, 120)
    
    #The three boxes that are now a darker shade of their original colour
    fill(204, 102, 0)
    rect(60, 400, 100, 100)
    
    fill(153, 0, 153)
    rect(240, 400, 100, 100)
  
    fill(0, 153, 0)
    rect(420, 400, 100, 100)
    
    
