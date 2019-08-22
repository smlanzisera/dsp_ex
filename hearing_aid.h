#pragma once 

#include <stdint.h>

// length is in float32 words
#define MAX_ALLOWED_FILE_LENGTH (160000)

typedef struct {
  float gain; // in dB (https://en.wikipedia.org/wiki/Decibel)
  float output_limit; // in dB full scale (values <= 0 only)
  float limiting_attack_release; // exponential averaging coefficient for limiter
  uint32_t block_size; // energy is calculated over the block size for output limiting
} hearingaid_settings_t;

// Run a stream of PCM audio sampeles in float32 format through a simulated 
// hearing aid including a forward gain path with output limiting 
// and a undesired feedback path. 
void hearingaid_run(  hearingaid_settings_t * settings, 
                      float * audio_samples_in, 
                      uint16_t audio_length, 
                      float * audio_samples_out);

// Read from a file the length of the binary data in the file and  
// the words in the file. Allocate a buffers for the input data and 
// for the output of the hearing aid processing. 
int setup_input_output( char * filename, 
                        float ** in_data, 
                        float ** out_data, 
                        uint32_t * length_read); 

// Free allocated memory.
void destroy_buffers(float * in_data, float * out_data);
