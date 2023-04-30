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

# Set the file to unknown state.
with open(file_path, "w") as f:
    f.write("9\n") 

while continue_playing:
    with open(file_path, "r") as f:
        lines = f.readlines()
        last_line = lines[-1].strip()

    # Check if the last line is a valid command
    if last_line == "01":
        # Stop the current song, if there is one
        if current_song is not None:
            os.system("killall aplay")
            time.sleep(1)  # wait for the current song to stop
        
        # Play the new song
        current_song = songs[idx]
        os.system(f"aplay -q {current_song} &")  # add "&" to run in the background
        # Set the file to unknown state.
        with open(file_path, "w") as f:
            f.write("9\n")      

    elif last_line == "02":
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
        # Set the file to unknown state.
        with open(file_path, "w") as f:
            f.write("9\n")   

    elif last_line == "03":
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
        # Set the file to unknown state.
        with open(file_path, "w") as f:
            f.write("9\n") 

    elif last_line == "04":
        # Stop the current song, if there is one
        if current_song is not None:
            os.system("killall aplay")
            current_song = None  # reset the current song variable
            idx = 0
        # Set the file to unknown state.
        with open(file_path, "w") as f:
            f.write("9\n") 
    else:
        pass
    
    # Wait for a few seconds before checking the file again
    time.sleep(2)
