#### rebuild()


 void AudioProcessorGraph::rebuild ( ) 
 

Rebuilds the graph if necessary.This function will only ever rebuild the graph on the main thread. If this function is called from another thread, the rebuild request will be dispatched asynchronously to the main thread.