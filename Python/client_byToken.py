import ttio_udp

# by token

thingToken = 'thingtokenexample'
messageStr = 'ABCD1234'
# var sha1 = ''

ttio_udp.sendUDPMessageTTIOv1(thingToken,messageStr)
# ttio_udp.sendUDPMessageTTIOv1(thingToken,messageStr, sha1)
