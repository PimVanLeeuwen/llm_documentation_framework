#### getLastIndex()


 int AudioCDReader::getLastIndex ( ) const 
 

Returns the index number found during the last read() call.Index scanning is turned off by default turn it on with enableIndexScanning().Then when the read() method is called, if it comes across an index within that block, the index number is stored and returned by this method.Some devices might not support indexes, of course.(If you don't know what CD indexes are, it's unlikely you'll ever need them).See alsoenableIndexScanning