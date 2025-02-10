#### setItemPosition()


 void StretchableLayoutManager::setItemPosition ( int itemIndex, 
 
 int newPosition ) 

Moves one of the items, shifting along any other items as necessary in order to get it to the desired position.Calling this method will also update the preferred sizes of the items it shuffles along, so that they reflect their new positions.(This is the method that a StretchableLayoutResizerBar uses to shift the items about when it's dragged).Parameters

 itemIndex the item to move 
 
 newPosition the absolute position that you'd like this item to move to. The item might not be able to always reach exactly this position, because other items may have minimum sizes that constrain how far it can go