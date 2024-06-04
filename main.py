#!/usr/bin/env python3

import pygame as pg
import os
from enemy import Enemy
from harmless import Harmless
from juker import Juker
from destroyer import Destroyer
from player import Player
from projectile import Projectile
from pygame.locals import *

def main():
    """
        Project: 8-bit Arcade, Star Wars Game 
        Version: 1.0
        Authors: Bailey Compton and Brandon Baker
        Class: Structures of Programming Languages
        
        Main game loop that runs and updates the game 
    """
    
    # Startup pygame
    pg.init()
    pg.display.set_caption('Star Wars Game')
    
    # Get a screen object
    screen = pg.display.set_mode([1024, 768])
    
    player = Player()
    enemies = pg.sprite.Group()
    projectiles = pg.sprite.Group()
    
    enemy1 = Destroyer((250, 250))
    enemies.add(enemy1)

    enemy2 = Destroyer((250 + 100, 250))
    enemies.add(enemy2)
    
    # Spawn Jukers
    for i in range(4):
            enemy = Juker((100 + i * 100, 100))
            enemies.add(enemy)
    
    # Spawn harmless enemies in groups
    for i in range(4):
        for j in range(4):
            enemy = Harmless((685 + i * 65, 150 + j * 65))
            enemies.add(enemy)
    
    for i in range(4):
        for j in range(4):
            enemy = Harmless((100 + i * 65, 150 + j * 65))
            enemies.add(enemy)

    # Startup the main game loop
    running = True
    delta = 0
    shotDelta = 500
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    score = 0
    while running:
        
        # First thing we need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 100
                
        # Key Pressed
        keys = pg.key.get_pressed()
        
        # Detect player controls in player class
        player.move(keys, delta)
        
        # Reset projectile timer if weapon was changed
        if player.checkWeaponSwitch(keys):
            shotDelta = 500
        
        shotDelta, enemies, projectiles, player = player.shoot(keys, shotDelta, enemies, player, projectiles)
                
        if len(enemies) == 0:
            print("You've cleared the galaxy of evil!")
            return
        
        if player.health <= 0:
            print("You lost! Hold this please: L")
            return


        screen.fill((50, 50, 50))
        
        # Draw health bar 
        font = pg.font.Font(None, 30)
        health_display = font.render(f'Health: {player.health}', True, (255,255,255))
        screen.blit(health_display, (22, 715))
        
        for enemy in enemies:
            enemy.move(delta)
            if not isinstance(enemy, Harmless):
                projectiles, player = enemy.attack(delta, enemies, player, projectiles)
            
        for projectile in projectiles:
            projectile.move(delta)

        # Draw the sprites on the screen
        player.draw(screen)
        enemies.draw(screen)
        projectiles.draw(screen)
           
            
        # When drawing is done, flip the buffer.
        pg.display.flip()

        delta = clock.tick(fps) / 1000.0
        shotDelta += delta

# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()
