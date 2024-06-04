"""
    Project: 8-bit Arcade, Star Wars Game 
    Version: 1.0
    Authors: Bailey Compton and Brandon Baker
    Class: Structures of Programming Languages
"""

from enemy import Enemy
import pygame as pg
import os
from dimensions import Dimensions as dim
from pellet import Pellet

class Harmless(Enemy):
    """
    Harmless class inherits from the Enemy class and defines custom functionality for movement and attacking.

    Attributes:
        _speed (int): The speed of the Harmless enemy.
        _health (int): The health of the Harmless enemy.
    """
    def __init__(self, startLocation):
        """
        Initializes a Harmless enemy with default values.

        Args:
            startLocation (tuple): The initial location of the Harmless enemy.
        """
        Enemy.__init__(self, startLocation)
        og_image = pg.image.load(os.path.join('assets', 'enemy1.png')).convert_alpha()
        image_rect = og_image.get_bounding_rect()
        self.image = og_image.subsurface(image_rect)
        self.image = pg.transform.scale(self.image, (dim.harm_w_h, dim.harm_w_h))
        self.rect = self.image.get_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self._speed = 200
        self._health = 20

    @property
    def speed(self):
        """
        Gets the speed of the Harmless enemy.

        Returns:
            int: The speed of the Harmless enemy.
        """
        return self._speed
    
    @speed.setter
    def speed(self, value):
        """
        Sets the speed of the Harmless enemy.

        Args:
            value (int): The new speed value.
        """
        self._speed = value

    @property
    def health(self):
        """
        Gets the health of the Harmless enemy.

        Returns:
            int: The health of the Harmless enemy.
        """
        return self._health
    
    @health.setter
    def health(self, value):
        """
        Sets the health of the Harmless enemy.

        Args:
            value (int): The new health value.
        """
        self._health = value

    def move(self, delta):
        """
        Moves the Harmless enemy horizontally within a specified range.

        Args:
            delta (float): Time difference between frames.
        """
        self.rect.x += self.speed * delta * self.direction
        if self.rect.x > self.startLocation[0] + 100 or self.rect.x < self.startLocation[0] - 100:
            self.direction *= -1
            
    def hit(self, damageReceived):
        """
        Handles the logic when the Harmless enemy is hit by a projectile.

        Args:
            damageReceived (int): The amount of damage received.
        """
        super().hit(damageReceived)
        
    def destroy(self):
        """
        Handles the logic when the Harmless enemy is destroyed.
        """
        super().destroy()
