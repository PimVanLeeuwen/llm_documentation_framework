#### sendSynchronousChangeMessage()


 void ChangeBroadcaster::sendSynchronousChangeMessage ( ) 
 

Sends a synchronous change message to all the registered listeners.This will immediately call all the listeners that are registered. For threadsafety reasons, you must only call this method on the main message thread.See alsodispatchPendingMessages Referenced by SelectedItemSet< SelectableItemType >::changed().