import socket
from requests import get
import os

# Get current directory of running file by using the dir of the current running file

cwd = os.path.dirname(os.path.abspath(__file__))

# get list  but with /n with .readlines

Klist = open(cwd + '\Domains.txt').readlines()

# get new clean list with append.(i)replace

D = []

for line in Klist:
    D.append(line.replace("\n", ""))

# and a new list to for the ping

L = []

for line in D:
    L.append(socket.gethostbyname(line))

# To get location use ipapi

G = []
adress = "https://ipapi.co/{}/country/"
for line in L:
    A = (adress.format(line))
    G.append(get(A).text)

# CombineLists  and add spaces with a new list

J = []
for i in L:
    J.append(" ")

P = [D + J + L + J + G for D, J, L, J, G in zip(D, J, L, J, G)]

# Write List on txt and save it / at the start so the path changes and the filename is created .
# If not it will be created one folder back

with open(cwd + '\Ready.txt', 'w') as ready:
    for i in P:
        ready.write("%s\n" % i)
ready.close()
