#!/usr/bin/env python
import roslib
roslib.load_manifest('opencv_fun')
import sys
import rospy
import cv2
import numpy as np, cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from kobuki_msgs.msg import ButtonEvent
from cv_bridge import CvBridge, CvBridgeError
import roslib
from std_msgs.msg import String
import roslib; roslib.load_manifest('sound_play')     
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from ar_track_alvar_msgs.msg import AlvarMarkers
from playsound import playsound
import threading
from threading import Thread
button = False
colorarr = False
#Flags for Sound Files
pikachu = False
mew = False
meowth = False
charmander = False
magikarp = False
squirtle = False
#Flags for Picture
mewS = False
meowthS = False
charmanderS = False
magikarpS = False
squirtleS = False
pikachushown = False
#Variables for text
drawT = False
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (50,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2


class image_converter:
  global move
  #Mehod no longer used to due issues with music running and preventing the rest of the program to work.
  def move():
	playsound('/home/turtlebot/catkin_ws/src/simple_pub_sub/src/oakHelloThere.wav')
	playsound('/home/turtlebot/catkin_ws/src/simple_pub_sub/src/PokeBotTheme.wav')   

  def __init__(self):
   #Subscribers
    self.image_pub = rospy.Publisher("image_topic_2",Image)
    self.ir_sub = rospy.Subscriber("/ar_pose_marker", AlvarMarkers, self.ir)
    self.button = rospy.Subscriber("/mobile_base/events/button", ButtonEvent, self.callback2)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback)

  def callback(self,data):
  #All the flags
    global button
    global colorarr
    global pikachu
    global pikachushown
    global font                 
    global bottomLeftCornerOfText 
    global fontColor             
    global lineType 
    global drawT
    global mew
    global meowth
    global charmander
    global magikarp
    global squirtle
    global mewS
    global meowthS
    global charmanderS 
    global magikarpS
    global squirtleS             
