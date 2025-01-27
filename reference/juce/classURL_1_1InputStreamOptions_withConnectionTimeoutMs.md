#### withConnectionTimeoutMs()


 InputStreamOptions URL::InputStreamOptions::withConnectionTimeoutMs ( int connectionTimeoutMs ) const nodiscard 
 

Specifies a timeout for the request in milliseconds.If 0, this will use whatever default setting the OS chooses. If a negative number, it will be infinite.