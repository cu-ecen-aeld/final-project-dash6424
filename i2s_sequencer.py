import os
import time

# Define the file path and songs
file_path = "audio_test.txt"
song1_path = "test.wav"
song2_path = "Front_Center.wav"

# Get the initial modification time of the file
last_mtime = os.stat(file_path).st_mtime

# Initialize the flag variable to True
continue_playing = True

# Initialize the current song variable
current_song = None

while continue_playing:
    # Check the modification time of the file
    mtime = os.stat(file_path).st_mtime

    # If the file has been modified since the last check, read it and get the last line
    if mtime > last_mtime:
        with open(file_path, "r") as f:
            lines = f.readlines()
            last_line = lines[-1].strip()

        # Check if the last line is a valid command
        if last_line == "1":
            # Stop the current song, if there is one
            if current_song is not None:
                os.system("killall aplay")
                time.sleep(1)  # wait for the previous song to stop

            # Play the new song
            current_song = song1_path
            os.system(f"aplay -q {current_song} &")  # add "&" to run in the background

        elif last_line == "2":
            # Stop the current song, if there is one
            if current_song is not None:
                os.system("killall aplay")
                time.sleep(1)  # wait for the previous song to stop

            # Play the new song
            current_song = song2_path
            os.system(f"aplay -q {current_song} &")  # add "&" to run in the background

        elif last_line == "3":
            # Stop the current song, if there is one
            if current_song is not None:
                os.system("killall aplay")
                current_song = None  # reset the current song variable

        # Update the last modification time
        last_mtime = mtime

    # Wait for a few seconds before checking the file again
    time.sleep(2)
