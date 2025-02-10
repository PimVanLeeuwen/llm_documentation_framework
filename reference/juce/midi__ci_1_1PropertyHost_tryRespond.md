#### tryRespond()


 bool midi\_ci::PropertyHost::tryRespond ( ResponderOutput & output, const Message::Parsed & message ) overridevirtual 
 

If the message is processed successfully, and a response sent, then this returns true.Otherwise, returns false, allowing other ResponderDelegates to attempt to handle the message if necessary.Implements midi\_ci::ResponderDelegate.