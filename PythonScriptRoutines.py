#Author: Nicholas Hickey
#IMD 3002 
#Assignment 03



import maya.cmds as cmds
import random as rnd


if 'myWin' in globals():
    if cmds.window(myWin, exists= True):
        cmds.deleteUI(myWin, window= True)
myWin = cmds.window(title='Nicholas Hickey: LEGO Assignment', menuBar= True)


#Used to create the tabs
ProjTabs = cmds.tabLayout()

#STANDARD BLOCK
tab1 = cmds.frameLayout(collapsable= True, label='Standard Block', width=475, height=140) 
cmds.columnLayout()
cmds.intSliderGrp('blockHeight', l='Height', f= True, min=1, max=20, value=3)
cmds.intSliderGrp('blockWidth', l='Width (Bumps)', f= True, min=1, max=20, value=2)
cmds.intSliderGrp('blockDepth', l='Length', f= True, min=1, max=20, value=8)
cmds.colorSliderGrp('blockColour', label='Colour', hsv=(38, 1, 1))
cmds.columnLayout()
cmds.button(label='Create Block', command=('basicBlock()'))
cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')

#BLOCK HOLES
tab2 = cmds.frameLayout(collapsable= True, label='Blocks with Holes', width= 475, height= 140)
cmds.columnLayout()
cmds.intSliderGrp('blockWidth3', l='Width', f= True, min= 1, max= 20, value= 2)
cmds.intSliderGrp('blockDepth3', l='Length', f= True, min= 1, max= 20, value= 8)
cmds.colorSliderGrp('blockColour3', label='Colour', hsv=(1, 257, 1))
cmds.columnLayout()
cmds.button(label='Create Block', command=('BlockWithHoles()'))
cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')

#ROUNDED HOLES
tab3 = cmds.frameLayout(collapsable=True, label='Rounded Blocks with Holes', width=475, height=140)
cmds.columnLayout()
cmds.intSliderGrp('blockDepth2', l='Length (HOLES)', f= True, min= 1, max= 20, value= 8)
cmds.colorSliderGrp('blockColour2', label='Colour', hsv=(128, 1, 1))
cmds.columnLayout()
cmds.button(label='Create Block', command=('RoundedBlock()'))
cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')

#ROUNDED ANGLE
tab4 = cmds.frameLayout(collapsable= True, label='Rounded Blocks with Holes  at Angle', width=475, height=180)
cmds.columnLayout()
cmds.intSliderGrp('AngleblockDepth', l='Non Angle Length (HOLES)', f= True, min=1, max=20, value=8)
cmds.intSliderGrp('AngleTopLength', l='Angle Top Length (HOLES)', f= True, min=1, max=20, value=8)
cmds.colorSliderGrp('AngleblockColour', label='Colour', hsv=(60, 12, 200))
cmds.columnLayout()
#First and second fucntions for each angle 90 and 45
cmds.button(label='Create 90 Degree Block', command=('RoundedBlockAngle()'))
cmds.button(label='Create 45 Degree Block', command=('RoundedBlockAngle45()'))
cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')

#AXEL
tab5 = cmds.frameLayout(collapsable= True, label='Axel', width=475, height=90)
cmds.columnLayout()
cmds.intSliderGrp('AxelLength', l='Length', f= True, min=1, max=20, value=3)
cmds.colorSliderGrp('AxelColour', label='Colour', hsv=(257, 1, 1))
cmds.columnLayout()
cmds.button(label='Create Axel', command=('Axel()'))
cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')

#WHEEL AND RIM
tab6 = cmds.frameLayout(collapsable=True, label='Wheels', width=475, height=120)
cmds.columnLayout()
cmds.intSliderGrp('WheelHeight', l='Wheel Size', f= True, min=1, max=20, value=3)
cmds.colorSliderGrp('WheelColour', l='Wheel Colour', hsv=(12, 1, 1))
cmds.colorSliderGrp('RimColour', l='Rim Colour', hsv=(176, 1, 1))
cmds.columnLayout()
cmds.button(label='Create Wheel', command=('wheels()'))
cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')

#Set the tab names
cmds.tabLayout( ProjTabs, edit=True, tabLabel=((tab1, 'Standard Block'), (tab2, 'Blocks with Holes'), (tab3, 'Rounded Blocks with Holes'), (tab4, 'Rounded Blocks with Holes  at Angle'), (tab5, 'Axel'), (tab6, 'Wheels')) )

