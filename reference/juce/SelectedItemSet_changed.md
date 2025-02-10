#### changed() [2/2]


template<class SelectableItemType > 

 void SelectedItemSet< SelectableItemType >::changed ( const bool synchronous ) 
 

Used internally, but can be called to force a change message to be sent to the ChangeListeners.References ChangeBroadcaster::sendChangeMessage(), and ChangeBroadcaster::sendSynchronousChangeMessage().