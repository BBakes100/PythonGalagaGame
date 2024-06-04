"""
    Project: 8-bit Arcade, Star Wars Game 
    Version: 1.0
    Authors: Bailey Compton and Brandon Baker
    Class: Structures of Programming Languages
"""

import os
from projectile import Projectile
import pygame as pg
from dimensions import Dimensions as dim

class Rocket(Projectile):
    """
    Rocket Class inherits a projectile and defines custom functionality.

    Attributes:
        _speed (int): The speed of the rocket projectile.
        _damage (int): The damage inflicted by the rocket projectile.
    """

    def __init__(self, shipLocation, enemies, player, projectiles):
        """
        Initializes a rocket projectile with default values.

        Args:
            shipLocation (pygame.Rect): The initial location of the ship firing the rocket.
            enemies (pygame.sprite.Group): Group of enemies in the game.
            player (Player): The player object.
            projectiles (pygame.sprite.Group): Group of projectiles in the game.
        """
        Projectile.__init__(self, shipLocation, enemies, player, projectiles)
        og_image = pg.image.load(os.path.join('assets', 'rocket.png')).convert_alpha()
        image_rect = og_image.get_bounding_rect()
        self.image = og_image.subsurface(image_rect)
        self.image = pg.transform.scale(self.image, (dim.rock_w, dim.rock_h))
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.x + 57
        self.rect.centery = shipLocation.y - 25
        self._speed = 150
        self._damage = 150

    @property
    def speed(self):
        """
        Gets the speed of the rocket projectile.

        Returns:
            int: The speed of the rocket projectile.
        """
        return self._speed
    
    @speed.setter
    def speed(self, value):
        """
        Sets the speed of the rocket projectile.

        Args:
            value (int): The new speed value.
        """
        self._speed = value

    @property
    def damage(self):
        """
        Gets the damage inflicted by the rocket projectile.

        Returns:
            int: The damage inflicted by the rocket projectile.
        """
        return self._damage
    
    @damage.setter
    def damage(self, value):
        """
        Sets the damage inflicted by the rocket projectile.

        Args:
            value (int): The new damage value.
        """
        self._damage = value

    def move(self, delta):
        """
        Moves the rocket projectile.

        Args:
            delta (float): Time difference between frames.
        """
        super().move(delta)
        
    def destroy(self):
        """
        Destroys the rocket projectile.
        """
        super().destroy()
