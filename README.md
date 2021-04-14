# fakentp
own dummy implementation of something like ntp client-server connection



##### Features
 - Bad writed



There are some case scenarios (like my workplace) where the internet connection is throught a proxy; this proxy only allow output 443 port and not 123, so with this client-server software you could export your date/time from one remote location to localhost


##### Creating the Server

```
chmod +x ./fntpd.py
./fntpd.py 123
```

Here ```123``` means a port to listen on ```0.0.0.0```


##### Using the Client

```
chmod +x ./fntpc.py
./fntpc.py 127.0.0.1:123
```


Here ```127.0.0.1:123``` its the ip & port of the Server from above
(In this example we are running server & client on same Machine)

For use on startup just edit the ```.service``` files and install them with ```./install.sh```