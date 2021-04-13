# Callan Murphy
# 21/11/19
# Main File
import sound
from startup import *

game_over = False
playing = True
# sound.theme_music()
while playing:

    pressed = pygame.key.get_pressed()
    # player movement
    if pressed[pygame.K_a]:
        for x in things:
            x.rect.x += SPEED
    if pressed[pygame.K_d]:
        for x in things:
            x.rect.x -= SPEED
    if pressed[pygame.K_w]:
        player.change_img("img/back.png")
        for x in things:
            x.rect.y += SPEED
    if pressed[pygame.K_s]:
        player.change_img("img/front.png")
        for x in things:
            x.rect.y -= SPEED
    player.check_boundary()

    fix_collisions(things + [player])

    for x in skeletons:
        if x.collided(player):
            sound.ow()
            healths[0] -= 1
            current_health = healths[healths[0]]
            skeletons.remove(x)
            things.remove(x)
            mobs.remove(x)
            if healths[0] == 1:
                game_over = True
        x.move_to_obj(player)
        x.check_boundary()

    for x in coins:
        if x.collided(player):
            sound.coin()
            coins.remove(x)
            things.remove(x)
            gold_total += 1
            gold_total_text = font.render(str(gold_total), True, (255, 255, 255))

    # screen display
    screen.fill((15, 15, 15))
    if game_over:
        screen.blit(game_over_text, game_over_rect)
    else:
        for x in things:
            screen.blit(x.img, x.rect)
        screen.blit(current_health.img, current_health.rect)
        screen.blit(player.img, player.rect)
        screen.blit(health_text, health_text_rect)
        screen.blit(gold, gold_rect)
        screen.blit(gold_total_text, gold_total_text_rect)
    pygame.display.flip()

    # quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                playing = False

    clock.tick(60)
