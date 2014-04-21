import socket
 
network = 'irc.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )


print irc.recv ( 4096 )
irc.send ( 'NICK stolenbot\r\n' )
irc.send ( 'USER stolenbot stolenbot stolenbot :Python IRC\r\n' )
irc.send ( 'JOIN #testwad\r\n' )
irc.send ( 'PRIVMSG #testwad :Hello World.\r\n' )


while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )


   if data.find ( '!stolenbot quit' ) != -1:
      irc.send ( "PRIVMSG #testwad :Fine, if you don't want me\r\n" )
      irc.send ( 'QUIT\r\n' )


   if data.find ( 'hi stolenbot' ) != -1:
      irc.send ( 'PRIVMSG #testwad :I already said hi...\r\n' )


   if data.find ( 'hello stolenbot' ) != -1:
      irc.send ( 'PRIVMSG #testwad :I already said hi...\r\n' )


   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #testwad\r\n' )


   if data.find ( 'cheese' ) != -1:
      irc.send ( 'PRIVMSG #testwad :WHERE!!!!!!\r\n' )


   if data.find ( 'slaps stolenbot' ) != -1:
      irc.send ( 'PRIVMSG #testwad :This is the Trout Protection\r\n' )
   print data

