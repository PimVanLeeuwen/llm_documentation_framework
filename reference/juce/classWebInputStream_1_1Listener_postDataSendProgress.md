#### postDataSendProgress()


 virtual bool WebInputStream::Listener::postDataSendProgress ( WebInputStream & request, int bytesSent, int totalBytes ) virtual 
 

This method will be called periodically with updates on POST data upload progress.Parameters

 request the original request 
 
 bytesSent the number of bytes sent so far 
 totalBytes the total number of bytes to send 



Returnstrue to continue or false to cancel the upload