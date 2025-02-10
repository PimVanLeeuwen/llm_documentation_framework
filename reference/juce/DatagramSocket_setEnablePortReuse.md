#### setEnablePortReuse()


 bool DatagramSocket::setEnablePortReuse ( bool enabled ) 
 

Allow other applications to reuse the port.Allow any other application currently running to bind to the same port. Do not use this if your socket handles sensitive data as it could be read by any, possibly malicious, thirdparty apps.Returnstrue on success