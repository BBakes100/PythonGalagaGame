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

class Lazer(Projectile):
    """
    Lazer Class inherits a projectile and defines custom functionality.
    
    Attributes:
        _speed (int): The speed of the lazer projectile.
        _damage (int): The damage inflicted by the lazer projectile.
    """

    def __init__(self, shipLocation, enemies, player, projectiles):
        """
        Initializes a lazer projectile with default values.

        Args:
            shipLocation (pygame.Rect): The initial location of the ship firing the lazer.
            enemies (pygame.sprite.Group): Group of enemies in the game.
            player (Player): The player object.
            projectiles (pygame.sprite.Group): Group of projectiles in the game.
        """
        # Call the constructor of the base class (Projectile)
        Projectile.__init__(self, shipLocation, enemies, player, projectiles)

        # Load and scale the lazer image
        og_image = pg.image.load(os.path.join('assets', 'lazer.png')).convert_alpha()
        image_rect = og_image.get_bounding_rect()
        self.image = og_image.subsurface(image_rect)
        self.image = pg.transform.scale(self.image, (dim.laz_w, dim.laz_h))

        # Set the initial location of the lazer
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.x + 57
        self.rect.centery = shipLocation.y - 3

        # Default values for lazer attributes
        self._speed = 500
        self._damage = 5

    @property
    def speed(self):
        """
        Gets the speed of the lazer projectile.

        Returns:
            int: The speed of the lazer projectile.
        """
        return self._speed
    
    @speed.setter
    def speed(self, value):
        """
        Sets the speed of the lazer projectile.

        Args:
            value (int): The new speed value.
        """
        self._speed = value

    @property
    def damage(self):
        """
        Gets the damage inflicted by the lazer projectile.

        Returns:
            int: The damage inflicted by the lazer projectile.
        """
        return self._damage
    
    @damage.setter
    def damage(self, value):
        """
        Sets the damage inflicted by the lazer projectile.

        Args:
            value (int): The new damage value.
        """
        self._damage = value    

    def move(self, delta):
        """
        Moves the lazer projectile.

        Args:
            delta (float): Time difference between frames.
        """
        super().move(delta)
        
    def destroy(self):
        """
        Destroys the lazer projectile.
        """
        super().destroy()
