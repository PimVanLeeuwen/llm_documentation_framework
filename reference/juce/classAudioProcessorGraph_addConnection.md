#### addConnection()


 bool AudioProcessorGraph::addConnection ( const Connection & , 
 
 UpdateKind = UpdateKind::sync ) 

Attempts to connect two specified channels of two nodes.If this isn't allowed (e.g. because you're trying to connect a midi channel to an audio one or other such nonsense), then it'll return false.