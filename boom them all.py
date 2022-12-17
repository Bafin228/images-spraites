import os
import sys
from random import randint, randrange
import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
SIZE = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(SIZE)
BACKGROUND = 'black'
COUNT_BOMBS = 20




def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    boom = load_image('boom.png')

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = randrange(WIDTH - self.rect.width)
        self.rect.y = randrange(HEIGHT - self.rect.height)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
                center = self.rect.center
                self.image = Bomb.boom
                self.rect = self.image.get_rect()
                self.rect.center = center


all_sprites = pygame.sprite.Group()
for _ in range(COUNT_BOMBS):
    Bomb(all_sprites)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)
    screen.fill(BACKGROUND)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()