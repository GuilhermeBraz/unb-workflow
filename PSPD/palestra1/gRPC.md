# gRPC
## What is gRPC?
Protcol build on top of HTTP/2 (as a transport), define how to write request and interpret messages and responses, the  messages that you serialize are encoded by protocol buffers(Protobuf).

HTTP/2 takes a single physical stream an multiplex logical streams on top of that, every rpc request is an HTTP request and the same for reponse.

Create and compile clients libraries, machine readable (API contracts), which is different from HTTP/REST

### Examples 

![[Screenshot from 2022-02-11 00-51-43.png]]

Telephony API

![[Screenshot from 2022-02-11 00-23-49.png]]