cmds.showWindow(myWin)


#BASIC BLOCK FUNCTION
def basicBlock():
    
    
    #Initialize my block variables to the GUI inputs
    blockHeight = cmds.intSliderGrp('blockHeight', q = True, v= True)
    blockWidth = cmds.intSliderGrp('blockWidth', q   = True, v= True)
    blockDepth = cmds.intSliderGrp('blockDepth', q   = True, v= True)
    
    rgb = cmds.colorSliderGrp('blockColour', q = True, rgbValue = True)
    nsTmp = "Block" + str(rnd.randint(1000, 9999))
    
    cmds.select(clear  = True)
    cmds.namespace(add = nsTmp)
    cmds.namespace(set = nsTmp)
    
    #Set my cubeSize variables to the user inputs scaled
    cubeSizeX = blockWidth * 0.8
    cubeSizeY = blockHeight * 0.32
    cubeSizeZ = blockDepth * 0.8
    
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    
    #loop through width then depth to set the correct number of bumps and create the cyliners, then moving them to the proper location
    cmds.move((cubeSizeY / 2.0), moveY = True)
    for i in range(blockWidth):
        for j in range(blockDepth):
            cmds.polyCylinder(r=0.25, h=0.20)
            cmds.move((cubeSizeY + 0.10), moveY = True, a = True)
            cmds.move(((i * 0.8) - (cubeSizeX / 2.0) + 0.4), moveX = True, a = True)
            cmds.move(((j * 0.8) - (cubeSizeZ / 2.0) + 0.4), moveZ = True, a = True)
            
    myShader = cmds.shadingNode('lambert', asShader= True, name='blckMat')
    
    cmds.setAttr(nsTmp + ':blckMat.color', rgb[0], rgb[1], rgb[2], typ='double3')  
    cmds.polyUnite((nsTmp + ':*'), n=nsTmp, ch = False)
    cmds.delete(ch = True)   
    cmds.hyperShade(assign=(nsTmp + ':blckMat'))
    cmds.namespace(removeNamespace=':' + nsTmp, mergeNamespaceWithParent = True)    

#ROUNDED BLOCK FUCNTION
def RoundedBlock():
    
    #Initialize all my varibales to the GUI inputs
    blockHeight = 3
    blockWidth  = 2
    blockDepth  = cmds.intSliderGrp('blockDepth2', q = True, v= True)
    
    rgb = cmds.colorSliderGrp('blockColour2', q = True, rgbValue = True)
    nsTmp = "Block" + str(rnd.randint(1000, 9999))
    
    cmds.select(clear  = True)
    cmds.namespace(add = nsTmp)
    cmds.namespace(set = nsTmp)
    
    #Set all my cube varibales to the user inputs scaled
    cubeSizeX     = blockWidth * 0.8
    cubeSizeY     = blockHeight * 0.32
    cubeSizeZ     = blockDepth * 0.8
    halfCubeSizeY = cubeSizeY * 0.5
    
    #Created my cube and beveled in outter edges to create a rounded appearance 
    cube1=cmds.polyCube(h=cubeSizeY, w=0.5, d=cubeSizeZ)
    cmds.polyBevel(cube1[0]+'.e[0:3]',segments=20,offset=0.4)
    cmds.move((cubeSizeY / 2.0), moveY=True)


    #loop through depth and place the first set of holes for the cube
    for l in range(blockDepth):
        holes = cmds.polyCylinder(r=0.25, h=cubeSizeX+.50,sx=70)
        cmds.move((halfCubeSizeY), moveY= True, a= True)
        cmds.move(((l * 0.8) - (cubeSizeZ / 2.0) + 0.4), moveZ= True, a= True) 
        cmds.rotate(0,0,'90deg', r= True)
        cube1 = cmds.polyBoolOp( cube1[0],holes[0], op=2)
     
    myShader = cmds.shadingNode('lambert', asShader= True, name='blckMat')
    cmds.setAttr(nsTmp + ':blckMat.color', rgb[0], rgb[1], rgb[2], typ='double3')
    cmds.select(cube1)
    cmds.delete(ch= True)   
    cmds.hyperShade(assign=(nsTmp + ':blckMat')) 
    cmds.namespace(set=':')  
    cmds.namespace(removeNamespace=':' + nsTmp, mergeNamespaceWithParent= True)

