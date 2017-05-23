from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

black = Color(0x000000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
red = Color(0xff0000, 1.0)
brown = Color(0xD2691E, 1.0)
thinline = LineStyle(2, black)

#randoms
loglength = random.randint(2,10)
carspeed = random.randint(0,15)/10

black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, thinline, green)
bg = Sprite(bg_asset, (0,0))
lives = 3
class Road(Sprite):
    road = RectangleAsset(800, 250, thinline, black)
    def __init__(self, x, y):
        super().__init__(Road.road, (x, y))
        self.x = x
        self.y = y
        
class Water(Sprite):
    water = RectangleAsset(800, 250, thinline, blue)
    def __init__(self, x, y):
        super().__init__(Water.water, (x, y))
        self.x = x
        self.y = y

class Car(Sprite):
    car = RectangleAsset(20, 20, thinline, green)
    def __init__(self, x, y):
        super().__init__(Car.car, (x, y))
        self.x = x
        self.y = y

class Log(Sprite):
    global loglength
    log = RectangleAsset(20, 20*loglength, thinline, brown)
    def __init__(self, x, y):
        super().__init__(Log.log, (x, y))
        self.x = x
        self.y = y


        
class Frog(Sprite):
    frog = RectangleAsset(15, 15, thinline, red)
    def __init__(self, x, y):
        super().__init__(Frog.frog, (x, y))
        self.x = x
        self.y = y

class Frogger(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        #start#
        self.listenKeyEvent('keydown', 's', self.go)
        #movement keys#
        self.listenKeyEvent('keydown', 'right arrow', self.R)
        self.listenKeyEvent('keydown', 'left arrow', self.L)
        self.listenKeyEvent('keydown', 'up arrow', self.U)
        self.listenKeyEvent('keydown', 'down arrow', self.D)
        #start with no car#
        self.car = None
        self.log = None
#Movement keys#
    def R(self, event):
        self.frog.x += 20
    def L(self, event):
        self.frog.x -= 20
    def U(self, event):
        self.frog.y -= 20
    def D(self, event):
        self.frog.y += 20
    
   #start game# 
    def go(self, event):
        self.road=Road(0,300)
        self.water=Water(0,50)
        self.frog=Frog(400,600)
        self.car=Car(0,400)
        self.log=Log(0,250)

    #reset game#
    def reset(self):
        #life decrease#
        global lives
        lives = lives -1 
        self.car.destroy()
        self.frog.destroy()
        self.log.destroy()
        self.go2()
    
    def go2(self):
        self.road=Road(0,300)
        self.water=Water(0,50)
        self.frog=Frog(400,600)
        self.car=Car(0,400)
        self.log=Log(0,250)

    def step(self):
        global carspeed
        global logspeed
        global loglength
        #makes car move#
        if self.car:
            self.car.x += carspeed
            if self.car.x > 780:
                self.car.x = 1
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                print('a')
                self.reset()
                print('a')
                
                
            

    
            


myapp = Frogger(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()