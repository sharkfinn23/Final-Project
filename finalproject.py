from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

white = Color (0xffffff, 1.0)
black = Color(0x000000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
red = Color(0xff0000, 1.0)
brown = Color(0xD2691E, 1.0)
thinline = LineStyle(2, black)
whiteline = LineStyle(2, white)
#randoms
loglength = random.randint(2,10)
carlength = random.randint(1,3)
carspeed = random.randint(5,15)/10

black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, thinline, green)
bg = Sprite(bg_asset, (0,0))
class Road(Sprite):
    road = RectangleAsset(800, 250, thinline, black)
    def __init__(self, x, y):
        super().__init__(Road.road, (x, y))
        self.x = x
        self.y = y
        
class Water(Sprite):
    water = RectangleAsset(800, 265, thinline, blue)
    def __init__(self, x, y):
        super().__init__(Water.water, (x, y))
        self.x = x
        self.y = y

class Car(Sprite):
    global carlength
    car = RectangleAsset(40 * carlength, 30, thinline, green)
    def __init__(self, x, y):
        super().__init__(Car.car, (x, y))
        self.x = x
        self.y = y

class Log1(Sprite):
    loglength = random.randint(2,10) * 40
    log = RectangleAsset(loglength, 30, thinline, brown)
    def __init__(self, x, y):
        super().__init__(Log1.log, (x, y))
        self.x = x
        self.y = y
class Log2(Sprite):
    loglength = random.randint(2,10) * 40
    log = RectangleAsset(loglength, 30, thinline, brown)
    def __init__(self, x, y):
        super().__init__(Log2.log, (x, y))
        self.x = x
        self.y = y
class Log3(Sprite):
    loglength = random.randint(2,10) * 40
    log = RectangleAsset(loglength, 30, thinline, brown)
    def __init__(self, x, y):
        super().__init__(Log3.log, (x, y))
        self.x = x
        self.y = y
class Log4(Sprite):
    loglength = random.randint(2,10) * 40
    log = RectangleAsset(loglength, 30, thinline, brown)
    def __init__(self, x, y):
        super().__init__(Log4.log, (x, y))
        self.x = x
        self.y = y
class Log5(Sprite):
    loglength = random.randint(2,10) * 40
    log = RectangleAsset(loglength, 30, thinline, brown)
    def __init__(self, x, y):
        super().__init__(Log5.log, (x, y))
        self.x = x
        self.y = y
class Log6(Sprite):
    loglength = random.randint(2,10) * 40
    log = RectangleAsset(loglength, 30, thinline, brown)
    def __init__(self, x, y):
        super().__init__(Log6.log, (x, y))
        self.x = x
        self.y = y
class White(Sprite):
    white = RectangleAsset(400, 600, whiteline, white)
    def __init__(self, x, y):
        super().__init__(White.white, (x, y))
        self.x = x
        self.y = y







        
class Frog(Sprite):
    frog = RectangleAsset(40, 40, thinline, red)
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
        self.log1 = None
        self.log2 = None
        self.log3 = None
        self.log4 = None
        self.log5 = None
        self.log6 = None
        
#Movement keys#
    def R(self, event):
        self.frog.x += 40
    def L(self, event):
        self.frog.x -= 40
    def U(self, event):
        self.frog.y -= 40
    def D(self, event):
        self.frog.y += 40
    
   #start game# 
    def go(self, event):
        
        self.road=Road(0,300)
        self.water=Water(0,50)
        self.frog=Frog(400,600)
        self.log1=Log1(0,285)
        self.log2=Log2(800,245)
        self.log3=Log3(0,205)
        self.log4=Log4(800,165)
        self.log5=Log5(0,125)
        self.log6=Log6(800,85)
        self.car=Car(0,405)
        self.white=White(800,0)
        

    #reset game#
    def reset(self):
        self.road.destroy()
        self.water.destroy()
        self.frog.destroy()
        self.log1.destroy()
        self.log2.destroy()
        self.log3.destroy()
        self.log4.destroy()
        self.log5.destroy()
        self.log6.destroy()
        self.car.destroy()
        self.white.destroy()
        self.go2()
    
    def go2(self):
        self.road=Road(0,300)
        self.water=Water(0,50)
        self.frog=Frog(400,600)
        self.log1=Log1(0,285)
        self.log2=Log2(0,245)
        self.log3=Log3(0,205)
        self.log4=Log4(0,165)
        self.log5=Log5(0,125)
        self.log6=Log6(0,85)
        self.car=Car(0,405)
        self.white
        

    def step(self):
        #makes car move#
        if self.car:
            self.car.x += carspeed
            if self.car.x > 780:
                self.car.x = 1
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                self.reset()
        if self.log1:
            logspeed = random.randint(15,30)/10
            self.log1.x += logspeed
            if self.log1.x > 780:
                self.log1.x = 1
            watercollide = self.frog.collidingWithSprites(Water)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6)
            if watercollide:
                if logcollide:
                    self.frog.x += logspeed1
                else:
                    self.reset()
            if self.log1.x > 780:
                self.log1.x = 1
                
        if self.log2:
            logspeed = -1 * random.randint(15, 30)/10
            self.log2.x += logspeed
            if self.log2.x < 0:
                self.log2.x = 800
            watercollide = self.frog.collidingWithSprites(Water)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6)
            if watercollide:
                print('a')
                if logcollide:
                    self.frog.x += logspeed
                else:
                    self.reset()
            if self.log2.x < 0:
                self.log2.x = 800
                
                
                
            

    
            


myapp = Frogger(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()