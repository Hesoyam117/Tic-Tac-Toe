import pygame
import random
W = 902
H = 900
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("tic-tac-toe")
field = pygame.image.load('materials/field.png').convert_alpha()
field = pygame.transform.scale(field, (field.get_width()*10, field.get_height()*10))
cross = pygame.image.load('materials/Cross.png').convert_alpha()
cross = pygame.transform.scale(cross, (cross.get_width()*10, cross.get_height()*10))
circle = pygame.image.load('materials/circle.png').convert_alpha()
circle = pygame.transform.scale(circle, (circle.get_width()*10, circle.get_height()*10))
grscreen = pygame.image.load('materials/grscreen.png').convert_alpha()
grscreen = pygame.transform.scale(grscreen, (grscreen.get_width()*10, grscreen.get_height()*10))
redscreen = pygame.image.load('materials/redscreen.png').convert_alpha()
redscreen = pygame.transform.scale(redscreen, (redscreen.get_width()*10, redscreen.get_height()*10))
wood = pygame.image.load('materials/wood.jpg').convert()
bot = pygame.image.load('materials/hotsit.png').convert()
bot = pygame.transform.scale(bot, (bot.get_width()*8, bot.get_height()*8))
hotsit = pygame.image.load('materials/bot.png').convert()
hotsit = pygame.transform.scale(hotsit, (hotsit.get_width()*8, hotsit.get_height()*8))
grscreen2 = pygame.image.load('materials/grscreen2.png').convert_alpha()
grscreen2 = pygame.transform.scale(grscreen2, (grscreen2.get_width()*8, grscreen2.get_height()*8))
frame = pygame.image.load('materials/frame.png').convert_alpha()
frame = pygame.transform.scale(frame, (frame.get_width()*10, frame.get_height()*10))
FPS = 20
tile = 1
tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
tilesPick = 0
coords = [(0, 0), (220, 0), (440, 0), (0, 220), (220, 220), (440, 220), (0, 440), (220, 440), (440, 440)]
steps = 1
win_circle = False
win_cross = False
Draw = False
start = False
hotsitpl = False
botpl = False
choice = 2
circlepl = False
crosspl = False
fst = random.randint(0, 8)


clock = pygame.time.Clock()

flRunning = True
