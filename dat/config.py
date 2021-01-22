import socket

suck = socket.gethostname()
if suck == "Fulcrum-PC":
    root = "./"
elif suck == "WIN-KJ6QV3R1373":
    root = "/inetpub/wwwroot/"
