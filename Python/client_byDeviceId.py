import ttio_udp 

# by deviceId

productId = 19244
hashStr = '8RLfCQROVqpwag'
deviceId = 'TTIO_TRIAL'
messageStr = 'ABCD1234'
# sha1 = ''

ttio_udp.sendUDPMessageTTIOv0(productId,hashStr,deviceId,messageStr)
# ttio_udp.sendUDPMessageTTIOv0(productId,hash,deviceId,messageStr,sha1)
