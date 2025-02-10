#### operator==()


template<typename Iter , typename Index = ptrdiff\_t> 
template<typename OtherIter , typename OtherInd > 

 bool EnumerateIterator< Iter, Index >::operator== ( const EnumerateIterator< OtherIter, OtherInd > & other ) const nodiscardconstexpr 
 

Two EnumerateIterators are considered equal if the wrapped iterators are equal.Referenced by EnumerateIterator< Iter, Index >::operator!=().