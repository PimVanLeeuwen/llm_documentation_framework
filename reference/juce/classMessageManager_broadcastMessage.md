#### broadcastMessage()


 static void MessageManager::broadcastMessage ( const String & messageText ) static 
 

Sends a message to all other JUCE applications that are running.Parameters

 messageText the string that will be passed to the actionListenerCallback() method of the broadcast listeners in the other app. 
 



See alsoregisterBroadcastListener, ActionListener