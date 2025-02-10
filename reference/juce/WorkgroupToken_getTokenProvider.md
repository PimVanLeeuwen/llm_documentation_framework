#### getTokenProvider()


 const TokenProvider \* WorkgroupToken::getTokenProvider ( ) const nodiscard 
 

The result of this function can be compared to nullptr to check whether the token successfully joined the calling thread to a workgroup.Used in the implementation to provide platformspecific information about this token.Referenced by operator bool().