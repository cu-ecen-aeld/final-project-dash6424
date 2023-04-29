import os
import time

# Define the file path and songs
# Set the audio files
songs = ["test1.wav", "test2.wav", "test3.wav", "test4.wav"]
file_path = "audio_test.txt"

# Initialize the flag variable to True
continue_playing = True

# Initialize the current song variable
current_song = None
idx = 0

bool1 = False
bool2 = False
bool3 = False

while continue_playing:
        with open(file_path, "r") as f:
            lines = f.readlines()
            last_line = lines[-1].strip()

        # Check if the last line is a valid command
        if last_line == "1":
            bool2 = False
            bool3 = False
            if bool1 == False:
                # Stop the current song, if there is one
                if current_song is not None:
                    os.system("killall aplay")
                    time.sleep(1)  # wait for the current song to stop
                
                # Play the new song
                current_song = songs[idx]
                os.system(f"aplay -q {current_song} &")  # add "&" to run in the background
                bool1 = True

        elif last_line == "2":
            bool1 = False
            bool3 = False
            if bool2 == False:
                # Stop the current song, if there is one
                if current_song is not None:                
                    os.kill(os.getpid(), 2)  # add "&" to run in the background
                bool2 = True

        elif last_line == "3":
            bool1 = False
            bool2 = False
            bool3 = False
            # Stop the current song, if there is one
            if current_song is not None:
                os.system("killall aplay")
                time.sleep(1)  # wait for the current song to stop
            
            # Play the previous song
            idx = idx - 1
            if idx < 0:
                idx = 3
            current_song = songs[idx]
            os.system(f"aplay -q {current_song} &")  # add "&" to run in the background

        elif last_line == "4":
            bool1 = False
            bool2 = False
            bool3 = False
            # Stop the current song, if there is one
            if current_song is not None:
                os.system("killall aplay")
                time.sleep(1)  # wait for the current song to stop
            
            # Play the next song
            idx = idx + 1
            if idx == 4:
                idx = 0
            current_song = songs[idx]
            os.system(f"aplay -q {current_song} &")  # add "&" to run in the background

        elif last_line == "5":
            bool1 = False
            bool2 = False
            if bool3 == False:
                # Stop the current song, if there is one
                if current_song is not None:
                    os.system("killall aplay")
                    current_song = None  # reset the current song variable
                    idx = 0
                    bool3 = True

    # Wait for a few seconds before checking the file again
    time.sleep(2)