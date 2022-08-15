import pygame
import random
pygame.init()
from settings import *
def drawWindow():
    global steps
    global fst
    f_sys = pygame.font.SysFont('calibri', 50)
    if start == False and botpl == False and hotsitpl == False:
        win.blit(wood, (0, 0))
        win.blit(bot, (30, 30))
        win.blit(hotsit, (400, 30))
        win_text = f_sys.render(str("ESC - Выход в главное меню"), 4, (0, 0, 220))
        win.blit(win_text, (30, 500))
        win_text2 = f_sys.render(str("SPACE - Выбрать"), 4, (0, 0, 220))
        win.blit(win_text2, (30, 550))
        if choice == 2:
            win.blit(grscreen2, (400, 30))
            win_text3 = f_sys.render(str("Играть на одном компьютере"), 4, (0, 220, 0))
            win.blit(win_text3, (30, 400))
        elif choice == 1:
            win.blit(grscreen2, (30, 30))
            win_text3 = f_sys.render(str("Играть с ботом"), 4, (220, 0, 0))
            win.blit(win_text3, (30, 400))
    elif start == False and botpl == True:
        win.blit(wood, (0, 0))
        win.blit(circle, (30, 30))
        win.blit(cross, (270, 30))
        win.blit(frame, (20, 20))
        win.blit(frame, (260, 20))
        if choice == 2:
            win.blit(grscreen, (270, 30))
            win_text = f_sys.render(str("Играть за крестики"), 4, (0, 0, 0))
            win.blit(win_text, (30, 250))
        if choice == 1:
            win.blit(grscreen, (30, 30))
            win_text = f_sys.render(str("Играть за нолики"), 4, (220, 0, 0))
            win.blit(win_text, (30, 250))
    elif start == True:
        win.blit(wood, (0, 0))
        win.blit(field, (0, 0))
        if (steps % 2) == 1 and win_cross == False and win_circle == False and Draw == False and botpl == False:
            win_text = f_sys.render(str("Ход крестиков"), 4, (0, 0, 0))
            win.blit(win_text, (10, 700))
        if (steps % 2) == 0 and win_cross == False and win_circle == False and Draw == False and botpl == False:
            win_text = f_sys.render(str("Ход ноликов"), 4, (255, 0, 0))
            win.blit(win_text, (10, 700))
        if win_circle == True:
            win_text = f_sys.render(str("Победа ноликов"), 4, (255, 0, 0))
            win.blit(win_text, (100, 750))
            win_text2 = f_sys.render(str("Backspace - начать сначала"), 4, (255, 0, 0))
            win.blit(win_text2, (100, 800))
        if win_cross == True:
            win_text = f_sys.render(str("Победа крестиков"), 4, (0, 0, 0))
            win.blit(win_text, (100, 750))
            win_text2 = f_sys.render(str("Backspace - начать сначала"), 4, (0, 0, 0))
            win.blit(win_text2, (100, 800))
        if Draw == True:
            win_text = f_sys.render(str("Ничья"), 4, (0, 220, 0))
            win.blit(win_text, (100, 750))
            win_text2 = f_sys.render(str("Backspace - начать сначала"), 4, (0, 220, 0))
            win.blit(win_text2, (100, 800))
        if circlepl == True:
            win_text3 = f_sys.render(str("Вы играете за нолики"), 4, (255, 0, 0))
            win.blit(win_text3, (10, 700))
        if crosspl == True:
            win_text3 = f_sys.render(str("Вы играете за крестики"), 4, (0, 0, 0))
            win.blit(win_text3, (10, 700))
        for i in range (0, 9):
            if tiles[i] == 1:
                win.blit(circle, (coords[i]))
            if tiles[i] == 2:
                win.blit(cross, (coords[i]))
            if tilesPick == i and tiles[tilesPick] == 0 and win_cross == False and win_circle == False and Draw == False:
                win.blit(grscreen, coords[i])
            if (tilesPick == i and tiles[tilesPick] != 0) or (tilesPick == i and (win_cross == True or win_circle == True or Draw == True)):
                win.blit(redscreen, coords[i])
    pygame.mouse.set_visible(False)
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        #pygame.draw.circle(win, (220, 0, 0), pos, 7)
        win.blit(mel, pos)

    pygame.display.flip()

