#### sendUpstreamMessage()


 void PushNotifications::sendUpstreamMessage ( const String & serverSenderId, 
 
 const String & collapseKey, 
 const String & messageId, 
 const String & messageType, 
 int timeToLive, 
 const StringPairArray & additionalData ) 

Android only: sends an upstream message to your app server.The server must implement XMPP Connection Server protocol (refer to Firebase documentation).Parameters

 serverSenderId Represents the sender. Consult your Firebase project settings to retrieve the sender id. 
 
 collapseKey Remote messages with the same collapse key that were not yet delivered will be collapsed into one, with the newest message replacing all the previous ones. Note that there may be a limit of maximum collapse keys used at the same time and beyond the limit (refer to Firebase documentation) it is not guaranteed which keys will be in use by the server. 
 messageId A unique message ID. Used in error callbacks and debugging. 
 messageType Message type. 
 timeToLive TTL in seconds. If 0, the message sending will be attempted immediately and it will be dropped if the device is not connected. Otherwise, the message will be queued for the period specified. 
 additionalData Collection of keyvalue pairs to be used as an additional data for the message.