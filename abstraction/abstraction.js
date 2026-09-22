
// Kaylie, 203608@gscs.ca, Functions and Abstractions
function setup() {
  createCanvas (400, 400);
}

// This is a function to draw the shapes to their parameters
function draw() {
    draw_fixed_square();
    draw_circle(100, 200, 100);
    draw_concentric_circles(300, 200);
}

// function that creates a square
function draw_fixed_square(){ 
   rect(50, 50, 50, 50);
  }

//function that creates the circle
//*Parameter: x,y, d are the coordinates that will draw the circle
function draw_circle(x, y, d){
    circle(x, y, d);
  }

  
  //function that makes the 3 circles on top of one another
  //*Parameters: x,y are the coordinates that will have the centre coordinates
  function draw_concentric_circles(x,y){
     circle (x, y, 180);
     circle (x, y, 120);
     circle (x, y, 60);
 }
