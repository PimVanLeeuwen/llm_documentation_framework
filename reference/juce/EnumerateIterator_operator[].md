#### operator[]()


template<typename Iter , typename Index = ptrdiff\_t> 
template<typename I , std::enable\_if\_t< detail::canAdd< EnumerateIterator, I >, int > = 0> 

 auto EnumerateIterator< Iter, Index >::operator[] ( I diff ) const nodiscardconstexpr 
 

Indexes into this iterator, equivalent to adding an integral value to this iterator and then dereferencing the result.Only participates in overload resolution if the wrapped iterator allows addition of integral values.