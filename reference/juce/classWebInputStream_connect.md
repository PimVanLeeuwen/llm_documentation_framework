#### connect()


 bool WebInputStream::connect ( Listener \* listener ) 
 

Wait until the first byte is ready for reading.This method will attempt to connect to the URL given in the constructor and block until the status code and all response headers have been received or an error has occurred.Note that most methods will call connect() internally if they are called without an established connection. Therefore, it is not necessary to explicitly call connect unless you would like to use a custom listener.After a successful call to connect(), getResponseHeaders(), getTotalLength() and getStatusCode() will all be nonblocking.Parameters

 listener a listener to receive progress callbacks on the status of a POST data upload. 
 



See alsogetResponseHeaders, getTotalLength, getStatusCode