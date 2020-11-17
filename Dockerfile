FROM ubuntu:16.04

RUN apt update

RUN apt install -y \
    make gcc socat

WORKDIR /home/jailbash
COPY flag.txt Makefile src /home/jailbash/

RUN make

RUN useradd -d /home/jailbash/ -m -p "jailbash" -s /home/jbash/bin/jailbash jailbash
RUN echo "jailbash:jailbash" | chpasswd

EXPOSE 4000
USER jailbash

ENTRYPOINT socat tcp-l:4000,fork,reuseaddr exec:bin/jailbash,stderr