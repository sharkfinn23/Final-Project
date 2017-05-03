from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

black = Color(0x000000, 1.0)
green = Color(0x00ff00, 1.0)


thinline = LineStyle(2, black)


black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, thinline, black)
bg = Sprite(bg_asset, (0,0))

class Road(Sprite):
    road = RectangleAsset(200, 20, thinline, green)
    def __init__(self, x, y):
        super().__init__(Road.road, (x, y))
        self.x = x
        self.y = y
    
class Frogger(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.mousex = 0
        self.mousey = 0
        self.listenKeyEvent('keydown', 's', self.go)

    def go(self, event):
        Road(0,0)
        
myapp = Frogger(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()