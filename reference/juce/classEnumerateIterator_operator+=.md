#### operator+=()


template<typename Iter , typename Index = ptrdiff\_t> 
template<typename I , std::enable\_if\_t< detail::canAddAssign< Iter &, I >, int > = 0> 

 EnumerateIterator & EnumerateIterator< Iter, Index >::operator+= ( I diff ) constexpr 
 

Adds an integral value to both the iterator and the index.Only participates in overload resolution if the iterator can be addassigned.