#ROUNDED BLOCK ANGLE FUNCTION 
def RoundedBlockAngle():
    
    
    #Initialize all my block variable to the user input
    blockHeight = 3
    blockWidth  = 2
    blockDepth  = cmds.intSliderGrp('AngleblockDepth', q  = True, v = True) 
    blockTop    = cmds.intSliderGrp('AngleTopLength', q   = True, v = True)
    rgb         = cmds.colorSliderGrp('AngleblockColour', q= True, rgbValue= True)
    nsTmp       = "Block" + str(rnd.randint(1000, 9999)) 
   
    cmds.select(clear= True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp) 
    
    #Set all my cube varibales to the user inputs scaled
    cubeSizeX     = blockWidth  * 0.8
    cubeSizeY     = blockHeight * 0.32
    cubeSizeZ     = blockDepth  * 0.8
    cubeSizeTop   = blockTop   * 0.8
    halfCubeSizeY = cubeSizeY * 0.5
 
    #Created my cube and beveled in outter edges to create a rounded appearance
    cube1=cmds.polyCube(h=cubeSizeY, w=0.5, d=cubeSizeZ)
    cmds.polyBevel(cube1[0]+'.e[0:3]',segments=20,offset=0.4)
    cmds.move((cubeSizeY / 2.0), moveY=True)

    #loop through depth and place the first set of holes for object 1
    for l in range(blockDepth):
        holes = cmds.polyCylinder(r=0.25, h=cubeSizeX+.50,sx=70)
        cmds.move((halfCubeSizeY), moveY= True, a= True)
        cmds.move(((l * 0.8) - (cubeSizeZ / 2.0) + 0.4), moveZ= True, a= True) 
        cmds.rotate(0,0,'90deg', r= True)
        cube1 = cmds.polyBoolOp( cube1[0],holes[0], op=2)
    
    cube2= cmds.polyCube(h=cubeSizeY, w=0.5, d=cubeSizeTop)

    cmds.polyBevel(cube2[0]+'.e[0:3]',segments=20,offset=0.4)     
    cmds.move((cubeSizeY / 2.0), moveY=True)
    
    #loop through top length and place the first set of holes for object 2      
    for z in range(blockTop):
        holes2 = cmds.polyCylinder(r=0.25, h=cubeSizeX+.50,sx=70)
        cmds.move((halfCubeSizeY), moveY= True, a= True)
        cmds.move(((z * 0.8) - (cubeSizeTop / 2.0) + 0.4), moveZ= True, a= True) 
        cmds.rotate(0,0,'90deg', r= True)
        cube2 = cmds.polyBoolOp( cube2[0],holes2[0], op=2)       

    #Rotate and move the cube to match exactly   
    cube2 = cmds.rotate('90deg', 0, 0, r = True)
    cube2 = cmds.move((cubeSizeTop / 2.0) + 0.1, moveY=True)
    cube2= cmds.move((cubeSizeZ / - 2.0) - 0.1, moveZ = True)  
    #cube2 = cmds.polyBoolOp(cube2[0], cube1[0], op=2)
    myShader = cmds.shadingNode('lambert', asShader = True, name='blckMat')  
    cube2 = cmds.polyUnite((nsTmp +':*'), n = nsTmp, ch=False)
    cmds.setAttr(nsTmp + ':blckMat.color', rgb[0], rgb[1], rgb[2], typ='double3')
    cmds.delete(ch = True)   
    cmds.hyperShade(assign=(nsTmp + ':blckMat')) 
    cmds.namespace(set=':')  
    cmds.namespace(removeNamespace=':' + nsTmp, mergeNamespaceWithParent = True)
    
 
