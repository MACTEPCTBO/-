import pygame.image

from setting import *

class Bot(pygame.sprite.Sprite):
    def __init__(self,x,y,vec,id,mass):
        super().__init__()
        self.life = True
        self.mass = mass

        self.vec = vec
        self.id = id

        self.image = pygame.image.load('image/bot.png')
        self.rect = self.image.get_rect(center=(x,y))

    def update(self):
        for b in bots:
            if self.rect.x > b.rect.x:
                self.vec[0] -= b.mass
            elif self.rect.x < b.rect.x:
                self.vec[0] += b.mass
            if self.rect.y > b.rect.y:
                self.vec[1] -= b.mass
            elif self.rect.y < b.rect.y:
                self.vec[1] += b.mass

        self.rect.x += self.vec[0]
        self.rect.y += self.vec[1]

        self.stolk()
        #print(self.vec)

        if self.rect.x < 0:
            self.vec[0] = 2
        elif self.rect.x > WIDTH:
            self.vec[0] = -2

        if self.rect.y < 0:
            self.vec[1] = 2
        elif self.rect.y > HEIGHT:
            self.vec[1] = -2


        self.draw()


    def draw(self):
        screen.blit(self.image,self.rect)
    
    def stolk(self):
        for b in bots:
            if self.rect.colliderect(b.rect) and self.id != b.id:
                #print('kill')

                x = self.rect.x
                y = self.rect.y
                vec = [b.vec[0],b.vec[1]]

                b = Bot(x,y,vec,bot_id,self.mass+b.mass)
                bots.append(b)


                self.life = False
                b.life = False
                return

    def death(self):
        if not self.life:
            return True
        return False