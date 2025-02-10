#### getStatusCode()


 int WebInputStream::getStatusCode ( ) 
 

Returns the status code returned by the HTTP server.If getStatusCode() is called without an established connection, then getStatusCode() will call connect internally and block until connect returns either due to a successful connection or a connection error.See alsoconnect