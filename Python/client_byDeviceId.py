import ttio_udp 

# by deviceId

productId = 1234
hashStr = 'hashexample'
deviceId = 'TTIO_TRIAL'
messageStr = '1a2b3c'
# sha1 = ''

ttio_udp.sendUDPMessageTTIOv0(productId,hashStr,deviceId,messageStr)
# ttio_udp.sendUDPMessageTTIOv0(productId,hash,deviceId,messageStr,sha1)
