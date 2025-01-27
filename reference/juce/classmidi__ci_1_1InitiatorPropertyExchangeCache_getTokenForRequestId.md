#### getTokenForRequestId()


 std::optional< Token64 > midi\_ci::InitiatorPropertyExchangeCache::getTokenForRequestId ( RequestID ) const 
 

If there's a transaction ongoing with the given request id, returns the token uniquely identifying that transaction, otherwise returns nullopt.