def gamerule():
    global tiles
    global tilesPick
    global steps
    global win_cross
    global win_circle
    global Draw
    if tilesPick > 8: tilesPick = 0
    elif tilesPick < 0: tilesPick = 8
    if steps > 10:
        steps = 1
    elif ((tiles[0] == 1 and tiles[1] == 1 and tiles[2] == 1) or\
    (tiles[3] == 1 and tiles[4] == 1 and tiles[5] == 1) or\
    (tiles[6] == 1 and tiles[7] == 1 and tiles[8] == 1)):
        win_circle = True
    elif ((tiles[0] == 1 and tiles[3] == 1 and tiles[6] == 1) or\
    (tiles[1] == 1 and tiles[4] == 1 and tiles[7] == 1) or\
    (tiles[2] == 1 and tiles[5] == 1 and tiles[8] == 1) or\
    (tiles[0] == 1 and tiles[4] == 1 and tiles[8] == 1) or (tiles[2] == 1 and tiles[4] == 1 and tiles[6] == 1)):
        win_circle = True
    elif ((tiles[0] == 2 and tiles[1] == 2 and tiles[2] == 2) or\
    (tiles[3] == 2 and tiles[4] == 2 and tiles[5] == 2) or\
    (tiles[6] == 2 and tiles[7] == 2 and tiles[8] == 2)):
        win_cross = True
    elif ((tiles[0] == 2 and tiles[3] == 2 and tiles[6] == 2) or\
    (tiles[1] == 2 and tiles[4] == 2 and tiles[7] == 2) or\
    (tiles[2] == 2 and tiles[5] == 2 and tiles[8] == 2) or\
    (tiles[0] == 2 and tiles[4] == 2 and tiles[8] == 2) or (tiles[2] == 2 and tiles[4] == 2 and tiles[6] == 2)):
        win_cross = True
    elif tiles.count(0) < 1 and win_cross == False and win_circle == False:
            Draw = True
    else:
        win_cross = False
        win_circle = False
        Draw = False

    def botAI(n, m):
        done = 0
        if tiles[0] == n and tiles[1] == n and done == 0 and tiles[2] == 0:
            tiles[2] = n
            done = 1
        elif tiles[1] == n and tiles[2] == n and done == 0 and tiles[0] == 0:
            tiles[0] = n
            done = 1
        elif tiles[0] == n and tiles[2] == n and done == 0 and tiles[1] == 0:
            tiles[1] = n
            done = 1
        elif tiles[3] == n and tiles[4] == n and done == 0 and tiles[5] == 0:
            tiles[5] = n
            done = 1
        elif tiles[4] == n and tiles[5] == n and done == 0 and tiles[3] == 0:
            tiles[3] = n
            done = 1
        elif tiles[5] == n and tiles[3] == n and done == 0 and tiles[4] == 0:
            tiles[4] = n
            done = 1
        elif tiles[6] == n and tiles[7] == n and done == 0 and tiles[8] == 0:
            tiles[8] = n
            done = 1
        elif tiles[7] == n and tiles[8] == n and done == 0 and tiles[6] == 0:
            tiles[6] = n
            done = 1
        elif tiles[6] == n and tiles[8] == n and done == 0 and tiles[7] == 0:
            tiles[7] = n
            done = 1
        elif tiles[0] == n and tiles[3] == n and done == 0 and tiles[6] == 0:
            tiles[6] = n
            done = 1
        elif tiles[3] == n and tiles[6] == n and done == 0 and tiles[0] == 0:
            tiles[0] = n
            done = 1
        elif tiles[0] == n and tiles[6] == n and done == 0 and tiles[3] == 0:
            tiles[3] = n
            done = 1
        elif tiles[1] == n and tiles[4] == n and done == 0 and tiles[7] == 0:
            tiles[7] = n
            done = 1
        elif tiles[4] == n and tiles[7] == n and done == 0 and tiles[1] == 0:
            tiles[1] = n
            done = 1
        elif tiles[1] == n and tiles[7] == n and done == 0 and tiles[4] == 0:
            tiles[4] = n
            done = 1
        elif tiles[2] == n and tiles[5] == n and done == 0 and tiles[8] == 0:
            tiles[8] = n
            done = 1
        elif tiles[5] == n and tiles[8] == n and done == 0 and tiles[2] == 0:
            tiles[2] = n
            done = 1
        elif tiles[2] == n and tiles[8] == n and done == 0 and tiles[5] == 0:
            tiles[5] = n
            done = 1
        elif tiles[0] == n and tiles[4] == n and done == 0 and tiles[8] == 0:
            tiles[8] = n
            done = 1
        elif tiles[4] == n and tiles[8] == n and done == 0 and tiles[0] == 0:
            tiles[0] = n
            done = 1
        elif tiles[0] == n and tiles[8] == n and done == 0 and tiles[4] == 0:
            tiles[4] = n
            done = 1
        elif tiles[2] == n and tiles[4] == n and done == 0 and tiles[6] == 0:
            tiles[6] = n
            done = 1
        elif tiles[6] == n and tiles[2] == n and done == 0 and tiles[4] == 0:
            tiles[4] = n
            done = 1
        elif tiles[4] == n and tiles[6] == n and done == 0 and tiles[2] == 0:
            tiles[2] = n
            done = 1
        elif tiles[0] == m and tiles[1] == m and done == 0 and tiles[2] == 0:
            tiles[2] = n
            done = 1
        elif tiles[1] == m and tiles[2] == m and done == 0 and tiles[0] == 0:
            tiles[0] = n
            done = 1
        elif tiles[0] == m and tiles[2] == m and done == 0 and tiles[1] == 0:
            tiles[1] = n
            done = 1
        elif tiles[3] == m and tiles[4] == m and done == 0 and tiles[5] == 0:
            tiles[5] = n
            done = 1
        elif tiles[4] == m and tiles[5] == m and done == 0 and tiles[3] == 0:
            tiles[3] = n
            done = 1
        elif tiles[5] == m and tiles[3] == m and done == 0 and tiles[4] == 0:
            tiles[4] = n
            done = 1
        elif tiles[6] == m and tiles[7] == m and done == 0 and tiles[8] == 0:
            tiles[8] = n
            done = 1
        elif tiles[7] == m and tiles[8] == m and done == 0 and tiles[6] == 0:
            tiles[6] = n
            done = 1
        elif tiles[6] == m and tiles[8] == m and done == 0 and tiles[7] == 0:
            tiles[7] = n
            done = 1
        elif tiles[0] == m and tiles[3] == m and done == 0 and tiles[6] == 0:
            tiles[6] = n
            done = 1
        elif tiles[3] == m and tiles[6] == m and done == 0 and tiles[0] == 0:
            tiles[0] = n
            done = 1
        elif tiles[0] == m and tiles[6] == m and done == 0 and tiles[3] == 0:
            tiles[3] = n
            done = 1
        elif tiles[1] == m and tiles[4] == m and done == 0 and tiles[7] == 0:
            tiles[7] = n
            done = 1
        elif tiles[4] == m and tiles[7] == m and done == 0 and tiles[1] == 0:
            tiles[1] = n
            done = 1
        elif tiles[1] == m and tiles[7] == m and done == 0 and tiles[4] == 0:
            tiles[4] = n
            done = 1
        elif tiles[2] == m and tiles[5] == m and done == 0 and tiles[8] == 0:
            tiles[8] = n
            done = 1
        elif tiles[5] == m and tiles[8] == m and done == 0 and tiles[2] == 0:
            tiles[2] = n
            done = 1
        elif tiles[2] == m and tiles[8] == m and done == 0 and tiles[5] == 0:
            tiles[5] = n
            done = 1
        elif tiles[0] == m and tiles[4] == m and done == 0 and tiles[8] == 0:
            tiles[8] = n
            done = 1
        elif tiles[4] == m and tiles[8] == m and done == 0 and tiles[0] == 0:
            tiles[0] = n
            done = 1
        elif tiles[0] == m and tiles[8] == m and done == 0 and tiles[4] == 0:
            tiles[4] = n
            done = 1
        elif tiles[2] == m and tiles[4] == m and done == 0 and tiles[6] == 0:
            tiles[6] = n
            done = 1
        elif tiles[6] == m and tiles[2] == m and done == 0 and tiles[4] == 0:
            tiles[4] = n
            done = 1
        elif tiles[4] == m and tiles[6] == m and done == 0 and tiles[2] == 0:
            tiles[2] = n
            done = 1
        elif (tiles[8] == 0):
            tiles[8] = n
        elif tiles[0] == 0 and (tiles[8] != 0):
            tiles[0] = n
        elif tiles[4] == 0 and (tiles[0] != 0 and tiles[8] != 0):
            tiles[4] = n
        elif tiles[2] == 0 and (tiles[4] != 0 and tiles[0] != 0 and tiles[8] != 0):
            tiles[2] = n
        elif tiles[1] == 0 and (tiles[2] != 0 and tiles[4] != 0 and tiles[0] != 0 and tiles[8] != 0):
            tiles[1] = n
        elif tiles[5] == 0 and (tiles[1] != 0 and tiles[2] != 0 and tiles[4] != 0 and tiles[0] != 0 and tiles[8] != 0):
            tiles[5] = n
        elif tiles[6] == 0 and (tiles[5] != 0 and tiles[1] != 0 and tiles[2] != 0 and tiles[4] != 0 and tiles[0] != 0 and tiles[8] != 0):
            tiles[6] = n
        elif tiles[3] == 0 and (tiles[6] != 0 and tiles[5] != 0 and tiles[1] != 0 and tiles[2] != 0 and tiles[4] != 0 and tiles[0] != 0 and tiles[8] != 0):
            tiles[3] = n
        elif tiles[7] == 0 and (tiles[3] != 0 and tiles[6] != 0 and tiles[5] != 0 and tiles[1] != 0 and tiles[2] != 0 and tiles[4] != 0 and tiles[0] != 0 and tiles[8] != 0):
            tiles[7] = n
    fst = random.randint(0, 3)
    randomizer = [0, 2, 6, 8]
    snd = random.randint(0, 9)
    if start == True and botpl == True and circlepl == True:
        if steps == 1:
            if tiles == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
                tiles[(randomizer[fst])] = 2
            steps = 2
        elif steps == 3:
            botAI(2, 1)
            steps = 4
        elif steps == 5:
            botAI(2, 1)
            steps = 6
        elif steps == 7 and win_circle == False:
            botAI(2, 1)
            steps = 8
        elif steps == 9 and win_circle == False:
            botAI(2, 1)
    elif start == True and botpl == True and crosspl == True:
        if steps == 2:
            #botAI(1, 2)
            done1 = 0
            if tiles[(randomizer[fst])] == 0 and done1 == 0:
                tiles[(randomizer[fst])] = 1
                done1 = 1
            elif tiles[snd] == 0 and done1 == 0:
                tiles[snd] = 1
                done = 1
            elif done1 == 0:
                botAI(1, 2)
                done1 = 1
            steps = 3
        elif steps == 4:
            botAI(1, 2)
            steps = 5
        elif steps == 6 and win_cross == False:
            botAI(1, 2)
            steps = 7
        elif steps == 8 and win_cross == False:
            botAI(1, 2)
            steps = 9

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and tiles[tilesPick] == 0 and win_cross == False and win_circle == False and start == True and hotsitpl == True:
                if (steps % 2) == 0 and steps != 10:
                    tiles[tilesPick] = 1
                elif (steps % 2) == 1 and steps != 10:
                    tiles[tilesPick] = 2
                steps +=1
            elif event.key == pygame.K_SPACE and tiles[tilesPick] == 0 and win_cross == False and win_circle == False and botpl == True and start == True:
                if circlepl == True and (steps % 2) == 0 and steps !=10:
                    tiles[tilesPick] = 1
                    steps += 1
                if crosspl == True and (steps % 2) == 1 and steps !=10:
                    tiles[tilesPick] = 2
                    steps += 1
            elif event.key == pygame.K_SPACE and start == False and choice == 2 and hotsitpl == False and botpl == False:
                start = True
                hotsitpl = True
            elif event.key == pygame.K_SPACE and start == False and choice == 1 and hotsitpl == False and botpl == False:
                botpl = True
            elif event.key == pygame.K_SPACE and start == False and choice == 1 and botpl == True:
                start = True
                circlepl = True
            elif event.key == pygame.K_SPACE and start == False and choice == 2 and botpl == True:
                start = True
                crosspl = True
            elif event.key == pygame.K_ESCAPE:
                crosspl = False
                circlepl = False
                start = False
                botpl = False
                hotsitpl = False
                tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                steps = 1
            elif event.key == pygame.K_BACKSPACE:
                tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                steps = 1
                win_cross = False
                win_circle = False
            if event.key == pygame.K_RIGHT:
                if start == False and hotsitpl == False and botpl == False:
                    choice = 2
                elif start == True:
                    tilesPick += 1
                elif start == False and botpl == True:
                    choice = 2
            elif event.key == pygame.K_LEFT:
                if start == False and hotsitpl == False and botpl == False:
                    choice = 1
                elif start == True:
                    tilesPick -= 1
                elif start == False and botpl == True:
                    choice = 1
            elif event.key == pygame.K_UP:
                if tilesPick != 0  and tilesPick != 1 and tilesPick != 2:
                    tilesPick -= 3
            elif event.key == pygame.K_DOWN:
                if tilesPick != 6  and tilesPick != 7 and tilesPick != 8:
                    tilesPick += 3
        elif event.type == pygame.MOUSEMOTION:
            for i in range (0, 9):
                if event.pos[0] >= coords1x[i] and event.pos[0] <= coords2x[i] and event.pos[1] >= coords1y[i] and event.pos[1] <= coords2y[i]:
                    tilesPick = i
                    mousefocused = True
                elif event.pos[0] >= 30 and event.pos[0] <= 350 and event.pos[1] >= 30 and event.pos[1] <= 230 and start == False and  botpl == False and hotsitpl == False:
                    choice = 1
                    mousefocused = True
                elif event.pos[0] >= 400 and event.pos[0] <= 720 and event.pos[1] >= 30 and event.pos[1] <= 230 and start == False and  botpl == False and hotsitpl == False:
                    choice = 2
                    mousefocused = True
                elif event.pos[0] >= 30 and event.pos[0] <= 230 and event.pos[1] >= 30 and event.pos[1] <= 230 and  start == False and botpl == True:
                    choice = 1
                    mousefocused = True
                elif event.pos[0] >= 270 and event.pos[0] <= 470 and event.pos[1] >= 30 and event.pos[1] <= 230 and  start == False and botpl == True:
                    choice = 2
                    mousefocused = True
                #win.blit(circle, (30, 30))
                #win.blit(cross, (270, 30))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and tiles[tilesPick] == 0 and win_cross == False and win_circle == False and start == True and hotsitpl == True and mousefocused == True:
                if (steps % 2) == 0 and steps != 10:
                    tiles[tilesPick] = 1
                elif (steps % 2) == 1 and steps != 10:
                    tiles[tilesPick] = 2
                steps +=1
            elif event.button == 1 and tiles[tilesPick] == 0 and win_cross == False and win_circle == False and botpl == True and start == True and mousefocused == True:
                if circlepl == True and (steps % 2) == 0 and steps !=10:
                    tiles[tilesPick] = 1
                    steps += 1
                if crosspl == True and (steps % 2) == 1 and steps !=10:
                    tiles[tilesPick] = 2
                    steps += 1
            elif event.button == 1 and start == False and choice == 2 and hotsitpl == False and botpl == False and mousefocused == True:
                start = True
                hotsitpl = True
            elif event.button == 1 and start == False and choice == 1 and hotsitpl == False and botpl == False and mousefocused == True:
                botpl = True
            elif event.button == 1 and start == False and choice == 1 and botpl == True and mousefocused == True:
                start = True
                circlepl = True
            elif event.button == 1 and start == False and choice == 2 and botpl == True and mousefocused == True:
                start = True
                crosspl = True





    gamerule()
    drawWindow()
    clock.tick(FPS)
