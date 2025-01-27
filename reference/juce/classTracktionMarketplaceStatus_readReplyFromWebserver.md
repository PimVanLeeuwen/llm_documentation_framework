#### readReplyFromWebserver()


 String TracktionMarketplaceStatus::readReplyFromWebserver ( const String & email, const String & password ) overridevirtual 
 

Subclasses that talk to a particular webstore will implement this method to contact their webserver and attempt to unlock the current machine for the given username and password.The return value is the XML text from the server which contains error information and/or the encrypted keyfile.Implements OnlineUnlockStatus.