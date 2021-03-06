import pygame, controls
from space_banger import Gun
from pygame.sprite import Group
from stats import Stats
from rating import Scores


def start():
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption('cosmo_wars')
    color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)

start()
