#### addMessageToQueue()


 void MidiMessageCollector::addMessageToQueue ( const MidiMessage & message ) 
 

Takes an incoming realtime message and adds it to the queue.The message's timestamp is taken, and it will be ready for retrieval as part of the block returned by the next call to removeNextBlockOfMessages().This method is fully threadsafe when overlapping calls are made with removeNextBlockOfMessages().