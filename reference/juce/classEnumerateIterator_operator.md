#### operator()


template<typename Iter , typename Index = ptrdiff\_t> 
template<typename OtherIter , typename OtherInd , std::enable\_if\_t< detail::canSub< Iter, OtherIter >, int > = 0> 

 auto EnumerateIterator< Iter, Index >::operator ( const EnumerateIterator< OtherIter, OtherInd > & other ) const nodiscardconstexpr 
 

Subtracts another enumerate iterator from this one, producing the same result as subtracting the two wrapped iterators.For randomaccess iterators, this will normally return the distance between the two iterators. Only participates in overload resolution if the wrapped iterators can be subtracted.