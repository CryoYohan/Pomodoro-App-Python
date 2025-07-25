import pygame
# from tkinter import filedialog # Removed as it's not used

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        # Add a flag to track if music has been loaded successfully
        self.music_loaded = False

    def load_music(self, file_name):
        """
        Loads a  music file.
        Includes basic error handling for file not found/corrupt.
        """
        try:
            pygame.mixer.music.load(file_name)
            self.music_loaded = True
            print(f"Music loaded: {file_name}")
        except pygame.error as e:
            print(f"Error loading music '{file_name}': {e}")
            self.music_loaded = False

    def play_music(self):
        """Plays the loaded music."""
        if self.music_loaded:
            if not pygame.mixer.music.get_busy(): # Only play if not already playing
                pygame.mixer.music.play(loops=-1)
                print("Music started.")
            else:
                print("Music is already playing.")
        else:
            print("No music loaded. Please call load_music() first.")

    def pause_music(self):
        """Pauses the currently playing music."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            print("Music paused.")
        else:
            print("No music is currently playing to pause.")

    def stop_music(self):
        """Stops the music and rewinds it."""
        if self.music_loaded and (pygame.mixer.music.get_busy() or pygame.mixer.music.get_pos() != -1):
            pygame.mixer.music.stop()
            print("Music stopped.")
        else:
            print("No music is currently playing or loaded to stop.")

    def __del__(self):
        """Ensures Pygame mixer is quit when the object is destroyed."""
        pygame.mixer.quit()
        print("Pygame mixer quit.")
