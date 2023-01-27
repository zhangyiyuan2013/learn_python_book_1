import pygame,sys
pygame.init()

screen = pygame.display.set_mode([640,480])

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
splat = pygame.mixer.Sound("splat.wav")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pygame.mixer.music.get_busy():  # Checks if the music is done playing
        splat.play()
        pygame.time.delay(1000)  # Waits 1 second for the "splat" sound to finish
        running = False
pygame.quit()
