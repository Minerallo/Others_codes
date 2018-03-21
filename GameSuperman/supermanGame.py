import pygame
import time
import random

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
green = (0, 200, 0)
blue = (0, 0, 200)
bright_green = (0, 250, 0)
bright_blue = (0, 0, 250)

pause = False

gameDisplay = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

carImg = pygame.image.load('character_game.png')
carImg = pygame.transform.scale(carImg, (car_width, car_height))
backimg = pygame.image.load('background.png')
backimg = pygame.transform.scale(backimg, (display_width+7, display_height+5))


def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def thing(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def background(a, b):
    gameDisplay.blit(backimg, (a-3, b))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()


def crash():
    crash = True
    txdisplay = ('Boing')
    message_display(txdisplay)
    largeText = pygame.font.SysFont("comicsansms", 95)
    TextSurf, TextRect = text_objects("Boing", largeText)
    TextRect.center = ((display_width/2), (display_height/4))
    while crash = True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # button("Start", 150, 320, 100, 50, green, bright_green, "play")
        button("Continue", 150, 320, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 320, 100, 50, blue, bright_blue, quitgame)


def quitgame():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, k, n, action=None):
    # k and n are color active and inactive
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    # print(mouse)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, k, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            # if action == "play":
            #     game_loop()
            # elif action == "quit":
            #     pygame.quit()
            #     quit()
    else:
        pygame.draw.rect(gameDisplay, n, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x + (w/2), y+(h/2))
    gameDisplay.blit(textSurf, textRect)


def gameintro():
    x = (display_width * 0.45)
    y = (display_height * 0.65)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        background(a, b)
        car(x, y)
        largeText = pygame.font.SysFont("comicsansms", 95)
        TextSurf, TextRect = text_objects("SupermanGame", largeText)
        TextRect.center = ((display_width/2), (display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        # button("Start", 150, 320, 100, 50, green, bright_green, "play")
        button("Start", 150, 320, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 320, 100, 50, blue, bright_blue, quitgame)

        pygame.display.update()
        clock.tick(15)


def unpause():
    global pause
    pause = False


def paused():
    largeText = pygame.font.SysFont("comicsansms", 95)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # button("Start", 150, 320, 100, 50, green, bright_green, "play")
        button("Continue", 150, 320, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 320, 100, 50, blue, bright_blue, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():

    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.65)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)

    thing_starty = -600

    # negative to start outside of the screen
    thing_speed = 3
    thing_height = random.randrange(50, 100)
    thing_width = random.randrange(50, 100)

    dodged = 0

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
                if event.key == pygame.K_p:
                    pause = True
                    paused()
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

        # (thingx, thingy, thingw, thingh, color):
        thing(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        # each time goes down of 7 pixels and give the illusion to be faster
        car(x, y)
        things_dodged(dodged)
        if thing_starty > display_height:
            thing_starty = 0-thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            # thing_speed += 1
            thing_width += (dodged*1.2)
        # if y < thing_starty+thing_height:
        #     if thing_startx+thing_width > x and thing_startx+thing_width < x+car_width:
        #         crash()
        #     if thing_startx < x+car_width and thing_startx > x:
        #         crash()
        # if y+car_height > thing_starty:
        #     if x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
        #         crash()
        #     if x < thing_startx+thing_width and x > thing_startx:
        #         crash()
        if y < thing_starty+thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                print('xcrossover')
                crash()
        pygame.display.update()
        # Frame per second
        clock.tick(50)


# test
gameintro()
game_loop()
pygame.quit()
quit()
