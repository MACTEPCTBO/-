from Bot import Bot
from setting import *


def create():
    global bot_id,pressed,time_pressed
    click = pygame.mouse.get_pressed()
    x,y = pygame.mouse.get_pos()

    if click[0] and pressed:
        b = Bot(x,y,[randint(-2,2),randint(-2,2)],bot_id,randint(0,2))
        bots.append(b)
        bot_id += 1
        pressed = False
        time_pressed = 0
    elif time_pressed < 60:
        pressed = True
    else:
        time_pressed += 1



b = Bot(250,250,[-1,1],bot_id,0.2)
bots.append(b)
bot_id += 1
b = Bot(350,350,[5,-1],bot_id,0.3)
bots.append(b)
bot_id += 1

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for i in range(len(bots)):

            bots[i].update()
    for i in range(len(bots)-1,0,-1):
        if bots[i].death():
            bot_id += 1
            bots.pop(i)
    create()

    print(f'бот id {bot_id}')


    pygame.display.update()
    time.tick(FPS)