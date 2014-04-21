import socket
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect(("zak.radionova.no", 6667))

print irc.recv(4096)
irc.send ('NICK botwad\r\n')
irc.send ('USER botwad botwad botwad :botwad \r\n')
#irc.send ('JOIN #radionova\r\n')

