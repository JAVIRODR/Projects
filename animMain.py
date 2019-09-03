
# Vizard anim code
  
import viz
import vizshape
import vizcam
import math

from anim import *

# set size (in pixels) and title of application window
viz.window.setSize( 1280, 720 )
viz.window.setName( "Mazinger Animation" )

# get graphics window
window = viz.MainWindow
# setup viewing volume

# set background color of window to blue 
viz.MainWindow.clearcolor( [0,0,150] ) 
viz.clearcolor(viz.SKYBLUE)
env = viz.add(viz.ENVIRONMENT_MAP,'sky.jpg')
sky = viz.add('skydome.dlc')
# Add piazza animations
#animations = viz.add('piazza_animations.osgb')
#below is the command for a sky box use if current map doesn't include one
sky.texture(env)



# allows mouse to rotate, translate, and zoom in/out on object
pivotNav = vizcam.PivotNavigate()
viz.MainView.setPosition([0,10,20])
viz.lookAt([0,10,0])
# Create Half-Lambert lighting model effect 
effect = vizfx.addLightingModel(diffuse=vizfx.DIFFUSE_HALFLAMBERT)

# Apply to default composer (replaces default lighting model effect)
vizfx.getComposer().addEffect(effect)
#posCam = vizcam.KeyboardPosCamera()
c = anim()

# render the scene in the window
viz.go()
