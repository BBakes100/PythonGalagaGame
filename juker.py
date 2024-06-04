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
import math
from pellet import Pellet

class Juker(Enemy):
    """
    Juker class inherits an enemy and defines custom functionality for movement and attacking.
    
    Attributes:
        projectileType: The type of projectile used by the Juker.
        _speed (int): The speed of the Juker.
        _health (int): The health of the Juker.
        __dir (int): The direction of movement (-1 for left, 1 for right).
        __shot_delta (float): The time since the last shot.
        __shoot_delay (float): The delay between shots.
        __attack_cooldown (float): The cooldown time between attacks.
        __time_since_last_attack (float): The time elapsed since the last attack.
    """
    def __init__(self, startLocation):
        """
        Creates a Juker enemy ship and assigns default values.

        Args:
            startLocation: The start location of the enemy ship.
        """
        Enemy.__init__(self, startLocation)
        og_image = pg.image.load(os.path.join('assets', 'enemy2.png')).convert_alpha()
        image_rect = og_image.get_bounding_rect()
        self.image = og_image.subsurface(image_rect)
        self.image = pg.transform.scale(self.image, (dim.juker_w_h, dim.juker_w_h))
        self.rect = self.image.get_rect()
        self.rect.center = (startLocation[0], startLocation[1])
        self.projectileType = Pellet
        self._speed = 200
        self._health = 100
        self.__dir = 1
        self.__shot_delta = 0
        self.__shoot_delay = 0.25
        self.__attack_cooldown = 2.0 
        self.__time_since_last_attack = 0.0

    def move(self, delta):
        """
        Moves Juker sprite across the screen in a sin wave motion.

        Args:
            delta (float): Time difference between frames.
        """
        # Move in a sin wave motion until both ends of screen before flipping
        self.rect.x += self._speed * delta * self.__dir
        self.rect.y = (100 * math.sin(2 * self.rect.x / 200)) + 600 // 2

        if self.rect.x >= 1024:
            self.__dir = -1
            
        if self.rect.x <= 0:
            self.__dir = 1
    
    def attack(self, delta, enemies, player, projectiles):
        """
        Initiates an attack by firing projectiles.

        Args:
            delta (float): Time difference between frames.
            enemies (pygame.sprite.Group): Group of enemies in the game.
            player (Player): The player object.
            projectiles (pygame.sprite.Group): Group of projectiles in the game.

        Returns:
            tuple: A tuple containing the updated projectile group and player object.
        """
        self.__time_since_last_attack += delta
        self.__shot_delta += delta

        if self.time_since_last_attack >= self.attack_cooldown:
            projectile = self.projectileType(self.rect, enemies, player, projectiles)
            projectile.shotfrom = "enemy"
            projectiles.add(projectile)
            self.__time_since_last_attack = 0.0
            self.__shot_delta = 0

        return projectiles, player
            
    def hit(self, damageRecieved):
        """
        Handles the logic when the Juker is hit by a projectile.

        Args:
            damageReceived (int): The amount of damage received.
        """
        super().hit(damageRecieved)
        
    def destroy(self):
        """
        Handles the logic when the Juker is destroyed.
        """
        super().destroy()
        
    @property
    def speed(self):
        """
        Gets the speed of the Juker.

        Returns:
            int: The speed of the Juker.
        """
        return self._speed
    
    @speed.setter
    def speed(self, value):
        """
        Sets the speed of the Juker.

        Args:
            value (int): The new speed value.
        """
        self._speed = value

    @property
    def health(self):
        """
        Gets the health of the Juker.

        Returns:
            int: The health of the Juker.
        """
        return self._health
    
    @health.setter
    def health(self, value):
        """
        Sets the health of the Juker.

        Args:
            value (int): The new health value.
        """
        self._health = value
        
    @property
    def shot_delta(self):
        """
        Gets the time since the last shot.

        Returns:
            float: Time since the last shot.
        """
        return self.__shot_delta
    
    @shot_delta.setter
    def shot_delta(self, value):
        """
        Sets the time since the last shot.

        Args:
            value (float): The new value for time since the last shot.
        """
        self.__shot_delta = value
        
    @property
    def shoot_delay(self):
        """
        Gets the delay between shots.

        Returns:
            float: The delay between shots.
        """
        return self.__shoot_delay
    
    @shoot_delay.setter
    def shoot_delay(self, value):
        """
        Sets the delay between shots.

        Args:
            value (float): The new value for the delay between shots.
        """
        self.__shoot_delay = value
        
    @property
    def attack_cooldown(self):
        """
        Gets the cooldown time between attacks.

        Returns:
            float: The cooldown time between attacks.
        """
        return self.__attack_cooldown
    
    @attack_cooldown.setter
    def attack_cooldown(self, value):
        """
        Sets the cooldown time between attacks.

        Args:
            value (float): The new value for the cooldown time between attacks.
        """
        self.__attack_cooldown = value
        
    @property
    def time_since_last_attack(self):
        """
        Gets the time elapsed since the last attack.

        Returns:
            float: Time elapsed since the last attack.
        """
        return self.__time_since_last_attack
    
    @time_since_last_attack.setter
    def time_since_last_attack(self, value):
        """
        Sets the time elapsed since the last attack.

        Args:
            value (float): The new value for the time elapsed since the last attack.
        """
        self.__time_since_last_attack = value
