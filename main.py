import pygame
import random
import os

num = random.randint(0, 100)
print(num)

W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption('Угадай число ')
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W, H))

path = os.path.dirname(os.path.abspath(__file__))
bg = pygame.image.load(os.path.join(path, 'image/room.png'))
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load(os.path.join(path, 'image/cat.png'))
cat_rect = cat.get_rect(center=(70, 220))
dog = pygame.image.load(os.path.join(path, 'image/dog.png'))
dog_rect = dog.get_rect(center=(410, 220))
owl = pygame.image.load(os.path.join(path, 'image/owl.png'))
owl_rect = owl.get_rect(center=(210, 120))
dialog = pygame.image.load(os.path.join(path, 'image/dialog.png'))
dialog_rect = dialog.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x, - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    pygame.display.update()
