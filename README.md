## Estimating the Feedback Path in a Simple Hearing Aid Simulator

In a system with a microphone close to an amplified speaker, [acoustic 
feedback](https://en.wikipedia.org/wiki/Audio_feedback) can occur if the gain 
of the forward path exceeds the attenuation of the feedback path. Feedback 
cancellation algorithms estimate the feedback or leakage path characteristics 
and attempt to subtract an estimated feedback signal from the measured signal
to increase system stability.

This project contains a simple hearing aid simulator that contains forward 
gain, an output limiter, and a feedback path. 

### Exercise
Implement a function that estimates the feedback path impulse response or 
transfer function. Generate a meaningful, easy to review representation of the 
transfer function or impulse response. Provide a very brief summary of 
important details or observations you think another engineer would find
interesting. Insert this new function into the main function where shown. Add 
any necessary output for you to complete your task.

Do not create a feedback canceler or provide excessive documentation.

If after 30m or so, this exercise looks like it's going to take more than a
couple of hours, maybe we have made a mistake. Help us (and help yourself) make
the exercise better by stopping and letting us know how you were confused. 

To complete the exercise:
1. Create a feature branch. 
2. Add your changes. 
3. Commit your code and push. 
4. Submit a [pull request](https://help.github.com/en/articles/about-pull-requests) 
that contains your new code, a brief description of what you did, and any 
documentation or notes you think are relevant. 

### What we hope to learn

We hope to see you take a relevant problem, learn a little about it, implement
a little code to solve a problem in a language used in this role, and 
communicate findings clearly and concisely. As an added bonus, you will use git.

### Using the simulator
Build docker image 
`docker build -t whisper/dsp-exercise .`

To build:
`docker run -v $(pwd):/home/dsp_exercise whisper/dsp-exercise make`

To run:
`docker run -v $(pwd):/home/dsp_exercise whisper/dsp-exercise ./build/sim <input data file name>`

Example:
`docker run -v $(pwd):/home/dsp_exercise whisper/dsp-exercise ./build/sim test_files/tone.dat`

Example input files are in `test_files/` and have a `.dat` extension. There is
also a python script that created these files if you are interested in creating
your own files. 

The file format is `struct audio { uint32_t length; float data[length] }`

In the `main` function, there's a spot labeled for your function.

You do not have the source to the `hearing_aid.c`.
