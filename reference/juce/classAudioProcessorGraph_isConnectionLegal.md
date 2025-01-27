#### isConnectionLegal()


 bool AudioProcessorGraph::isConnectionLegal ( const Connection & ) const 
 

Returns true if the given connection's channel numbers map on to valid channels at each end.Even if a connection is valid when created, its status could change if a node changes its channel config.