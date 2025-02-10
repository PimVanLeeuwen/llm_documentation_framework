#### getLocalAddress()


 static IPAddress IPAddress::getLocalAddress ( bool includeIPv6 = false ) static 
 

Returns the first 'real' address for the local machine.Unlike local(), this will attempt to find the machine's actual assigned address rather than "127.0.0.1". If there are multiple network cards, this may return any of their addresses. If it doesn't find any, then it'll return local() as a fallback.