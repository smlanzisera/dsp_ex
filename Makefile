
sim: build/hearing_aid.o 
	cc -Werror -Og main.c build/hearing_aid.o -o build/sim

ha: build/hearing_aid.o

build/hearing_aid.o:
	cc -Werror -O3 -c hearing_aid.c -o build/hearing_aid.o

clean:
	rm  build/sim
