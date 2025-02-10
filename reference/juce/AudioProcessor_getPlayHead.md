#### getPlayHead()


 AudioPlayHead \* AudioProcessor::getPlayHead ( ) const noexcept 
 

Returns the current AudioPlayHead object that should be used to find out the state and position of the playhead.You can ONLY call this from your processBlock() method! Calling it at other times will produce undefined behaviour, as the host may not have any context in which a time would make sense, and some hosts will almost certainly have multithreading issues if it's not called on the audio thread.The AudioPlayHead object that is returned can be used to get the details about the time of the start of the block currently being processed. But do not store this pointer or use it outside of the current audio callback, because the host may delete or reuse it.If the host can't or won't provide any time info, this will return nullptr.