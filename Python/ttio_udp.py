import socket
import time

TTIO_HOST = '104.199.85.211'
TTIO_PORT = 28399

def sendUDPMessageTTIOv0(productId, hashStr, deviceId, messageStr, sha1Str = None):
    # by deviceId
    protocol = '0x00'

    idProductHex = decimalToPaddedHexString(productId)
    idProductLengthHex = decimalToPaddedHexString((len(idProductHex)-2)/2)
    
    hashHex = stringToHex(hashStr)
    
    idDeviceHex = stringToHex(deviceId)
    idDeviceLengthHex = decimalToPaddedHexString((len(idDeviceHex)-2)/2)

    mg = messageStr

    sha1 = stringToHex(sha1Str) if sha1Str is not None else None

    hexList = [protocol, idProductLengthHex, idProductHex, hashHex, idDeviceLengthHex, idDeviceHex, mg, sha1]
    print(hexList)
    message = concatenateListOfHex(hexList)

    sendUDPMessage(message, TTIO_HOST, TTIO_PORT)

def sendUDPMessageTTIOv1(thingToken, messageStr, sha1Str = None):
    # by token
    protocol = '0x01'
    token = stringToHex(thingToken)
    mg = messageStr
    sha1 = stringToHex(sha1Str) if sha1Str is not None else None

    hexList = [protocol, token, mg, sha1]
    print(hexList)
    message = concatenateListOfHex(hexList)

    sendUDPMessage(message, TTIO_HOST, TTIO_PORT)

def sendUDPMessage(message, TTIO_HOST, TTIO_PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(bytearray.fromhex(message),(TTIO_HOST,TTIO_PORT))
    print(message)
    print("UDP message sent to '{}':'{}'".format(TTIO_HOST,TTIO_PORT))
    time.sleep(1)
    data, address = s.recvfrom(4096)
    print("received %s from address %s"% (data,address))

def decimalToPaddedHexString(num):
    paddedHex = "{0:#0{1}x}".format(num,4)
    return paddedHex

def concatenateListOfHex(hexList):
    return ''.join([format(int(c, 16), '02X') for c in hexList if c is not None])
    
def stringToHex(str):
    str_hex = list()
    for character in str:
        str_hex.append(hex(ord(character)))
    return '0x' + concatenateListOfHex(str_hex)
    
