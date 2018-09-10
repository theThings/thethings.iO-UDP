# thethings.iO-UDP
Repository with all you need to send messages to TTIO using UDP protocol

## What is UDP?

User Datagram Protocol (UDP). With UDP, computer applications can send messages, in this case referred to as datagrams, to other hosts on an Internet Protocol (IP) network.

## Status code

When sending messages, you will receive a status code back indicating if the message was received correctly. In case it wasn't, the error code will indicate what is wrong.

In case you don't know how to fix the issue, we kindly ask you to contact us indicating the problem.

| Status code | Description | Observations |
| ------------- | ------------- |------|
|0x20 |	OK. Cloud function was called | It means that the message is correctly formatted and the function udp_parser was called. However, it doesn't assures that the function was executed correctly |
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
