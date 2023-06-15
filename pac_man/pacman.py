import pygame

pygame.init()

yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)


screen = pygame.display.set_mode((800, 600), 0)


speed = 1
speed_x = speed
speed_y = speed

class Pacman:
    def __init__(self):
        self.mid_x = 400
        self.mid_y = 300
        self.size = 50
        self.radius  =  self.size // 2
        self.speed = 1
        self.speed_x = speed
        self.speed_y = speed
    
    def calc_rules(self):
        # self.colun = self.colun + self.speed_x
        # self.line = self.linha + self.speed_y
        self.mid_x = int(self.mid_x + self.size)
        self.mid_y = int(self.mid_y + self.size)

       
        if self.mid_x + self.radius > 800:
            self.speed_x = -speed
        if self.mid_x - self.radius < 0:
            self.speed_x = speed
        if self.mid_y + self.radius  > 600:
            self.speed_y = -speed
        if self.mid_y+ self.radius < 0:
            self.speed_y = speed


    def drawer(self, screen):
        pygame.draw.circle(screen, yellow, (self.mid_x, self.mid_y), self.radius, 0)

        mouth_corner = (self.mid_x, self.mid_y )
        mouth_upper = (self.mid_x + self.radius, self.mid_y - self.radius)
        mouth_lower = (self.mid_x + self.radius, self.mid_y + self.radius)
        mouth = [mouth_corner, mouth_upper, mouth_lower]

        pygame.draw.polygon(screen, black, mouth, 0)


        #olho do pacman
        eyes_x = int(self.mid_x + self.radius / 3.5)
        eyes_y = int(self.mid_y - self.radius / 1.5)
        eyes_radius = int(self.radius / 8)

        pygame.draw.circle(screen, black, (eyes_x, eyes_y), eyes_radius, 0)

pygame.display.set_caption("Pacman")

pacman = Pacman()

while True:
   
    pacman.calc_rules()

    pacman.drawer(screen)
    screen.fill(black)
    pygame.display.update()


    for e in  pygame.event.get():
        if e.type == pygame.QUIT:
            exit()