#### withPOSTData() [2/2]


 URL URL::withPOSTData ( const MemoryBlock & postData ) const nodiscard 
 

Returns a copy of this URL, with a block of data to send as the POST data.If the URL already contains some POST data, this will replace it, rather than being appended to it.If no HTTP command is set when calling createInputStream() to read from this URL and some data has been set, it will do a POST request.