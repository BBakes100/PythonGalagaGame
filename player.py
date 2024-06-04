"""
    Project: 8-bit Arcade, Star Wars Game 
    Version: 1.0
    Authors: Bailey Compton and Brandon Baker
    Class: Structures of Programming Languages
"""

import os
import pygame as pg
from pygame.locals import *
from lazer import Lazer
from pellet import Pellet
from rocket import Rocket
from dimensions import Dimensions as dim

class Player(pg.sprite.Sprite):
    """
    Player class that defines player functionality.
    
    Attributes:
        projectile_types (list): List of available projectile types for list iteration.
        projectileType (class): The currently selected projectile type.
        last_switch_time (float): Time of the last weapon switch.
        health (int): Player's health.
    """

    def __init__(self):
        """
        Initializes the player with default values.
        """
        super(Player, self).__init__()

        # Load and scale the player image
        og_image = pg.image.load(os.path.join('assets', 'player.png')).convert_alpha()
        image_rect = og_image.get_bounding_rect()
        self.image = og_image.subsurface(image_rect)
        self.image = pg.transform.scale(self.image, (dim.player_w, dim.player_h))
        self.image = pg.transform.rotate(self.image, 90)

        # Set the initial location of the player
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.centery = 600

        # Default values for player attributes
        self.projectile_types = [Pellet, Lazer, Rocket]
        self.projectileType = self.projectile_types[0]  # Default projectile type
        self.last_switch_time = 0
        self.health = 500

    def draw(self, screen):
        """
        Draws the player on the screen.

        Args:
            screen: The pygame display surface.
        """
        screen.blit(self.image, self.rect)

    def move(self, keys, delta):
        """
        Moves the player based on user input.

        Args:
            keys: The dictionary of currently pressed keys.
            delta (float): Time difference between frames.
        """
        moveSpeed = 500
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += moveSpeed * delta
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= moveSpeed * delta
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= moveSpeed * delta
        if keys[K_d] and self.rect.x < 890:
            self.rect.x += moveSpeed * delta

    def checkWeaponSwitch(self, keys):
        """
        Checks for a weapon switch input and updates the selected projectile type.

        Args:
            keys: The dictionary of currently pressed keys.

        Returns:
            switched (bool): True if a weapon switch occurred, False otherwise.
        """
        switched = False
        switch_delay = 0.5 
        current_time = pg.time.get_ticks() / 1000.0 
        if current_time - self.last_switch_time >= switch_delay:
            if keys[K_e]:
                # Use list iteration to switch to the next projectile type
                index = (self.projectile_types.index(self.projectileType) + 1) % len(self.projectile_types)
                self.projectileType = self.projectile_types[index]
                switched = True
                self.last_switch_time = current_time
        return switched

    def shoot(self, keys, shotDelta, enemies, player, projectiles):
        """
        Handles shooting projectiles based on user input.

        Args:
            keys: The dictionary of currently pressed keys.
            shotDelta (float): Time since the last shot.
            enemies (pygame.sprite.Group): Group of enemies in the game.
            player (Player): The player object.
            projectiles (pygame.sprite.Group): Group of projectiles in the game.

        Returns:
            tuple: A tuple containing the updated shotDelta, enemies, projectiles, and player.
        """
        if keys[K_SPACE]:
            
            # List iteration to switch between player weapons
            shootDelay = [0.25, 0.05, 2][self.projectile_types.index(self.projectileType)]
            
            if shotDelta >= shootDelay:
                projectile = self.projectileType(self.rect, enemies, player, projectiles)
                projectile.shotfrom = "player"
                projectiles.add(projectile)
                shotDelta = 0
            
        return shotDelta, enemies, projectiles, player

    def hit(self, damageRecieved):
        """
        Handles the logic when the player is hit by a projectile.

        Args:
            damageReceived (int): The amount of damage received.
        """
        self.health -= damageRecieved
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        """
        Handles the logic when the player is destroyed.
        """
        self.kill()
