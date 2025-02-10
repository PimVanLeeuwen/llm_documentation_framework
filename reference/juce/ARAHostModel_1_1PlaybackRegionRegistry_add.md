#### add()


template<typename RendererRef , typename Interface > 

 void ARAHostModel::PlaybackRegionRegistry< RendererRef, Interface >::add ( PlaybackRegion & region ) 
 

Adds a PlaybackRegion to the corresponding PlaybackRendererInterface or EditorRendererInterface.The plugin instance must be in an unprepared state i.e. before AudioProcessor::prepareToPlay() or after AudioProcessor::releaseResources().