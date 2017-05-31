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
carlength = random.randint(3,6)/2
carspeed = random.randint(40,75)/10

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
class Log7(Sprite):
    loglength = random.randint(2,10) * 40
    log = RectangleAsset(loglength, 30, thinline, brown)
    def __init__(self, x, y):
        super().__init__(Log7.log, (x, y))
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
        self.car2= None
        self.car3 = None
        self.car4= None
        self.car5 = None
        self.car6 = None
        self.car7 = None
        self.log1 = None
        self.log2 = None
        self.log3 = None
        self.log4 = None
        self.log5 = None
        self.log6 = None
        self.log7 = None
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
        self.log1=Log1(random.randint(0,800),285)
        self.log2=Log2(random.randint(0,800),245)
        self.log3=Log3(random.randint(0,800),205)
        self.log4=Log4(random.randint(0,800),165)
        self.log5=Log5(random.randint(0,800),125)
        self.log6=Log6(random.randint(0,800),85)
        self.log7=Log7(random.randint(0,800),45)
        self.car=Car(random.randint(0,800),405)
        self.car2=Car(random.randint(0,800), 365)
        self.car3=Car(random.randint(0,800), 325)
        self.car4=Car(random.randint(0,800), 445)
        self.car5=Car(random.randint(0,800), 485)
        self.car6=Car(random.randint(0,800), 525)
        
        
        
        self.white=White(800,0)
        self.white1=White(-400, 0)
        

    #reset game#
    def reset(self):
        self.frog.destroy()
        self.go2()
    
    def go2(self):
        self.frog=Frog(400,600)

    def step(self):
        #makes car move#
        if self.car:
            self.car.x += carspeed
            if self.car.x > 780:
                self.car.x = 1
            whitedeath = self.frog.collidingWithSprites(White)
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                self.reset()
            if whitedeath:
                self.reset()
        if self.car2:
            self.car2.x += carspeed
            if self.car2.x > 780:
                self.car2.x = 1
            whitedeath = self.frog.collidingWithSprites(White)
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                self.reset()
            if whitedeath:
                self.reset()
        if self.car3:
            self.car3.x -= carspeed
            if self.car3.x < 0:
                self.car3.x = 800
            whitedeath = self.frog.collidingWithSprites(White)
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                self.reset()
            if whitedeath:
                self.reset()
        if self.car4:
            self.car4.x += carspeed
            if self.car4.x > 780:
                self.car4.x = 1
            whitedeath = self.frog.collidingWithSprites(White)
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                self.reset()
            if whitedeath:
                self.reset()
        if self.car5:
            self.car5.x -= carspeed
            if self.car5.x < 0:
                self.car5.x = 800
            whitedeath = self.frog.collidingWithSprites(White)
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                self.reset()
            if whitedeath:
                self.reset()
        if self.car6:
            self.car6.x += carspeed
            if self.car6.x > 780:
                self.car6.x = 1
            whitedeath = self.frog.collidingWithSprites(White)
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                self.reset()
            if whitedeath:
                self.reset()
        if self.car7:
            self.car7.x -= carspeed
            if self.car7.x < 0:
                self.car7.x = 800
            whitedeath = self.frog.collidingWithSprites(White)
            cardeath = self.frog.collidingWithSprites(Car)
            if cardeath:
                self.reset()
            if whitedeath:
                self.reset() 
        if self.log1:
            logspeed = random.randint(15,30)/10
            neglogspeed = -1*logspeed
            log1collide = self.frog.collidingWithSprites(Log1)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6) or self.frog.collidingWithSprites(Log7)
            watercollide = self.frog.collidingWithSprites(Water)
            self.log1.x += logspeed
            if self.log1.x > 800:
                self.log1.x = 0
            if watercollide:
                if log1collide:
                    self.frog.x += logspeed
                if logcollide:
                    pass
                else:
                    self.reset()

                
        if self.log2:
            logspeed = -1*random.randint(15,30)/10
            log2collide = self.frog.collidingWithSprites(Log2)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6) or self.frog.collidingWithSprites(Log7)
            watercollide = self.frog.collidingWithSprites(Water)
            self.log2.x += logspeed
            if self.log2.x < -20:
                self.log2.x = 800
            if watercollide:
                if log2collide:
                    self.frog.x += logspeed
                if logcollide:
                    pass
                else:
                    self.reset()
        if self.log3:
            logspeed = random.randint(15,30)/10
            log3collide = self.frog.collidingWithSprites(Log3)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6) or self.frog.collidingWithSprites(Log7)
            watercollide = self.frog.collidingWithSprites(Water)
            self.log3.x += logspeed
            if self.log3.x > 800:
                self.log3.x = 0
            if watercollide:
                if log3collide:
                    self.frog.x += logspeed
                if logcollide:
                    pass
                else:
                    self.reset()
        if self.log4:
            logspeed = -1*random.randint(15,30)/10
            log4collide = self.frog.collidingWithSprites(Log4)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6) or self.frog.collidingWithSprites(Log7)
            watercollide = self.frog.collidingWithSprites(Water)
            self.log4.x += logspeed
            if self.log4.x < -20:
                self.log4.x = 800
            if watercollide:
                if log4collide:
                    self.frog.x += logspeed
                if logcollide:
                    pass
                else:
                    self.reset()
        if self.log5:
            logspeed = random.randint(15,30)/10
            log5collide = self.frog.collidingWithSprites(Log5)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6) or self.frog.collidingWithSprites(Log7)
            watercollide = self.frog.collidingWithSprites(Water)
            self.log5.x += logspeed
            if self.log5.x > 800:
                self.log5.x = 0
            if watercollide:
                if log5collide:
                    self.frog.x += logspeed
                if logcollide:
                    pass
                else:
                    self.reset()
        if self.log6:
            logspeed = -1*random.randint(15,30)/10
            log6collide = self.frog.collidingWithSprites(Log6)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6) or self.frog.collidingWithSprites(Log7)
            watercollide = self.frog.collidingWithSprites(Water)
            self.log6.x += logspeed
            if self.log6.x < -20:
                self.log6.x = 800
            if watercollide:
                if log6collide:
                    self.frog.x += logspeed
                if logcollide:
                    pass
                else:
                    self.reset()
        if self.log7:
            logspeed = random.randint(15,30)/10
            log7collide = self.frog.collidingWithSprites(Log7)
            logcollide = self.frog.collidingWithSprites(Log1) or self.frog.collidingWithSprites(Log2) or self.frog.collidingWithSprites(Log3) or self.frog.collidingWithSprites(Log4) or self.frog.collidingWithSprites(Log5) or self.frog.collidingWithSprites(Log6) or self.frog.collidingWithSprites(Log7)
            watercollide = self.frog.collidingWithSprites(Water)
            self.log7.x += logspeed
            if self.log7.x > 800:
                self.log7.x = 0
            if watercollide:
                if log7collide:
                    self.frog.x += logspeed
                if logcollide:
                    pass
                else:
                    self.reset()
        
        
                
            

    
            


myapp = Frogger(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()