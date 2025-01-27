#### operator>()


template<typename Iter , typename Index = ptrdiff\_t> 
template<typename OtherIter , typename OtherInd , std::enable\_if\_t< detail::canGreaterThan< Iter, OtherIter >, int > = 0> 

 bool EnumerateIterator< Iter, Index >::operator> ( const EnumerateIterator< OtherIter, OtherInd > & other ) const nodiscardconstexpr 
 

Returns the result of comparing the two wrapped iterators.Only participates in overload resolution if the wrapped iterators are comparable.