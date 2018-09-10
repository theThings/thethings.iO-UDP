import ttio_udp

# by token

thingToken = 'QnxQgWCRMMirS4kmW_6EVW7nULJ4ssnZvPU_PQ8HMNE'
messageStr = 'ABCD1234'
# var sha1 = ''

ttio_udp.sendUDPMessageTTIOv1(thingToken,messageStr)
# ttio_udp.sendUDPMessageTTIOv1(thingToken,messageStr, sha1)
