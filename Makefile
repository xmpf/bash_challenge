CC=`which gcc`
RM=`which rm`
MKDIR=`which mkdir`

CFLAGS=-Wall -Wextra
CFLAGS+=-DMAX_TRIES=3
CFLAGS+=-DCLOSE_STDOUT=0

VPATH=src/

all: jailbash

jailbash: shell.c
	${MKDIR} -p bin
	$(CC) $(CFLAGS) -o bin/$@ $< 

.PHONY: clean
clean:
	$(RM) -rf bin/jailbash
