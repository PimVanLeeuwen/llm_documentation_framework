#### beginLasso()


template<class SelectableItemType > 

 void LassoComponent< SelectableItemType >::beginLasso ( const MouseEvent & e, 
 
 LassoSource< SelectableItemType > \* lassoSource ) 

Call this in your mouseDown event, to initialise a drag.Pass in a suitable LassoSource object which the lasso will use to find the items and change the selection.After using this method to initialise the lasso, repeatedly call dragLasso() in your component's mouseDrag callback.See alsodragLasso, endLasso, LassoSource References LassoSource< SelectableItemType >::getLassoSelection(), MouseEvent::getMouseDownPosition(), Component::getParentComponent(), jassert, and Component::setSize().