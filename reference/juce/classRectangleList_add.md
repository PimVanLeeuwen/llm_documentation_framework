#### add() [3/3]


template<typename ValueType > 

 void RectangleList< ValueType >::add ( const RectangleList< ValueType > & other ) 
 

Merges another rectangle list into this one.Any overlaps between the two lists will be clipped, so that the result is the union of both lists.References RectangleList< ValueType >::add().