# Chan Jia Hui

import pygame
import sys
from prettytable import PrettyTable
# https://pypi.org/project/prettytable/

pygame.init()
pygame.mixer.init()
# https://www.pygame.org/docs/ref/mixer.html

WIDTH, HEIGHT = 1060,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SRCALPHA)
pygame.display.set_caption("Congratulations! You're win!!! ")


winbg = pygame.image.load("winbg.png")
WIN.blit(winbg,(0,0))

pygame.draw.rect(WIN,(0,102,153,25),(80,40,900,600),border_radius =30)

data = []
# https://www.geeksforgeeks.org/how-to-open-a-file-using-the-with-statement/
with open("name.txt","r") as f:
    for lines in f:
        line = lines.strip().split()
        if len(line) == 2 and line[1].isdigit():
            user, score = line
            data.append((user, int(score)))

data_sorted = sorted(data, key=lambda x: x[1])    
# https://www.w3schools.com/python/python_lambda.asp
table = PrettyTable()
table.field_names = ["Rank", "Username", "Score"]

font = pygame.font.SysFont("comicsans", 30)

field_names_rendered = []
for field in table.field_names:
    field_rendered = font.render(field, True, (255, 255, 255))
    field_names_rendered.append(field_rendered)

text_height = font.get_height()
x_offset = 170
y_offset = 100

for i, (user, score) in enumerate(data_sorted[:10], start=1):
    rank_text = font.render(str(i), True, (255, 255, 255))
    user_text = font.render(user, True, (255, 255, 255))
    score_text = font.render(str(score), True, (255, 255, 255))

    for j, field_rendered in enumerate(field_names_rendered):
        WIN.blit(field_rendered, (x_offset + j * 300, y_offset))

    WIN.blit(rank_text, (x_offset + 25, y_offset + i * text_height))
    WIN.blit(user_text, (x_offset + 300, y_offset + i * text_height))
    WIN.blit(score_text, (x_offset + 600, y_offset + i * text_height))



sound_effect = pygame.mixer.Sound("winse.mp3")
sound_effect.play()
pygame.mixer_music.load("winbgm.mp3")
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.5)

         
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

