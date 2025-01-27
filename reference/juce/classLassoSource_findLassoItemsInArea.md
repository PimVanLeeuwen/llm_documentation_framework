#### findLassoItemsInArea()


template<class SelectableItemType > 

 virtual void LassoSource< SelectableItemType >::findLassoItemsInArea ( Array< SelectableItemType > & itemsFound, const Rectangle< int > & area ) pure virtual 
 

Returns the set of items that lie within a given lassoable region.Your implementation of this method must find all the relevant items that lie within the given rectangle. and add them to the itemsFound array.The coordinates are relative to the topleft of the lasso component's parent component. (i.e. they are the same as the size and position of the lasso component itself).