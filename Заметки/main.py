import pygame

from __pygame.Button import Button

def open_new_window(args):
    global screen
    Button.clearButtons()
    screen = pygame.display.set_mode((width,height))




if __name__ == '__main__':
    width, height = 900, 800
    screen, tick = pygame.display.set_mode((width, height)), pygame.time.Clock()

    for i in range(3):
        for j in range(3):
            Button(50 + j * 300, 50 + i * 250, 200, 200, f'i={i*3+j}',open_new_window,[i*3+j],screen)


    while True:
        screen.fill('#000000')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        Button.loop()



        pygame.display.flip()
        tick.tick(60)