#ROUNDED BLOCK ANGLE 45 FUCNTION
def RoundedBlockAngle45():
    
    
    #Initialize all my block variable to the user input    
    blockHeight = 3
    blockWidth  = 2
    blockDepth  = cmds.intSliderGrp('AngleblockDepth', q  = True, v = True) 
    blockTop    = cmds.intSliderGrp('AngleTopLength', q   = True, v = True)
    rgb = cmds.colorSliderGrp('AngleblockColour',     q   = True, rgbValue= True)
    nsTmp = "Block" + str(rnd.randint(1000, 9999))
    
    cmds.select(clear  = True)
    cmds.namespace(add = nsTmp)
    cmds.namespace(set = nsTmp)
    
    #set all my variables to the user input values scaled
    cubeSizeX   = blockWidth  * 0.8
    cubeSizeY   = blockHeight * 0.32
    cubeSizeZ   = blockDepth  * 0.8
    cubeSizeTop = blockTop   * 0.8
    halfCubeSizeY = cubeSizeY * 0.5
    
    #Created my cube and beveled in outter edges to create a rounded appearance
    cube1=cmds.polyCube(h=cubeSizeY, w=0.5, d=cubeSizeZ)
    cmds.polyBevel(cube1[0]+'.e[0:3]',segments=20,offset=0.4)
    
    cmds.move((cubeSizeY / 2.0), moveY = True)
    
    #loop through depth and place the first set of holes for object 1
    for l in range(blockDepth):
        holes = cmds.polyCylinder(r= 0.25, h = cubeSizeX + 10, sx = 70)
        cmds.move((halfCubeSizeY), moveY = True, a = True)
        cmds.move(((l * 0.8) - (cubeSizeZ / 2.0) + 0.4), moveZ = True, a = True) 
        cmds.rotate(0,0,'90deg', r = True)
        cube1 = cmds.polyBoolOp( cube1[0],holes[0], op=2)
     
     
    cube2= cmds.polyCube(h=cubeSizeY, w=0.5, d=cubeSizeTop)   
    cmds.polyBevel(cube2[0]+'.e[0:3]',segments=20,offset=0.4)  
    
    cmds.move((cubeSizeY / 2.0), moveY = True)
    
    #loop through top length and place the first set of holes for object 2   
    for z in range(blockTop):
        holes2 = cmds.polyCylinder(r= 0.25,  h = cubeSizeX + 10, sx = 70)
        cmds.move((halfCubeSizeY), moveY = True, a = True)
        cmds.move(((z * 0.8) - (cubeSizeTop / 2.0) + 0.4), moveZ = True, a = True) 
        cmds.rotate(0,0,'90deg', r = True)
        cube2 = cmds.polyBoolOp( cube2[0],holes2[0], op=2)      

    #Change pivot point of the second cube that is rotating
    cube2 = cmds.move(0, 0, cubeSizeTop/2.0, cube2[0] + ".scalePivot", cube2[0] + ".rotatePivot", absolute=True)
    #Rotate the cubeand move it to match exactly
    cube2 = cmds.rotate('45deg', 0, 0, r = True)
    cmds.move( -0.13, moveY = True)
    cmds.move((cubeSizeZ/-2.0)-(cubeSizeTop/2.0) + 0.35, moveZ = True)
    myShader = cmds.shadingNode('lambert', asShader = True, name='blckMat')
    cube2 = cmds.polyUnite((nsTmp +':*'), n = nsTmp, ch=False)
    
    cmds.setAttr(nsTmp + ':blckMat.color', rgb[0], rgb[1], rgb[2], typ='double3')
    cmds.delete(ch = True)   
    cmds.hyperShade(assign=(nsTmp + ':blckMat')) 
    cmds.namespace(set=':')  
    cmds.namespace(removeNamespace=':' + nsTmp, mergeNamespaceWithParent= True)
        

