import pygame, sys, random

Hit = 1
BFired = 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "./assets/Gun.png"
        )

        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))

    def update(self):
        if (284, 0) > pygame.mouse.get_pos():
            self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(
            "./assets/Bullet.png"
        )
        self.rect = self.image.get_rect(center=(pos_x + 35, pos_y - 13))

    def update(self):
        global Hit
        self.rect.x += 15
        if self.rect.colliderect(box_rect):
            Hit += 1
            box_rect.x = random.randint(300, screen_width - 48)
            box_rect.y = random.randint(0, screen_height - 48)
            self.kill()
        if self.rect.x >= screen_width + 100:
            self.kill()


# initialize pygame
pygame.init()


# Basic code
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SHOOT THE BOX")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
Box_image = pygame.image.load(
    "./assets/Box.png"
)
box_rect = Box_image.get_rect()
box_rect.center = (screen_width // 2, screen_height // 2)


# Music and sound effects
sound_1 = pygame.mixer.Sound(
    "./assets/BS2.mp3"
)
pygame.mixer.music.load("./assets/SH.mp3")
pygame.mixer.music.play(-1, 0.0)


# Text
font = pygame.font.Font("./assets/rim.otf", 20)


def show_score():
    score = font.render(
        "Hits: "
        + str(Hit - 1)
        + "  Accuracy: "
        + str(round((Hit / BFired) * 100, 2))
        + "%",
        True,
        (255, 0, 0),
        None,
    )
    score_rect = score.get_rect()
    screen.blit(score, score_rect)


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (284, 0) > pygame.mouse.get_pos():
                BFired += 1
                bullet_group.add(player.create_bullet())
                sound_1.play()

    screen.fill((255, 255, 255))
    pygame.draw.circle(
        screen, (0, 255, 0), (0, 300), 324, 1000, False, False, False, False
    )
    screen.blit(Box_image, box_rect)
    player_group.draw(screen)
    bullet_group.draw(screen)
    bullet_group.update()
    player_group.update()
    show_score()
    pygame.display.update()
    clock.tick(60)