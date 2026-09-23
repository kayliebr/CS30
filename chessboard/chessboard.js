// Kaylie L, 203608@gscs.ca, Chessboard
function setup() {
  createCanvas(200,200);
  
  // For each row I am repeating the same process which is fill and rect and just the changing the color and x,y coordinate
  // When I am changing the x,y coordinate, the x coordinate will stay the same pattern on going up 0-150 by 50 each time
  //The y-coordinate will go up by 50 each row
  
  // Row 1
  fill(255);
  rect (0, 0, 50, 50);
  fill (0);
  rect(50, 0, 50, 50);
  fill (255);
  rect (100, 0, 50, 50);
  fill (0);
  rect (150, 0, 50, 50);
  
  //row 2
  fill (0);
  rect(0, 50, 50, 50);
  fill(255);
  rect (50, 50, 50, 50);
  fill (0);
  rect (100, 50, 50, 50);
  fill(255);
  rect(150, 50, 50 , 50);
 
 //row 3
 fill(255);
 rect(0, 100, 50, 50)
 fill(0);
 rect(50, 100, 50, 50);
 fill(255);
 rect(100, 100, 50, 50);
 fill(0);
 rect(150, 100, 50, 50);
 
 //row 4
 fill (0);
 rect(0, 150, 50, 50);
 fill(255);
 rect(50, 150, 50, 50);
 fill(0);
 rect(100, 150, 50, 50);
 fill(255);
 rect(150, 150, 50, 50);

}


function draw() {

}