#BASIC BLOCK WITH HOLES
def BlockWithHoles():
    
    
    #Initialize variables to the user inputted values
    blockHeight = 3
    blockWidth  = cmds.intSliderGrp('blockWidth3', q = True, v = True)
    blockDepth  = cmds.intSliderGrp('blockDepth3', q = True, v = True)   
    rgb = cmds.colorSliderGrp('blockColour3',  q = True, rgbValue = True)
    nsTmp = "Block" + str(rnd.randint(1000, 9999))    
    cmds.select(clear  = True)
    cmds.namespace(add = nsTmp)
    cmds.namespace(set = nsTmp)
    
    #Set cubeSize variables and a second variable for half the size for easy moving or translation
    cubeSizeX     = blockWidth * 0.8
    cubeSizeY     = blockHeight * 0.32
    cubeSizeZ     = blockDepth * 0.8
    halfCubeSizeY = cubeSizeY * 0.5   
    finalBlock    = cmds.polyCube(height = cubeSizeY, width = cubeSizeX, depth = cubeSizeZ)
    cmds.move((cubeSizeY / 2.0), moveY = True)
    
    #Adding the top bumps based on a double for loop first looping through the block width then depth, created the cylinders or bumps within the loop and move them to the correct spots.
    for i in range (blockWidth):
        for j in range (blockDepth):
            cmds.polyCylinder(r= 0.25, h = 0.20)
            cmds.move((cubeSizeY + 0.10), moveY = True, a = True)
            cmds.move(((i * 0.8) - (cubeSizeX / 2.0) + 0.4), moveX = True, a = True)
            cmds.move(((j * 0.8) - (cubeSizeZ / 2.0) + 0.4), moveZ = True, a = True)    
     
    #Execute this loop at -1 so one less hole gets drawn compared to bumps, to allow for the holes to then be centered between two bumps, then created the cutout cylinders and size. 
    #Next moved the cylinders to the correct spot and rotated to alligh correctly with the width of the block. BoolOperation 2 to remove the holes from the block.      
    for z in range (blockDepth - 1):
        #Had to increase x subdivisions to 130 for when the length goes past 8
        cutOuts = cmds.polyCylinder(radius = 0.25, height = cubeSizeX + 10, sx = 130)
        cmds.move((halfCubeSizeY), moveY = True, a = True)
        cmds.move(((z * 0.8) - (cubeSizeZ / 2.0) + 0.8), moveZ = True, a = True)        
        cmds.rotate(0,0,'90deg', r = True)
        finalBlock = cmds.polyBoolOp( finalBlock[0], cutOuts[0], op = 2)
  
    myShader = cmds.shadingNode('lambert', asShader = True, name='blckMat')  
    cmds.setAttr(nsTmp + ':blckMat.color', rgb[0], rgb[1], rgb[2], typ='double3')  
    cmds.polyUnite((nsTmp + ':*'), n=nsTmp, ch = False)
    cmds.delete(ch = True)   
    cmds.hyperShade(assign=(nsTmp + ':blckMat'))
    cmds.namespace(removeNamespace=':' + nsTmp, mergeNamespaceWithParent = True) 

#AXEL FUCNTION    
def Axel():

    
    #Set axel length to the user input value from the GUI
    AxelLength = cmds.intSliderGrp('AxelLength', q = True, v = True)
    rgb = cmds.colorSliderGrp('AxelColour', q = True, rgbValue = True)
    nsTmp = "Block" + str(rnd.randint(1000,9999))
    
    cmds.select(clear  = True)
    cmds.namespace(add = nsTmp)
    cmds.namespace(set = nsTmp)
    
    #Set radius and length variables
    radius = 0.25
    length = AxelLength
    
    #Axel 1 creation using bevel to curve the edges in 
    axel1    = cmds.polyCube(height = length, width = 0.50, depth = 0.1)
    cmds.polyBevel(axel1[0]+'.e[6:7]',segments = 5,offset=0.05)
    cmds.polyBevel(axel1[0]+'.e[4:5]',segments = 5,offset=0.05)

    cmds.rotate(90, y = True) 
    
    #Axel 2 creation using a bevel to curve the specific edges in
    axel2    = cmds.polyCube(height = length, width = 0.50, depth = 0.1)
    cmds.polyBevel(axel2[0]+'.e[6:7]',segments = 5,offset=0.05)
    cmds.polyBevel(axel2[0]+'.e[4:5]',segments = 5,offset=0.05)
    
    myShader = cmds.shadingNode('lambert', asShader= True, name='blckMat')
    cmds.setAttr(nsTmp + ':blckMat.color', rgb[0], rgb[1], rgb[2], typ='double3')
    

    cmds.polyUnite((nsTmp + ':*'), n=nsTmp, ch = False)
    cmds.delete(ch= True)   
    cmds.hyperShade(assign=(nsTmp + ':blckMat')) 
    cmds.namespace(set=':')  
    cmds.namespace(removeNamespace=':' + nsTmp, mergeNamespaceWithParent= True)
    

