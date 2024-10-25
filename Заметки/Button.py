import pygame
from threading import Thread

pygame.init()

class Button:
    buttons = []
    font = pygame.font.Font(None,30)
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 text: str,
                 command: str,
                 args: list,
                 screen: pygame.Surface
                 ):


        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.Surface = pygame.Surface((width,height))
        self.Surface.fill('#800080')

        self.text = text
        self.text_render = self.font.render(self.text,True,(255,255,255))

        self.command = command
        self.args = args
        self.click = True

        self.screen = screen

        self.buttons.append(self)


    def event(self):
        click = pygame.mouse.get_pressed()
        x,y = pygame.mouse.get_pos()

        if self.click and click[0] and self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.click = False
            if self.args != []:
                self.command(self.args)
            else:
                self.command(self.args)
        elif not self.click and not click[0]:
            self.click = True


    @classmethod
    def loop(cls):
        print(len(cls.buttons))
        for i in range(len(cls.buttons)):
            try:
                cls.buttons[i].render_text()
                cls.buttons[i].draw()
                cls.buttons[i].event()
            except:pass

    def draw(self):
        self.Surface.blit(self.text_render, (0,0))
        self.screen.blit(self.Surface, (self.x,self.y))


    def render_text(self):
        self.text_render = self.font.render(self.text,True,(255,255,255))


    @classmethod
    def clearButtons(cls):
        cls.buttons = []



def h1(args):
    print(args)


if __name__ == '__main__':
    width,height = 500,500
    screen,tick = pygame.display.set_mode((width,height)),pygame.time.Clock()

    b1 = Button(100,100,200,100,'hello world',h1,['1',2,'3'], screen)


    while True:
        screen.fill('#000000')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        b1.loop()


        pygame.display.flip()
        tick.tick(60)