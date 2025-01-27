#### tryRespond()


 virtual bool midi\_ci::ResponderDelegate::tryRespond ( ResponderOutput & output, const Message::Parsed & message ) pure virtual 
 

If the message is processed successfully, and a response sent, then this returns true.Otherwise, returns false, allowing other ResponderDelegates to attempt to handle the message if necessary.Implemented in midi\_ci::ProfileHost, and midi\_ci::PropertyHost.