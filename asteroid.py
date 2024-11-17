import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            first_vel = self.velocity.rotate(angle)
            second_vel = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first = Asteroid(self.position.x, self.position.y, new_radius)
            second = Asteroid(self.position.x, self.position.y, new_radius)

            first.velocity = first_vel * 1.2
            second.velocity = second_vel * 1.2