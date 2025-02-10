#### getResponseHeaders()


 StringPairArray WebInputStream::getResponseHeaders ( ) 
 

Returns a StringPairArray of response headers.If getResponseHeaders() is called without an established connection, then getResponseHeaders() will call connect internally and block until connect returns either due to a successful connection or a connection error.See alsoconnect