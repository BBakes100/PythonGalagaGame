"""
    Project: 8-bit Arcade, Star Wars Game 
    Version: 1.0
    Authors: Bailey Compton and Brandon Baker
    Class: Structures of Programming Languages
"""

from abc import abstractmethod, abstractproperty
import os
import pygame as pg
from enemy import Enemy

class Projectile(pg.sprite.Sprite):
    """
    Projectile interface that defines projectile functionality.

    Attributes:
        image: The image of the projectile.
        rect: The bounding rectangle of the projectile.
        enemies: Group of enemy sprites.
        player: Player instance.
        projectiles: Group of projectile sprites.
        event: Pygame event type.
        shotfrom (str): The entity from which the projectile was shot ("player" or "enemy").
        rotated (bool): Flag indicating whether the projectile image has been rotated.
    """

    def __init__(self, shipLocation, enemies, player, projectiles):
        """
        Projectile constructor that sets default values.

        Args:
            shipLocation: Projectile starting location.
            enemies: Group of enemy sprites.
            player: Player instance.
            projectiles: Group of projectile sprites.
        """
        super(Projectile, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'pellet.png')).convert_alpha()
        self.rect = self.image.get_bounding_rect()
        self.enemies = enemies
        self.player = player
        self.projectiles = projectiles
        self.event = pg.USEREVENT + 1
        self.shotfrom = ""
        self.rotated = False

    @abstractproperty
    def speed(self):
        """
        Abstract property representing the speed of the projectile.
        """
        pass

    @abstractproperty
    def damage(self):
        """
        Abstract property representing the damage inflicted by the projectile.
        """
        pass

    @abstractmethod
    def move(self, delta):
        """
        Move method to control the movement of a projectile.

        Args:
            delta: Time difference between frames.
        """
        projectiles_to_destroy = []

        if self.shotfrom == "player":
            self.rect.y -= self._speed * delta
            if self.rect.y < -100:
                self.destroy()
            collision = pg.sprite.spritecollideany(self, self.enemies)
            if collision:
                collision.hit(self._damage)
                if collision.health <= 0:
                    collision.destroy()
                pg.event.post(pg.event.Event(self.event))
                self.destroy()
            for projectile in pg.sprite.spritecollide(self, self.projectiles, False):
                if projectile.shotfrom == "enemy":
                    projectiles_to_destroy.append(projectile)

        if self.shotfrom == "enemy":
            self.rect.y += self._speed / 2 * delta
            if self.rect.y > 800:
                self.destroy()
            if self.rect.colliderect(self.player.rect):
                self.player.hit(self._damage)
                pg.event.post(pg.event.Event(self.event))
                self.destroy()
            for projectile in pg.sprite.spritecollide(self, self.projectiles, False):
                if projectile.shotfrom == "player":
                    projectiles_to_destroy.append(projectile)

        if self.shotfrom == "enemy" and not self.rotated:
            self.image = pg.transform.rotate(self.image, 180)
            self.rotated = True

        for projectile in projectiles_to_destroy:
            projectile.destroy()

    @abstractmethod
    def destroy(self):
        """
        Destroy method that removes the projectile from the projectile sprite group.
        """
        self.kill()
