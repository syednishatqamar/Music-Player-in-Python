

import os
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.playlists = {}
        self.current_playlist = None
        self.current_song = None

    def load_playlists(self):
        playlists = {}
        for root, dirs, files in os.walk('./playlists'):
            for file in files:
                if file.endswith('.txt'):
                    playlist_name = file.split('.')[0]
                    with open(os.path.join(root, file), 'r') as f:
                        songs = f.read().splitlines()
                        playlists[playlist_name] = songs
        return playlists

    def save_playlist(self, playlist_name):
        if playlist_name in self.playlists:
            with open(f'./playlists/{playlist_name}.txt', 'w') as f:
                for song in self.playlists[playlist_name]:
                    f.write(song + '\n')

    def create_playlist(self, playlist_name):
        self.playlists[playlist_name] = []

    def add_to_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].append(song)

    def list_playlists(self):
        print("Playlists:")
        for playlist in self.playlists:
            print(f"- {playlist}")

    def list_songs(self, playlist_name):
        if playlist_name in self.playlists:
            print(f"Songs in {playlist_name}:")
            for i, song in enumerate(self.playlists[playlist_name], 1):
                print(f"{i}. {song}")

    def play_song(self, song):
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()

    def run(self):
        self.playlists = self.load_playlists()

        while True:
            print("\n1. List Playlists")
            print("2. Create Playlist")
            print("3. List Songs in Playlist")
            print("4. Add Song to Playlist")
            print("5. Play Song")
            print("6. Stop Song")
            print("7. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.list_playlists()
            elif choice == '2':
                playlist_name = input("Enter playlist name: ")
                self.create_playlist(playlist_name)
                self.save_playlist(playlist_name)
            elif choice == '3':
                playlist_name = input("Enter playlist name: ")
                self.list_songs(playlist_name)
            elif choice == '4':
                playlist_name = input("Enter playlist name: ")
                song = input("Enter song name: ")
                self.add_to_playlist(playlist_name, song)
                self.save_playlist(playlist_name)
            elif choice == '5':
                song = input("Enter song name: ")
                self.play_song(song)
            elif choice == '6':
                self.stop_song()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()