#WHEEL AND RIMS FUCNTION
def wheels():
    
    
    #Initialize my wheel vriables to the user input to the GUI
    WheelHeight = cmds.intSliderGrp('WheelHeight',q = True, v = True)
    WheelWidth  = 2
    
    rgb = cmds.colorSliderGrp('WheelColour',  q = True, rgbValue = True)
    rgb2 = cmds.colorSliderGrp('RimColour',  q = True, rgbValue = True)
    nsTmp = "Block" + str(rnd.randint(1000, 9999))
    
    cmds.select(clear  = True)
    cmds.namespace(add = nsTmp)
    cmds.namespace(set = nsTmp)
    
    #two rotations for each tread
    treadRotA   = 0
    treadRotB   = 7.4
    treadNumber = 24
    
    #Initialize all my variables and scaling values to allow the tire to be scaled based on the user input but keep the same ratios.
    cubeSizeY   = WheelHeight * 0.32
    cubeSizeX   = WheelWidth * 0.8
    rimHeight   = WheelHeight / 2.0
    rimRadius   = WheelHeight / 5.0
    wheelW      = WheelHeight / 14.0
    wheelD      = WheelHeight / 5.0
    moveZ       = WheelHeight / 5.0
    moveZ2      = WheelHeight / 10.0

    #Loop throught the amount of tread I decided on (24), place a cube scale it rotate and repeat
    #In the process i increment the rotation so the next piece in the loop is drawn correct then i bool op the middle drum spacing from the cubes
    for i in range(treadNumber):
        tread1 = cmds.polyCube(h = WheelHeight, w = wheelW, d = wheelD)
        cmds.rotate( 0, 0, treadRotA, tread1, pivot=(0, 0, 1) )
        treadRotA = treadRotA + 15
        cutOut = cmds.polyCylinder( sh = 10, h = rimHeight, r = rimRadius)
        cmds.move( moveZ2, z   = True)
        cmds.rotate(90, x = True)
        tread1 = cmds.polyBoolOp(tread1[0], cutOut[0], op=2)
        
    #Same process as above loop but ofset rotation at the start to create a checkerboard like tread for the tire. 
    for z in range(treadNumber):
        tread2 = cmds.polyCube(h = WheelHeight, w = wheelW, d = wheelD)
        cmds.rotate( 0, 0, treadRotB, tread2, pivot=(0, 0, 1) )
        cmds.move( moveZ, z = True)
        treadRotB = treadRotB + 15    
        cutOut2 = cmds.polyCylinder( sh = 10, h = rimHeight, r = rimRadius)
        cmds.move( moveZ2, z   = True)
        cmds.rotate(90, x = True)
        tread2 = cmds.polyBoolOp(tread2[0], cutOut2[0], op=2)

    #Creating a second pipe to make the tread less grooved per say. Essentially makes a pipe to create a more realistic looking tire with smaller tread opposed to all tread without the pipe.
    wheelThickness = cmds.polyPipe(sh=2, h = WheelHeight * 0.8 , r = rimRadius * 2.2, t = rimRadius)
    wheelThickness = cmds.move(wheelD/2 , z = True)   
    wheelThickness = cmds.rotate(90, x = True) 

    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    myShader2 = cmds.shadingNode('lambert', asShader=True, name="blckMat2") 
    cmds.polyUnite((nsTmp + ':*'), n=nsTmp, ch = False)   
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cmds.setAttr(nsTmp+":blckMat2.color",rgb2[0],rgb2[1],rgb2[2], typ='double3')
    cmds.delete(ch = True)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    #RIM CREATION
    rim = cmds.polyCylinder( sh = 10, h = rimHeight * 0.5, r = rimRadius)
    cmds.move(wheelD/2 , z = True)  
    cmds.rotate(90, x = True) 
    
    #RIM CUTOUT1
    rimCutOut  = cmds.polyCube(height = 10, width = 0.25, depth = 0.1)  
    cmds.move(wheelD/2 , z = True) 
    cmds.rotate(90, x = True) 
    rim = cmds.polyBoolOp(rim[0], rimCutOut[0], op=2) 

    #RIM CUTOUT2 
    rimCutOut2  = cmds.polyCube(height = 10, width = 0.25, depth = 0.1)  
    cmds.move(wheelD/2 , z = True) 
    cmds.rotate(90, x = True)
    cmds.rotate(90, z = True) 
    rim = cmds.polyBoolOp(rim[0], rimCutOut2[0], op=2) 


    cmds.hyperShade(assign=(nsTmp+":blckMat2"))   
    cmds.polyUnite((nsTmp + ':*'), n=nsTmp, ch = False)     
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent = True)     

