#!/usr/bin/bash

echo "Creating bins in /usr/local/bin"
cp fntpd.py /usr/local/bin/
cp fntpc.py /usr/local/bin/
echo "Allow Execution Permissions"
chmod +x /usr/local/bin/fntpd.py /usr/local/bin/fntpc.py
echo "Copying services"
cp *service /lib/systemd/system

