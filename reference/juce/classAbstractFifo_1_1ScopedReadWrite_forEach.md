#### forEach()


template<ReadOrWrite mode> 
template<typename FunctionToApply > 

 void AbstractFifo::ScopedReadWrite< mode >::forEach ( FunctionToApply && func ) const 
 

Calls the passed function with each index that was deemed valid for the current read/write operation.

Member Data Documentation