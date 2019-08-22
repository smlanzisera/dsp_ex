
#include <stdio.h>
#include <stdint.h>

#include "hearing_aid.h"

int main(int argc, char * argv[]) {

  if (argc != 2) {
    printf("usage:\t%s <input file>\n", argv[0]);
    printf("\tinput file has the following format:\n");
    printf("\tstruct audio { uint32_t length; float data[length] };\n");
    return -1;
  }

  float * in_data = NULL;
  float * out_data = NULL;
  uint32_t length = 0;
  if (0 != setup_input_output(argv[1], &in_data, &out_data, &length)) {
    printf("initilization error\n");
    return -2;
  }

  hearingaid_settings_t settings = {
    .gain = 10, // dB
    .output_limit = 0, // dB
    .limiting_attack_release = 0.01,
    .block_size = 16,
  };

  hearingaid_run(&settings, in_data, length, out_data);
  
  /* Insert a new function here that estimates the feedback path */

  destroy_buffers(in_data, out_data);
  return 0;
}
