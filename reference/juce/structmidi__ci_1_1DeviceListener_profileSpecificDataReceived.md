#### profileSpecificDataReceived()


 virtual void midi\_ci::DeviceListener::profileSpecificDataReceived ( MUID x, ChannelInGroup destination, Profile profile, Span< const std::byte > data ) virtual 
 

Called to indicate that data for a profile were received.Note that this function may be called either when a remote device attempts to send data to one of the local Device's profiles, or when a profile on a remote device produces some data.Each profile will specify its own mechanism for distinguishing between the two cases if necessary.