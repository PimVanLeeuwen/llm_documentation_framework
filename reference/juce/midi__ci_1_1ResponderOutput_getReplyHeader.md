#### getReplyHeader()


 Message::Header midi\_ci::ResponderOutput::getReplyHeader ( std::byte replySubID ) const 
 

Returns a default header that can be used for outgoing replies.This always sets the destination MUID equal to the source MUID of the incoming header, so it's not suitable for broadcast messages.