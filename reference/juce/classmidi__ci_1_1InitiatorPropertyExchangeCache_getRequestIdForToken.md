#### getRequestIdForToken()


 std::optional< RequestID > midi\_ci::InitiatorPropertyExchangeCache::getRequestIdForToken ( Token64 ) const 
 

If the token refers to an ongoing transaction, returns the request id of that transaction.Otherwise, returns an invalid request id.