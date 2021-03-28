import socket

suck = socket.gethostname()
if suck in ["fulcrum", "Fulcrum-PC"]:
    root = "./"
elif suck == "WIN-KJ6QV3R1373":
    root = "/inetpub/wwwroot/"

# "start " for Windows
# "rhythmbox-client --play-uri="
player = "totem "