#Code for displaying windows and images
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
     
      

    except CvBridgeError as e:
      print(e)
    (rows,cols,channels) = cv_image.shape
	#Draws a new window next to the camera and displays a title screen. Didn't have time to implement a counter
	#A counter was meant to replace this screen after a pokemon was seen.
    if drawT == False:
	title = cv2.imread("titlescreen.jpg", cv2.IMREAD_COLOR)
    	cv2.imshow("Image window2", title)
    	cv2.moveWindow("Image window2",705,50)
	drawT = True

    elif pikachu == True and pikachushown == False:
    	pik = cv2.imread("pika.jpg", cv2.IMREAD_COLOR)
	(rows,cols,channels) = pik.shape
	img1 = cv_image
	img2 = pik
	#Combines two images together so they appear side by side in the same window until key is pressed. Code is repeated for each pokemon

	h1, w1 = img1.shape[:2]
	h2, w2 = img2.shape[:2]

	#create empty matrix
	vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

	#combine 2 images
	vis[:h1, :w1,:3] = img1
	vis[:h2, w1:w1+w2,:3] = img2
	#vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
	#Text telling the user to press a key is repeated for each pokemon
	cv2.putText(vis,'Press Any Key To Continue', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
	cv2.imshow("Image window", vis)
	
	cv2.waitKey(0)
	pikachushown=True
    elif mew == True and mewS == False:
    	pik = cv2.imread("mew.jpg", cv2.IMREAD_COLOR)
	(rows,cols,channels) = pik.shape
	img1 = cv_image
	img2 = pik

	h1, w1 = img1.shape[:2]
	h2, w2 = img2.shape[:2]

	#create empty matrix
	vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

	#combine 2 images
	vis[:h1, :w1,:3] = img1
	vis[:h2, w1:w1+w2,:3] = img2
	#vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

	cv2.putText(vis,'Press Any Key To Continue', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
	cv2.imshow("Image window", vis)
	
	cv2.waitKey(0)
	mewS=True
    elif magikarp == True and magikarpS == False:
    	pik = cv2.imread("magi.jpg", cv2.IMREAD_COLOR)
	(rows,cols,channels) = pik.shape
	img1 = cv_image
	img2 = pik

	h1, w1 = img1.shape[:2]
	h2, w2 = img2.shape[:2]

	#create empty matrix
	vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

	#combine 2 images
	vis[:h1, :w1,:3] = img1
	vis[:h2, w1:w1+w2,:3] = img2
	#vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

	cv2.putText(vis,'Press Any Key To Continue', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
	cv2.imshow("Image window", vis)
	
	cv2.waitKey(0)
	magikarpS=True
    elif meowth == True and meowthS == False:
    	pik = cv2.imread("meowth.jpg", cv2.IMREAD_COLOR)
	(rows,cols,channels) = pik.shape
	img1 = cv_image
	img2 = pik

	h1, w1 = img1.shape[:2]
	h2, w2 = img2.shape[:2]

	#create empty matrix
	vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

	#combine 2 images
	vis[:h1, :w1,:3] = img1
	vis[:h2, w1:w1+w2,:3] = img2
	#vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

	cv2.putText(vis,'Press Any Key To Continue', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
	cv2.imshow("Image window", vis)
	
	cv2.waitKey(0)
	meowthS=True
    elif charmander == True and charmanderS == False:
    	pik = cv2.imread("charmander.png", cv2.IMREAD_COLOR)
	(rows,cols,channels) = pik.shape
	img1 = cv_image
	img2 = pik

	h1, w1 = img1.shape[:2]
	h2, w2 = img2.shape[:2]

	#create empty matrix
	vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

	#combine 2 images
	vis[:h1, :w1,:3] = img1
	vis[:h2, w1:w1+w2,:3] = img2
	#vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

	cv2.putText(vis,'Press Any Key To Continue', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
	cv2.imshow("Image window", vis)
	
	cv2.waitKey(0)
	charmanderS=True
    elif squirtle == True and squirtleS == False:
    	pik = cv2.imread("Squirtle.png", cv2.IMREAD_COLOR)
	(rows,cols,channels) = pik.shape
	img1 = cv_image
	img2 = pik

	h1, w1 = img1.shape[:2]
	h2, w2 = img2.shape[:2]

	#create empty matrix
	vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

	#combine 2 images
	vis[:h1, :w1,:3] = img1
	vis[:h2, w1:w1+w2,:3] = img2
	#vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

	cv2.putText(vis,'Press Any Key To Continue', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
	cv2.imshow("Image window", vis)
	
	cv2.waitKey(0)
	squirtleS=True
    elif squirtle == True and charmander == True and meowth == True and magikarp == True and pikachu == True and mew == True:
     	 pik = cv2.imread("youwin.jpg", cv2.IMREAD_COLOR)
	 cv2.imshow("Image window", pik)
	 cv2.waitKey(0)	


	#Title screen is displayed in a second window due to the fact that combining it with the camera window	
	#would cause the frame rate to lower. So this work-around was done
    title = cv2.imread("titlescreen.jpg", cv2.IMREAD_COLOR)

    cv2.imshow("Image window", cv_image)
    cv2.moveWindow("Image window",50,50)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)
	#Unused method left over from image_fun.py
  def callback2(self, state):
	global button
	if state.button == 0 and state.state == 1 and button == False:
		button = True
	elif state.button == 0 and state.state == 1 and button == True:
		button = False
  def ir(self, state):
  #code for detecting AR Markers
	global pikachu
    global mew
    global meowth
   	global charmander
   	global magikarp
    global squirtle
	
# Flag Checker sets boolean to true when pokemon was seen and plays sound of pokemon.
# IDs are widely different numbers because these would read the best during our testing phase.
	if len(state.markers) != 0:
		if state.markers[0].id == 7 and pikachu == False:
			print("You caught Pikachu!")
			playsound('/home/turtlebot/catkin_ws/src/simple_pub_sub/src/pikachu1.wav') 
			pikachu = True
		elif state.markers[0].id == 6 and mew == False:
			print("You caught Mew!")
			playsound('/home/turtlebot/catkin_ws/src/simple_pub_sub/src/mew2.wav') 
			mew = True 
		elif state.markers[0].id == 5 and meowth == False:
			print("You caught Meowth!")
			playsound('/home/turtlebot/catkin_ws/src/simple_pub_sub/src/meowth1.wav') 
			meowth = True 
		elif state.markers[0].id == 11 and magikarp == False:
			print("You caught Magikarp!")
			playsound('/home/turtlebot/catkin_ws/src/simple_pub_sub/src/magikarp.wav') 
			magikarp = True 
		elif state.markers[0].id == 1 and charmander == False:
			print("You caught Charmander!")
			playsound('/home/turtlebot/catkin_ws/src/simple_pub_sub/src/charmander2.wav') 
			charmander = True 
		elif state.markers[0].id == 2 and squirtle == False:
			print("You caught Squirtle!")
			playsound('/home/turtlebot/catkin_ws/src/simple_pub_sub/src/squirtle.wav') 
			squirtle = True  
	
def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()
  

if __name__ == '__main__':
    main(sys.argv)
   
