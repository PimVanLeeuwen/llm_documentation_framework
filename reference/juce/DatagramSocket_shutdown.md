#### shutdown()


 void DatagramSocket::shutdown ( ) 
 

Closes the underlying socket object.Closes the underlying socket object and aborts any read or write operations. Note that all other methods will return an error after this call and the object cannot be reused.This method is useful if another thread is blocking in a read/write call and you would like to abort the read/write thread. Simply deleting the socket object without calling shutdown may cause a racecondition where the read/write returns just before the socket is deleted and the subsequent read/write would try to read from an invalid pointer. By calling shutdown first, the socket object remains valid but all current and subsequent calls to read/write will return immediately.