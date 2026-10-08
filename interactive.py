#Kaylie L, 203608@gscs.ca, Interactive Circles

#In the function set-up w/ no parameters, I have the size and background to create the landscape of the code
def setup():
    size(400,400)
    background(0)
    
#What the function draw is doing is that its continously updating the code for the circles to follow the mouse's coordinates rather than in just one spot
def draw():
    #I set the background again in draw so it will keep being updated
    background(0)
    
    # This next part of the code is my two circles that have their respective colour
    fill(204, 153, 255)
    ellipse(mouse_x, mouse_y, 100, 100)
    
    fill(255, 153, 204)
    ellipse(mouse_x, mouse_y, 50, 50)
    
    #I returned everything so it will updated each time which is crucial if we want the circle to follow the mouse
    return

    