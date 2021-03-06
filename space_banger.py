import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):  # инициализация пушки
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):   # отрисовка пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self):   # обновление позиции пушки
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 5.5
        if self.move_left and self.rect.left > 0:
            self.center -= 5.5

        self.rect.centerx = self.center

    def create_gun(self):  # размещает новую пушку
        self.center = self.screen_rect.centerx



