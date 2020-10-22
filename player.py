import pygame
import settings

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
         # Another way of doingf this is
        # pg.sprite.Sprite.__init__(self)

        self.width = 150
        self.height = 15

        # Make our top-left corner the passed-in location.
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((settings.YELLOW))

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = settings.SCREEN_HEIGHT - self.height

    def update(self):
        # Get where the mouse is
        pos = pygame.mouse.get_pos()

        # Set the left side of the player bar to the mouse position
        self.rect.x = pos[0]

        # Make sure we don't push the player paddle
        # off the right side of the screen
        if self.rect.x > settings.SCREEN_WIDTH - self.width:
            self.rect.x = settings.SCREEN_WIDTH - self.width
