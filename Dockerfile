FROM alpine:3.10
RUN apk add --no-cache gcc musl-dev make
WORKDIR /home/dsp_exercise
