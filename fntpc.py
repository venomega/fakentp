#!/usr/bin/env python3


import socket as s
import sys
import os
import time


def connect():
    HOST, PORT = sys.argv[1].split(":")
    socket = s.socket()
    command = b"GET_TIME"

    m = ['ene', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dec']

    socket.connect((HOST, int(PORT)))
    socket.send(command)
    response = socket.recv(3333)
    asd = response.decode().split(" ")
    count = 0
    for i in m:
        if i in asd[2]:
            count += 1
            break
        count += 1

    cmd =   f"timedatectl set-time \"{asd[3]}-{count}-{asd[1]} {asd[4]}\""
    os.popen("timedatectl set-ntp 0").read()
    os.popen("timedatectl set-local-rtc 0").read()
    os.popen(cmd).read()
    


if __name__ == "__main__":
    pid = os.getpid()
    os.fork()
    if os.getpid() == pid:
        exit(0)
    else:
        while True:
            connect()
            time.sleep(60)
