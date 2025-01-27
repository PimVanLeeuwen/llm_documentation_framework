#### sendChangeMessage()


 void ChangeBroadcaster::sendChangeMessage ( ) 
 

Causes an asynchronous change message to be sent to all the registered listeners.The message will be delivered asynchronously by the main message thread, so this method will return immediately. To call the listeners synchronously use sendSynchronousChangeMessage().Referenced by SelectedItemSet< SelectableItemType >::changed(), and SelectedItemSet< SelectableItemType >::changed().