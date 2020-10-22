import pygame
import settings
import math

class Ball(pygame.sprite.Sprite):

    def __init__(self):

        # Call the parent class (Sprite) constructor
        super().__init__()
        # Another way of doingf this is
        # pg.sprite.Sprite.__init__(self)

        # Speed in pixels per cycle
        self.speed = settings.BALL_INIT_SPEED

        # Floating point representation of where the ball is
        self.x = 0.0
        self.y = 180.0

        # Direction of ball (in degrees)
        self.direction = settings.BALL_INIT_DIRECTION

        self.height = settings.BALL_HEIGHT
        self.width = settings.BALL_WIDTH

        # Create the image of the ball
        self.image = pygame.Surface((self.width,self.height))

        # Color the ball
        self.image.fill(settings.WHITE)

        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()

    def update(self):
        # Update the position of the ball.

        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)

        # Change the position (x and y) according to the speed and direction
        # x = x + .....
        self.x += self.speed * math.sin(direction_radians)

        # y = y - ......
        self.y -= self.speed * math.cos(direction_radians)

        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y

        # Do we bounce off the top of the screen?
        if self.y <= 0 :
            self.bounce(0)
            self.y = 1

       # Do we bounce off the left of the screen?
        if self.x <= 0:
            self.direction = self.deflection()
            self.x = 1

        # Do we bounce of the right side of the screen?
        if self.x > settings.SCREEN_WIDTH - self.width:
            self.direction = self.deflection()
            self.x = settings.SCREEN_WIDTH - self.width - 1

        # Did we fall off the bottom edge of the screen?
        if self.y > settings.SCREEN_HEIGHT:
            return True
        else:
            return False

    def bounce(self, diff):
        # This function will bounce the ball off a horizontal surface 
        # (not a vertical one)
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def deflection(self):
        # This function will bounce the ball off a vertical surface 
        # (not a horizontal one)
        return (360 - self.direction) % 360