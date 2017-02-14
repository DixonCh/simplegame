
import constants
import pygame
import os, sys


class SpriteSheet:

    sprite_sheet = None

    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(self.resource_path(os.path.join('resources',filename))).convert()

    def resource_path(self, relative):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative)
        return os.path.join(relative)

    def get_image(self, x, y, width, height):

        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image
