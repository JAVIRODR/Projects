# maze.py starter Code

import viz
import vizfx
import vizshape
import vizcam
import math
import vizact
from Model import *

# An instance of this class adds a maze to the scene along with 
# an avatar that can be navigated through it.
class anim(viz.EventClass):

	# Constructor 
	def __init__(self):
		# base class constructor 
		viz.EventClass.__init__(self)
		self.model = viz.addChild('piazza.osgb')

		# set up keyboard and timer callback methods
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		self.callback(viz.MOUSEDOWN_EVENT,self.onMouseDown)
		#booleans for video
		self.check1 = False
		#avatar's postion and rotation angle
		self.x = 0.5
		self.z = 0.5
		#counts for animaions
		self.count = 0.0
		self.count2 = 0.0
		self.theta = 0
		#inserting avater
		
		self.avatar = vizfx.addAvatar('mazinger/mazinger.cfg')
		self.avatar.state(0)
		#translating avatar to correct position
		mat = viz.Matrix()
		#mat.postAxisAngle(0,1,0,self.theta)
		mat.postTrans(0,7,0);
		self.avatar.setMatrix(mat)
		self.callback(viz.TIMER_EVENT,self.onTimer)
	
		#mazin.addAction(spin)
		#Music
		
		#add ground
		grass = viz.addTexture('images/tile_grass.jpg', wrap=viz.REPEAT)

		#Add the terrain using the infinte terrain plug-in.
		#terrain = viz.add('InfiniteTerrain.dlc',6,'456',7,6,15000,0.0005)
		
		#Texture the terrain.
		#terrain.texture(grass)
		#alternate ground object
		#self.ground = viz.addChild('ground.osgb')			
	# Key pressed down event code currently changes state of avatar manually .
	def onKeyDown(self,key):
		if key == '1':
			self.avatar.stopAction(1)
			self.avatar.state(0)
		elif key == "2":
			self.avatar.state(1)
		elif key == "3":
			mySound = viz.addAudio( 'mazin.mp3' )
			mySound.loop( viz.ON )
			mySound.play()
			#self.avatar.execute(1)
			#opening video test
			#title text
			self.textScreen = viz.addText('Mazinger Animation Demo',viz.SCREEN)
			#self.textScreen.alignment(viz.ALIGN_CENTER_BOTTOM)
			self.textScreen.setScale([1,1,1])
			#self.textScreen.setPosition([0,10,0])
			self.starttimer(2,1,22)
			self.object = viz.addTexQuad(size=2)
			video = viz.addVideo('open.avi')
			video.setRate(1)
			video.volume(0) 
			video.play()
			#fixing video position
			self.object.texture(video)
			self.object.setAxisAngle( [0, 1, 0 , 180] ) 
			self.object.setPosition([0,10,18])
			
			#self.avatar.setAnimationSpeed(1, .5) #run at half speed
		elif key == "4":
			viz.MainView.setPosition([0,10,20])
			viz.lookAt([0,10,0])
			self.starttimer(1,1,8)
			self.avatar.execute(2)
			
	
	

	# Adds coodinate system that originates at (0,0,0) and extends
	# down the +x, +y, and +z directions.  Locations 1 and 2 units
	# in each direction are marked on the axis.
	def addCoordinateAxes(self):
		viz.startLayer(viz.LINES)
		viz.linewidth(7)
		viz.vertexColor( viz.RED )
		# positive y axis
		viz.vertex(0,0,0); 	   viz.vertex(0,20,0)
		#positive x axis
		viz.vertex(0,0,0); 	   viz.vertex(20,0,0)
		#positive z axis
		viz.vertex(0,0,0); 	   viz.vertex(0,0,20)
		#y=1 tick mark
		viz.vertex(-0.25,1,0); viz.vertex(0.25,1,0)
		#y=2 tick mark
		viz.vertex(-0.25,2,0); viz.vertex(0.25,2,0)
		#x=1 tick mark
		viz.vertex(1,0,-.25);  viz.vertex(1,0,.25)
		#x=2 tick mark
		viz.vertex(2,0,-.25);  viz.vertex(2,0,+.25)
		#z=1 tick mark
		viz.vertex(-.25,0,1);  viz.vertex(.25,0,1)
		#z=2 tick mark
		viz.vertex(-.25,0,2);  viz.vertex(.25,0,2)
		viz.endLayer()
	def onMouseDown(self,button):
		x=0
	def onTimer(self,num):
		#animation for flight
		if num == 1:
			self.count2 = self.count2+1
			print(self.count2)
			if self.count2 == 1:
				
				viz.MainView.runAction(vizact.move([0,1,0],2))
			elif self.count2 == 2:
				
				viz.MainView.runAction(vizact.move([0,0,-1],3))
			elif self.count2 == 5:
				x=0
				viz.MainView.runAction(vizact.spinTo(point=[0,30,0],time=2))
			elif self.count2 == 9:
				#end of flight or state 2
				self.avatar.stopAction(2)
				self.avatar.state(0)
				viz.MainView.setPosition([0,10,20])
				viz.lookAt([0,10,0])
				self.object2 = viz.addTexQuad(size=10)
				self.object = viz.addTexQuad(size=2)
				self.object2.setPosition([0,10,17])
				video = viz.addVideo('fly2.avi')
				video.setRate(1)
				video.volume(0) 

				video.play()
				self.object.texture(video)
				self.object.setAxisAngle( [0, 1, 0 , 180] ) 
				self.object.setPosition([0,10,18])
				#destroy stage for illusion flightand start next state
				self.model.remove()
				self.avatar.state(3)

				#start next part and reset cound
				self.count2 = 0
				self.starttimer(3,1,28)
		elif num == 2:
			#start of animation
			self.count = self.count +1
			print(self.count)
			if self.count == 17:
				self.textScreen.remove()
				self.object.remove()
				self.avatar.state(1)
			elif self.count == 20:
				self.avatar.stopAnimation(1)
			elif self.count == 22:
				#start flight
				self.starttimer(1,1,8)
				self.avatar.execute(2)
		elif num == 3:
			self.count2 = self.count2 + 1
				

			if self.count2 == 9:
				#adding last stage
				viz.MainView.runAction(vizact.move([0,0,-1],7))
				self.object3 = viz.addTexQuad(size=55)
				video = viz.addVideo('skyanim.avi')
				video.setRate(1)
				video.volume(0) 
				video.play()
				video.loop()
				#fixing video position
				self.object3.texture(video)
				self.object3.setAxisAngle( [0, 1, 0 , 180] ) 
				self.object3.setPosition([0,10,-10])
				self.object4 = viz.addTexQuad(size=50)
				
				self.object4.setPosition([0,10,-11])
				self.object.remove()
				self.object2.remove()
				

		
		
					
		

