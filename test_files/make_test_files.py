"""Build test data files for the hearing aid simulator. This script is very
simple but gets the job done.
"""

import numpy as np
import wave

SAMPLE_RATE = 16000 # samples per second
FILE_LENGTH_SECONDS = 10
MAX_ALLOWED_FILE_LENGTH = 160000

def write_file(filename, length, data):
    """Write a .dat file given an integer length and float32 data."""
    if data.dtype != np.float32:
        print("data must be float32")
        return
    if length > MAX_ALLOWED_FILE_LENGTH:
        print("max allowed file length is {}".format(MAX_ALLOWED_FILE_LENGTH))
        return
    
    outfile = open(filename, "wb")
    outfile.write(np.array([length], dtype='uint32').tobytes())
    outfile.write(data.tobytes())
    outfile.close()
    
def make_tone_file():
    """Create a .dat file with a 2kHz tone"""
    length = SAMPLE_RATE * FILE_LENGTH_SECONDS
    t = np.linspace(0, FILE_LENGTH_SECONDS, FILE_LENGTH_SECONDS * SAMPLE_RATE + 1)[0:-1]
    tone = (0.01 * np.sin(2 * np.pi * 2000 * t)).astype('float32')
    write_file("tone.dat", length, tone)

def make_noise_file():
    """Create a .dat file with white noise."""
    length = SAMPLE_RATE * FILE_LENGTH_SECONDS
    noise = (0.01 * np.random.normal(size = SAMPLE_RATE * FILE_LENGTH_SECONDS)).astype('float32')
    write_file("noise.dat", length, noise)
    
def make_voice_file():
    """Reformat a wave file into the desired format. Intended to be used with 
    16b 16kSps PCM audio only. Does not check the sample rate, so it can do
    some strange things. 
    Sample audio source: https://www.youtube.com/watch?v=zG-nZxpanO8
    """
    infile = wave.open("talking.wav")
    if (infile.getnchannels() != 1) or (infile.getsampwidth() != 2):
        print("only mono 16b PCM supported")
        return
    length = infile.getnframes()
    if length > MAX_ALLOWED_FILE_LENGTH:
        length = MAX_ALLOWED_FILE_LENGTH
    data_int16 = np.frombuffer(infile.readframes(length), dtype = 'int16')
    # convert int16 data to float from -1 to 1
    data = data_int16.astype('float32') / (-np.iinfo(np.int16).min)     
    write_file("talking.dat", length, data)

def main():
    make_tone_file()
    make_noise_file()
    make_voice_file()

if __name__ == '__main__':
    main()
