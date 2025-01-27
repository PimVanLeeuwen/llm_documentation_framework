#### Advertiser()


 NetworkServiceDiscovery::Advertiser::Advertiser ( const String & serviceTypeUID, 
 
 const String & serviceDescription, 
 int broadcastPort, 
 int connectionPort, 
 RelativeTime minTimeBetweenBroadcasts = RelativeTime::seconds(1.5) ) 

Creates and starts an Advertiser thread, broadcasting with the given properties.Parameters

 serviceTypeUID A usersupplied string to define the type of service this represents 
 
 serviceDescription A description string that will appear in the Service::description field for clients 
 broadcastPort The port number on which to broadcast the service discovery packets 
 connectionPort The port number that will be sent to appear in the Service::port field 
 minTimeBetweenBroadcasts The interval to wait between sending broadcast messages