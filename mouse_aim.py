import pygame
import pygame.draw
#from main import gameScreen

pygame.init()
WIDTH, HEIGHT = 800, 600
FPSt = 60
gameScreen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

#функция размера курсора и прорисовка его
def Cursor_pitsel(x, y):
    pygame.draw.circle(gameScreen,(255,255,255), (x, y), 10, 1)
    pygame.draw.circle(gameScreen,(255,255,255), (x, y), 20, 1)
    pygame.draw.circle(gameScreen,(255,255,255), (x, y),  1)
    pygame.draw.line(gameScreen, (255,255, 255), (x - 24, y),(x-16, y))
    pygame.draw.line(gameScreen, (255,255, 255), (x + 24, y),(x+16, y))
    pygame.draw.line(gameScreen, (255,255, 255), (x, y - 24),(x, y - 16))
    pygame.draw.line(gameScreen, (255,255, 255), (x, y + 24),(x, y + 16))


pygame.mouse.set_visible(False)#скрытие мышки, мышка не перекрывает курсор, а стала невидема
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

#курсор ходит за мышкой
    pos = pygame.mouse.get_pos()

    gameScreen.fill(pygame.Color('black'))
    Cursor_pitsel(pos[0], pos[1])


    buttonLeft, buttonMiddle, buttonReght = pygame.mouse.get_pressed() #нажатие на кнопки мыши и на колесико
    print(buttonLeft, buttonMiddle,buttonReght)


   # Cursor_pitsel(300,200)
    pygame.display.update()
    clock.tick(FPSt)
pygame.quit()
