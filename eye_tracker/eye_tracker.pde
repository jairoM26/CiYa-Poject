/**
 * eye_tracker.pde
 * @details Proram to detect the eye pupil
 * 
 * @author LuisDiego Delgado Alfaro <>
 * @author JuanDiego Delgado Vargas <>
 * @author JeanCarlos Gonzales Hernandez <>
 * @author Mariana Guerrero Jimenez <>
 * @author Jairo Mendez Martinez <jairomendezmartinez@gmail.com>
 * @date 14-07-2018
 * 
 * Execution: open with procesing
 * what do you need?: add the libraries of video and nyar4psg
 * if you are using ubuntu depending on the version the gstreaming librarie is going to be a problem
 * so if you have a problem run the following commands:
 *            sudo apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
 *            sudo apt-get install gstreamer0.10-plugins-good
 */

// Importar bibliotecas
import processing.video.*;
import jp.nyatla.nyar4psg.*;
import java.util.HashSet;
import java.util.Arrays;

PupilDetector pup;        //importing the pupil detector class
Capture eyeCam;           //importing the camara capture
PImage img;               //for video streaming

void setup()
{
  //setting the size of the windows 640x480
  size(640, 480); 
  
  // Set sketch framerate ??
  frameRate(60);
  
  //initiation of the pupil detector object
  //param 1: threshold
  //param 2: minimum value of circumference
  //param 3: maximum value of circumference
  pup = new PupilDetector(0.01, 0.001, 0.005);
  
  // Get list of camera names
  String[] cams = getCameraNames();
  
  // Change camera order here
  String eye = cams[0];

  // Start eye camera
  eyeCam = new Capture(this, 640, 480, eye, 30);
  eyeCam.start();
}

void draw()
{
  // Read eye camera
  if (eyeCam.available())
  {
    eyeCam.read();
  }
  
  // Draw eye image
  image(eyeCam, 0, 0, eyeCam.width / 4.0, eyeCam.height / 4.0);
  
  // Draw pupil
  if(pup.detect(eyeCam))
  {
    noFill();
    strokeWeight(2);
    stroke(0, 255, 0);
    ellipse(pup.posX, pup.posY, pup.posR, pup.posR);
  }

   println("x:" + pup.posX + " y:" + pup.posY); //print the pupil position
}

/**
 * @brief get a list of the camera availables on the computer
*/
String[] getCameraNames()
{
  String[] list = Capture.list();
  for (int i=0; i < list.length; i++)
  {
    String[] chunks = split(list[i], ',');
    chunks = split(chunks[0], '=');
    list[i] = chunks[1];
  }
  String[] unique = new HashSet<String>(Arrays.asList(list)).toArray(new String[0]);
  return unique;
}
