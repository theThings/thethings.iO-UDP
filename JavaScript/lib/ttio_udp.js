const dgram = require('dgram');

const TTIO_HOST = '104.199.85.211';
const TTIO_PORT = 28399; 

exports.sendUDPMessageTTIOv0 = function(productId, hash, deviceId, messageStr, sha1Str = null){

    // by deviceId
    let protocol = Buffer.from('00', 'hex');
   
    var productIdHex = decimalToPaddedHexString(productId);
    let idProductHex = Buffer.from(productIdHex, 'hex'); 

    var idProductLength = idProductHex.length.toString(16)
    if (idProductLength.length == 1) idProductLength = '0' + idProductLength;
    let idProductLengthHex = Buffer.from(idProductLength, 'hex');

    let hashHex = Buffer.from(hash.toString('hex'));

    let idDeviceHex = Buffer.from(deviceId.toString('hex'));

    var deviceIdLength = deviceId.length.toString(16);
    if (deviceIdLength.length == 1) deviceIdLength = '0' + deviceIdLength;
    var idDeviceLength = idDeviceHex.length.toString(16)
    if (idDeviceLength.length == 1) idDeviceLength = '0' + idDeviceLength;
    let idDeviceLengthHex = Buffer.from(idDeviceLength, 'hex');

    let sha1 = sha1Str != null ? Buffer.from(sha1Str, 'hex') : Buffer.from('', 'hex');

    let message = Buffer.concat([protocol, idProductLengthHex, idProductHex, hashHex, idDeviceLengthHex, idDeviceHex, Buffer.from(messageStr, 'hex'), sha1]);

    sendUDPMessage(message, TTIO_HOST, TTIO_PORT)
}

exports.sendUDPMessageTTIOv1 = function(thingToken, messageStr, sha1Str = null){

    // by token
    let protocol = Buffer.from('01', 'hex');
    let token = Buffer.from(thingToken.toString('hex'));
    let sha1 = sha1Str != null ? Buffer.from(sha1Str, 'hex') : Buffer.from('', 'hex');
    let message = Buffer.concat([protocol, token, Buffer.from(messageStr, 'hex'), sha1]);

    sendUDPMessage(message, TTIO_HOST, TTIO_PORT)
}

function sendUDPMessage(message, TTIO_HOST, TTIO_PORT){
    var client = dgram.createSocket('udp4');

    client.on('error', function(e) {
        throw e;
    });

    client.on('message', function (msg, rinfo) {
        console.log(msg);
        client.close();
    });

    client.send(message, 0, message.length, TTIO_PORT, TTIO_HOST, function(err, bytes) {
        console.log(message);
        if (err) throw err;
        console.log('UDP message sent to ' + TTIO_HOST +':'+ TTIO_PORT);
    });
}

function decimalToPaddedHexString(num)
{
    var hex = num.toString(16)
    if (hex.length % 2 != 0) var paddedHex = '0' + hex;
    else paddedHex = hex;
    return paddedHex
}