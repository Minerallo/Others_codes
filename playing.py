import pygame

pygame.init()

display_width = 800
display_height = 600
car_width = 100
car_height = 160

a = 0
b = 0

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

carImg = pygame.image.load('character_game.png')
carImg = pygame.transform.scale(carImg, (car_width, car_height))
backimg = pygame.image.load('background.png')
backimg = pygame.transform.scale(backimg, (display_width+7, display_height+5))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def background(a, b):
    gameDisplay.blit(backimg, (a-3, b))


def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.65)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #         x_change = 0
        x += x_change
        y += y_change
        if x > display_width-car_width:
            x_change = -5
        if x < 0:
            x_change = 5
        if y > display_height-car_height:
            y_change = -5
        if y < 0:
            y_change = 5
        # if y < 0:
        #     x_change = 5
        background(a, b)
        # gameDisplay.fill(white)
        car(x, y)

        pygame.display.update()
        # Frame per second
        clock.tick(50)


game_loop()
pygame.quit()
quit()
