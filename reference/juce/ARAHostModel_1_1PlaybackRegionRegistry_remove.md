#### remove()


template<typename RendererRef , typename Interface > 

 void ARAHostModel::PlaybackRegionRegistry< RendererRef, Interface >::remove ( PlaybackRegion & region ) 
 

Removes a PlaybackRegion from the corresponding PlaybackRendererInterface or EditorRendererInterface.The plugin instance must be in an unprepared state i.e. before AudioProcessor::prepareToPlay() or after AudioProcessor::releaseResources().