import asyncio
import platform
import pygame
import random
import math
from pygame import image, sprite, mouse, event, display, font, time, mixer, draw

X_IDX = 0
Y_IDX = 1
WIDTH_IDX = X_IDX
HEIGHT_IDX = Y_IDX
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_SPEED = 60
PLAY_CIRCLE_RADIUS = 324
PLAY_CIRCLE_CENTER_X = 0
PLAY_CIRCLE_CENTER_Y = 300
BULLET_OFFSET_X = 70
BULLET_OFFSET_Y = 18
BOX_MIN_X = 300
BOX_SIZE = 48
BULLET_OFFSCREEN_OFFSET = 100
Hit = 0
Bullets_Fired = 0
Bullets_Resolved = 0
Box_Rect = None
Space_Pressed = False

class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image.load("./assets/Gun.png")
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = mouse.get_pos()
        circle_center = (PLAY_CIRCLE_CENTER_X, PLAY_CIRCLE_CENTER_Y)
        radius = PLAY_CIRCLE_RADIUS

        # Calculate distance from mouse to circle center
        dx = mouse_pos[X_IDX] - circle_center[X_IDX]
        dy = mouse_pos[Y_IDX] - circle_center[Y_IDX]
        distance = math.sqrt(dx**2 + dy**2)

        if distance <= radius:
            # If mouse is inside the circle, move player to mouse position
            self.rect.center = mouse_pos
        else:
            # If mouse is outside, clamp position to the circle's edge
            # Normalize the direction vector and scale by radius
            if distance > 0:  # Avoid division by zero
                dx /= distance
                dy /= distance
                clamped_x = circle_center[X_IDX] + dx * radius
                clamped_y = circle_center[Y_IDX] + dy * radius
                self.rect.center = (clamped_x, clamped_y)

    def create_bullet(self):
        return Bullet(self.rect.x, self.rect.y)

class Bullet(sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = image.load("./assets/Bullet.png")
        self.rect = self.image.get_rect(center=(pos_x + BULLET_OFFSET_X, pos_y + BULLET_OFFSET_Y))

    def update(self):
        global Hit, Bullets_Fired, Bullets_Resolved, Box_Rect
        self.rect.x += 15
        if Box_Rect and self.rect.colliderect(Box_Rect):
            Hit += 1
            Bullets_Resolved += 1
            Box_Rect.x = random.randint(BOX_MIN_X, SCREEN_WIDTH - BOX_SIZE)
            Box_Rect.y = random.randint(0, SCREEN_HEIGHT - BOX_SIZE)
            self.kill()
        if self.rect.x >= SCREEN_WIDTH + self.rect.size[X_IDX]:
            Bullets_Resolved += 1
            self.kill()

def shoot(bullet_sound, player, bullet_group):
    global Bullets_Fired
    Bullets_Fired += 1
    bullet_group.add(player.create_bullet())
    bullet_sound.play()

async def main():
    global Hit, Bullets_Fired, Bullets_Resolved, Box_Rect, Space_Pressed
    # Initialize pygame
    pygame.init()
    running = True

    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display.set_caption("SHOOT THE BOX")
    clock = time.Clock()
    mouse.set_visible(False)
    Box_image = image.load("./assets/Box.png")
    Box_Rect = Box_image.get_rect()
    Box_Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Music and sound effects
    bullet_sound = mixer.Sound("./assets/BS2.mp3")
    mixer.music.load("./assets/SH.mp3")
    mixer.music.set_volume(0.8)
    mixer.music.play(-1, 0.0, 1000)

    # Text
    Rim_font = font.Font("./assets/rim.otf", 20)

    def show_score():
        acc = 100 if Bullets_Resolved == 0 else round((Hit / Bullets_Resolved) * 100, 2)
        score = Rim_font.render(
            f"Hits: {Hit}  Accuracy: {acc}%",
            True,
            (255, 20, 20),
            None,
        )
        score_rect = score.get_rect()
        screen.blit(score, score_rect)

    player = Player()
    player_group = sprite.Group()
    player_group.add(player)

    bullet_group = sprite.Group()

    while running:
        for eve in event.get():
            if eve.type == pygame.QUIT:
                running = False

            if eve.type == pygame.MOUSEBUTTONDOWN:
                shoot(bullet_sound, player, bullet_group)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False
        elif keys[pygame.K_SPACE] and not Space_Pressed:
            Space_Pressed = True
            shoot(bullet_sound, player, bullet_group)
        elif not keys[pygame.K_SPACE]:
            Space_Pressed = False

        screen.fill((255, 255, 255))
        draw.circle(screen, (0, 255, 0), (PLAY_CIRCLE_CENTER_X, PLAY_CIRCLE_CENTER_Y), PLAY_CIRCLE_RADIUS, 1000, False, False, False, False)
        screen.blit(Box_image, Box_Rect)
        player_group.draw(screen)
        bullet_group.draw(screen)
        bullet_group.update()
        player_group.update()
        show_score()
        display.update()
        clock.tick(GAME_SPEED)
        await asyncio.sleep(1.0 / GAME_SPEED)

    pygame.quit()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())