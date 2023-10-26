"""
Networking/Socket Programming:
An Internet Socket/ network socket is an endpoint
of a bidirectional inter-process communication flow across an internet
Protocol Based computer network
"""
import socket
import xml.etree.ElementTree as ET
import urllib.request, urllib.error
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("data.pr4e.org", 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_socket.send(cmd)
"""
1. The socket is kind of file handle and is not yet connected
    we use connect in line 9 to connect
2. In line 8 AF_INET tells we are making socket that goes across the internet
3. In line 8 SOCK_STREAM means it's series of characters that come one after another
    rather than series of blocks/text.
4. Line 9 associates and makes connection to internet.
5. The 'encode()' function is encoding the data into UTF-8
6. 512 bytes of data to be received at once we can change it to any high or low number depending on our requirement
"""
while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
my_socket.close()

"""
URLLIB - Python library does all the socket stuff !
"""
# here we are reading text while, we can also read pages but for html we have separate packages to do!
file_hand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in file_hand:
    print(line.decode().strip())
"""
We have another python library names BeautifulSoup which is used
for parsing HTML Documents and extracting data from them.
"""
"""
Wire protocol: sending data back and forth which is independent of
any programming language and these structure of data are XML/JSON.
"""
# XML in PYTHON
data = '''<person>
<name>Pragati</name>
<phone type="intl">
+91 8379905974
</phone>
<email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
