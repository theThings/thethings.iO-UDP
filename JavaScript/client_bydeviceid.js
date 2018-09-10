const ttio_udp = require('lib/ttio_udp');

// by deviceId

var productId = 1234;
var hash = 'hashexample'
var deviceId = 'TTIO_TRIAL'
var messageStr = 'ABCD1234'
//let sha1 = ''

ttio_udp.sendUDPMessageTTIOv0(productId,hash,deviceId,messageStr)
//ttio_udp.sendUDPMessageTTIOv0(productId,hash,deviceId,messageStr,sha1)
