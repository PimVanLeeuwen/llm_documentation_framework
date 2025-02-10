#### terminate()


 bool midi\_ci::InitiatorPropertyExchangeCache::terminate ( Token64 ) 
 

Terminates/cancels an ongoing transaction.Returns true if the termination had an effect (i.e. the transaction was still ongoing), or false otherwise (the transaction already ended or never started).