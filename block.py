import pygame
import settings

class Block(pygame.sprite.Sprite):

    def __init__(self, colour, x, y):

        # Call the parent class (Sprite) constructor
        super().__init__()
        # Another way of doingf this is
        # pg.sprite.Sprite.__init__(self)

        # Create the image of the block of appropriate size
        self.image = pygame.Surface((settings.BLOCK_WIDTH,settings.BLOCK_HEIGHT))

        # Fill the image with the appropriate color
        self.image.fill(colour)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Move the top left of the rectangle to x,y.
        # This is where our block will appear..
        self.rect.x = x
        self.rect.y = y


