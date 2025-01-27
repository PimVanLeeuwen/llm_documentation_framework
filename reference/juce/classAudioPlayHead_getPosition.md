#### getPosition()


 virtual Optional< PositionInfo > AudioPlayHead::getPosition ( ) const pure virtual 
 

Fetches details about the transport's position at the start of the current processing block.If this method returns nullopt then the current play head position is not available.A nonnull return value just indicates that the host was able to provide some\* relevant timing information. Individual PositionInfo getters may still return nullopt.You can ONLY call this from your processBlock() method! Calling it at other times will produce undefined behaviour, as the host may not have any context in which a time would make sense, and some hosts will almost certainly have multithreading issues if it's not called on the audio thread.