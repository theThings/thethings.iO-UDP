# thethings.iO-UDP
Repository with all you need to send messages to thethings.io using UDP protocol. You can use JavaScript or Python to test the examples

## What is UDP?

User Datagram Protocol (UDP). With UDP, computer applications can send messages, in this case referred to as datagrams, to other hosts on an Internet Protocol (IP) network.

## Connection parameters

##### The format is a HEX String.

UDP thethings.iO gateway IP: 104.199.85.211

The port is: 28399

This is the structure of the message:

##### TTIO_HEADER | PAYLOAD | HMAC-SHA1(PSK, PAYLOAD) 

## thethings.iO header

To be able to communicate with our UDP service, you first have to add a header to your UDP data. At this moment we provide two possible headers to best adapt to your use case.

### Using your own deviceId.

You don't have to activate the things. They will be activated automatically once you send first message

| Byte | Value | Description |
| ------------- | ------------- |------|
Byte 0 | 0x00 | Header type: deviceId
Byte 1 | Number 1 | Length of the idProduct value
Bytes 2 to 2+(idProduct length) | Number | idProduct Value.
Bytes 2+(idProduct length) to 16+(idProduct length) | String | idProduct Hash string
Byte 16+(idProduct length) | Number | deviceId Length | 
Bytes 17+(idProduct length) to 17+(idProduct length)+(deviceId Length) | String | DeviceId String

### Using our thingToken

Things must be activated before you send first message.

| Byte | Value | Description |
| ------------- | ------------- |------|
Byte 0 | 0x01 | Header type: thingToken
Bytes 1 to 43 | String| thingToken

## Payload

Once you have the header you have to concatenate your own payload. This payload will be sent as an hex string to a cloud code function which will parse the payload sent by your devices. This cloud code function is created automatically when you create a new UDP product.

### HMAC-SHA1

This part of the message is optional. By default isn't enabled, so we have to configure manually to be ready to work. Contact us in case you want to use this feature

You can concatenate an HMAC-SHA1 hash at the end of the message. To generate the hash you have to use your payload and share with us a generated PSK (Pre-Shared Key): HMAC-SHA1(PLAIN_MESSGAGE, PSK)


## Status code

When sending messages, you will receive a status code back indicating if the message was received correctly. In case it wasn't, the error code will indicate what is wrong.

In case you don't know how to fix the issue, we kindly ask you to contact us indicating the problem.

| Status code | Description | Observations |
| ------------- | ------------- |------|
|0x20 |	OK. Cloud function was called | It means that the message is correctly formatted and the function udp_parser was called. However, it doesn't ensure that the function was executed correctly |
|0x00 |	Internal error | Please contact us |
|0x01 |	Invalid protocol | You are using a protocol different from 0x00 or 0x01 |
|0x02 |	Invalid product Id | |
|0x03 |	Invalid product hash | |
|0x04 |	Thing not found | |
|0x05 |	Message or Key length incorrect | |
|0x06 |	Invalid HMAC-SHA1 hash | |
|0x07 |	Product organizationId is wrong | |
|0x08 |	Organization has no subscription plan| |
|0x09 |	Subscription Plan is expired | |
|0x10 |	Insufficient Activation Codes | You have reached the number of things of your plan. Please get more activation codes |
|0x11 |	Error when activating a new a thing| |
|0x12 |	Error when setting thing's name | |
|0x13 |	Thing token not found | |


## More information

You can find more information about the UPD protocol at our Developers Portal: https://developers.thethings.io/v2.0/docs/udp
