import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.init()
        pygame.mixer.init()
        self.playing = False
        self.playlist = []  
        self.current_track_index = 0
        self.load_music(music_folder)
        self.screen = pygame.display.set_mode((300, 200))
        self.clock = pygame.time.Clock()
        self.player_img = pygame.image.load("lab7/player.png")
        self.player_rect = self.player_img.get_rect(center=(150, 100))

    def load_music(self, folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".mp3"):
                self.playlist.append(os.path.join(folder_path, file))

    def play(self):
        if not pygame.mixer.music.get_busy() and self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track_index])
            pygame.mixer.music.play()
            self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next_track(self):
        if self.current_track_index < len(self.playlist) - 1:
            self.current_track_index += 1
            self.play()
        else:
            self.stop()

    def prev_track(self):
        if self.current_track_index > 0:
            self.current_track_index -= 1
            self.play()
        else:
            self.stop()

    def draw_player(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.player_img, self.player_rect)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.playing:
                        self.stop()
                    else:
                        self.play()
                elif event.key == pygame.K_RIGHT:
                    self.next_track()
                elif event.key == pygame.K_LEFT:
                    self.prev_track()

    def run(self):
        while True:
            self.handle_events()
            self.draw_player()
            self.clock.tick(30)

if __name__ == "__main__":
    player = MusicPlayer("lab7\music")
    player.run()
