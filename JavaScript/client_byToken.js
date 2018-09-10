const ttio_udp = require('./lib/ttio_udp');

// by token

var thingToken = 'thingtokenexample';
var messageStr = 'ABCD1234';
//var sha1 = '';

ttio_udp.sendUDPMessageTTIOv1(thingToken,messageStr)
//ttio_udp.sendUDPMessageTTIOv1(thingToken,messageStr, sha1)
