import processing.video.*;
import oscP5.*;
import netP5.*;

Movie movie;
OscP5 oscP5;
NetAddress myRemoteLocation;

PImage img;
color c;
float z;                            // zed coordinate
int columns, rows, loc, s = 0;      // s is the index for random jumps in video projection

// PARAMETERS 
boolean arrivato = false;           // arrivato is a boolean check for RECEIVED OSC message
int port1 = 5005;
int cellsize = 2;                   // resolution for exploded cells
int counterOSC=0;
float omega = 0;                    // angular freq for oscillations in z value
float OSCvalue = 370;               // default value

void setup(){
  frameRate(60);
 
  movie = new Movie(this, "C:/Users/jacop/Desktop/ImUS/themorph.avi");    // directory of chosen video
  
  size ( 500, 600, P3D );
 
  movie.play();
  movie.loop();
  movie.speed(2.5);
  oscP5 = new OscP5(this, port1);                                         // listening on port1
  myRemoteLocation = new NetAddress("255.255.255.240", 8000);             // sending thru port 8000
}

void draw(){
 
  movie.resize( 500, 600 );
  for(int i = 0; i < movie.height; ++i){
    for(int j = 0; j < movie.width; ++j){
      
      loc = j + i * movie.width;
      
      c = movie.pixels[loc]; 
      
      omega = omega + 0.001;
      if (omega > 200){  omega=0;  }
    
      float a = 0;
      float b = width;
      float min = 120;
      float max = 350;
      
      float fraction = ((b - a) * (OSCvalue - min) / (max - min)) + a;    // linearizing behavior when people are near each other

      if (OSCvalue >= 200 && OSCvalue <= 220){ 
        fraction = OSCvalue * 3; 
      }
      if (OSCvalue > 220 && OSCvalue <= 240){ 
        fraction = OSCvalue * 5;   
      }
      if (OSCvalue > 240 && OSCvalue <= 270){ 
        fraction = OSCvalue * 7;   
      }
      if (OSCvalue > 270 && OSCvalue <= 300){ 
        fraction = OSCvalue * 9;   
      }
      if (OSCvalue > 300 && OSCvalue <= 330){ 
        fraction = OSCvalue * 11;   
      }
      if (OSCvalue > 330 && OSCvalue <= 360){ 
        fraction = OSCvalue * 13;   
      }
      if (OSCvalue > 360){ 
        fraction = OSCvalue * 15;   
      }
   
      z = fraction * tan(j*i) * sin(omega);
      
      pushMatrix();
      translate(j, i , z );
      noStroke();
      fill(c);
      rect(0, 0, cellsize, cellsize); 
      popMatrix();
      }
    }
    
  s++;
  if(s >=22 ){
    movie.jump(random(movie.duration()));
    s = 0;
  }
}

void movieEvent(Movie m) {
  m.read();
}

void oscEvent(OscMessage theOscMessage) {
   if(theOscMessage.checkAddrPattern("/IDP") == true) {
     float act_val = theOscMessage.get(0).floatValue();
     if (act_val > 120){
       OSCvalue = act_val;
       arrivato = true;
       return;
      }
      else {OSCvalue = 121; return;}
    }
}

void mousePressed() {                                                    // connection test function
  OscMessage myMessage = new OscMessage("/test");
  myMessage.add(2.7);
  oscP5.send(myMessage, myRemoteLocation); 
}
