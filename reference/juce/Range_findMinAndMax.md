#### findMinAndMax()


template<typename ValueType > 
template<typename Integral , std::enable\_if\_t< std::is\_integral\_v< Integral >, int > = 0> 

 static Range Range< ValueType >::findMinAndMax ( const ValueType \* values, Integral numValues ) staticnoexcept 
 

Scans an array of values for its min and max, and returns these as a Range.References Range< ValueType >::Range().