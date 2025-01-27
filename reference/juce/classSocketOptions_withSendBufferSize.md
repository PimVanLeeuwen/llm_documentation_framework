#### withSendBufferSize()


 SocketOptions SocketOptions::withSendBufferSize ( int size ) const nodiscard 
 

The provided size will be used to configure the socket's SO\_SNDBUF property.If this property is not specified, the system default value will be used, but a minimum of 65536 will be ensured.References withMember().