#### getIdForRequestKey()


 std::optional< RequestID > midi\_ci::Device::getIdForRequestKey ( RequestKey ) const 
 

Returns the request id corresponding to a particular request.If the request could not be found (it never started, or already finished), then this returns nullopt.