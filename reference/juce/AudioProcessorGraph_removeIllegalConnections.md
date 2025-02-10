#### removeIllegalConnections()


 bool AudioProcessorGraph::removeIllegalConnections ( UpdateKind = UpdateKind::sync ) 
 

Performs a sanity checks of all the connections.This might be useful if some of the processors are doing things like changing their channel counts, which could render some connections obsolete.