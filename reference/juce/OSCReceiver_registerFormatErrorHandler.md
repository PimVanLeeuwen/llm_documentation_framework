#### registerFormatErrorHandler()


 void OSCReceiver::registerFormatErrorHandler ( FormatErrorHandler handler ) 
 

Installs a custom error handler which is called in case the receiver encounters a stream it cannot parse as an OSC bundle or OSC message.By default (i.e. if you never use this method), in case of a parsing error nothing happens and the invalid packet is simply discarded.