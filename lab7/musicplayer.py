import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playing = False
        self.playlist = []
        self.current_track_index = 0

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.playing:
                        self.stop()
                    else:
                        self.play()
                elif event.key == pygame.K_RIGHT:
                    self.next_track()
                elif event.key == pygame.K_LEFT:
                    self.prev_track()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

if __name__ == "__main__":
    player = MusicPlayer()
    player.load_music("lab7\music")

    while True:
        player.handle_events()
