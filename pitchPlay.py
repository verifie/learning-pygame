# pitchPlay.py

# Dependencies: numpy, pygame
# pip install pygame


# Import modules
import time
import pygame
import numpy as np


# ========================================================================================
# Code to play beep sound

# Initialize the mixer module
pygame.mixer.init()

# Create a sound buffer with a given frequency and duration
# Function to generate a beep sound
def generate_beep(frequency, duration):
    sample_rate = 44100  # Sample rate in Hz
    n_samples = int(sample_rate * duration / 1000.0)  # Convert duration from milliseconds to samples

    # Generate a waveform array
    t = np.linspace(0, duration / 1000.0, n_samples, endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * t)

    # Convert waveform to 16-bit signed integers
    waveform = np.int16(waveform * 32767)

    # Repeat the waveform in 2 columns for stereo (left and right channels)
    stereo_waveform = np.column_stack((waveform, waveform))

    # Create the sound object from the stereo waveform
    sound = pygame.mixer.Sound(buffer=stereo_waveform)
    return sound

def pitchscale():
    # Define the pitch frequency range and parameters
    low_pitch = 1
    high_pitch = 25000
    pitch_step = 1
    duration = 500
    pause = 0.1

    # Roll through the pitch frequency range and play a beep sound
    print("Playing pitch scale")

    for pitch_frequency in range(low_pitch, high_pitch, pitch_step):
        print("Playing beep at frequency: ", pitch_frequency)
        beep = generate_beep(pitch_frequency, duration)  # frequency, ms duration
        beep.play()
        time.sleep(pause)


# ========================================================================================

def middle_c():
    print("Playing Middle C")
    # Middle C
    frequency = 261.63
    duration = 1000
    pause = 0.1

    # Generate a beep sound
    beep = generate_beep(frequency, duration)
    beep.play()
    time.sleep(pause)


# ========================================================================================
# Run the programs

middle_c()
pitchscale()

