#### addNode()


 Node::Ptr AudioProcessorGraph::addNode ( std::unique\_ptr< AudioProcessor > newProcessor, 
 
 std::optional< NodeID > nodeId = std::nullopt, 
 UpdateKind = UpdateKind::sync ) 

Adds a node to the graph.This creates a new node in the graph, for the specified processor. Once you have added a processor to the graph, the graph owns it and will delete it later when it is no longer needed.The optional nodeId parameter lets you specify a unique ID to use for the node. If the value is already in use, this method will fail and return an empty node.If this succeeds, it returns a pointer to the newlycreated node.