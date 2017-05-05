from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

black = Color(0x000000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
red = Color(0xff0000, 1.0)
thinline = LineStyle(2, black)


black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, thinline, green)
bg = Sprite(bg_asset, (0,0))
gravity = 0
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

        
class Frog(Sprite):
    frog = RectangleAsset(15, 15, thinline, red)
    def __init__(self, x, y):
        super().__init__(Frog.frog, (x, y))
        self.x = x
        self.y = y

class Frogger(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.listenKeyEvent('keydown', 's', self.go)
        self.listenKeyEvent('keydown', 's', self.buildCar)
        self.listenKeyEvent('keydown', 'f', self.car)

    def buildCar (self, event):
        self.carsprite = Car(0, 400)
    
    def go(self, event):
        Road(0,300)
        Water(0,50)
        Frog(400,600)
        
    def car(self, event):
        car.x += 1
            


myapp = Frogger(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()