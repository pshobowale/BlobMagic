from ursina import *


app = Ursina()  # create the game

blob = []

Light(type='ambient', color=(0.5,0.5,0.5,1)) 
Light(type='directional', color=(0.4,0.4,0.4,1)) # dim full spectrum
#Light(type='directional', color=(1,1,1,0.4), direction=(0,0,0))  # dim full spectrum

#Entity(model="xyplane",scale=(2.5,1,2.5))
blob.append(Entity(model="blob", color=(0,0.5,1,1),position=(0,0.125,0),scale=(0.1,0.1,0.1)))
blob.append(Entity(model="sphere",color=(0,0,0,1),position=(0.03,0.3,-0.1),scale=(0.03,0.03,0.03)))
blob.append(Entity(model="sphere",color=(0,0,0,1),position=(-0.03,0.3,-0.1),scale=(0.03,0.03,0.03)))
#blob.append(Entity(model="sphere",color=(0,0,0,1)))



def update():
    pass
    #for i in blob:
    #    i.rotation_y += 3
EditorCamera()
app.run()   # opens a window and starts the game.
