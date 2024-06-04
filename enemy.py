"""
    Project: 8-bit Arcade, Star Wars Game 
    Version: 1.0
    Authors: Bailey Compton and Brandon Baker
    Class: Structures of Programming Languages
"""

from abc import abstractmethod, abstractproperty
import os
import pygame as pg

class Enemy(pg.sprite.Sprite):
    """"" 
        Enemy interface that defines enemy functionality
        
        Attributes:
            image (pygame.Surface): The image representing the enemy sprite.
            rect (pygame.Rect): The bounding rectangle for the enemy sprite.
            startLocation (tuple): The initial location of the enemy.
            direction (int): The direction of movement (-1 for left, 1 for right).
    """
    
    def __init__(self, startLocation):
        """
        Initializes an enemy object with default values.

        Args:
            startLocation (tuple): The initial location of the enemy.
        """
        super(Enemy, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'enemy1.png')).convert_alpha()
        self.rect = self.image.get_bounding_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self.startLocation = startLocation
        self.direction = 1

    @abstractproperty
    def speed(self):
        """
        Gets the speed of the enemy.

        Returns:
            int: The speed of the enemy.
        """
        pass

    @abstractproperty
    def health(self):
        """
        Gets the health of the enemy.

        Returns:
            int: The health of the enemy.
        """
        pass

    @abstractmethod
    def move(self, delta):
        """
        Abstract method for moving the enemy.

        Args:
            delta (float): Time difference between frames.
        """
        pass
    
    @abstractmethod
    def hit(self, damageReceived):
        """
        Abstract method for handling when the enemy is hit.

        Args:
            damageReceived (int): The amount of damage received.
        """
        self._health -= damageReceived
    
    @abstractmethod
    def attack(self):
        """
        Abstract method for initiating an attack.
        """
        pass
    
    @abstractmethod
    def destroy(self):
        """
        Abstract method for handling the destruction of the enemy.
        """
        self.kill()