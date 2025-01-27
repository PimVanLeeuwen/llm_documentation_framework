#### withReceiveBufferSize()


 SocketOptions SocketOptions::withReceiveBufferSize ( int size ) const nodiscard 
 

The provided size will be used to configure the socket's SO\_RCVBUF property.Increasing the buffer size can reduce the number of lost packets with the DatagramSocket class, if the socket is to receive packets in large bursts.If this property is not specified, the system default value will be used, but a minimum of 65536 will be ensured.References withMember().