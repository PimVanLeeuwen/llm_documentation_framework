#### doIsPlaybackRegionContentAvailable()


 virtual bool ARADocumentControllerSpecialisation::doIsPlaybackRegionContentAvailable ( const ARA::PlugIn::PlaybackRegion \* playbackRegion, ARA::ARAContentType type ) protectedvirtual 
 

Override to implement isPlaybackRegionContentAvailable() for all your supported content types the default implementation always returns false.Typically, this call can directly delegate to the underlying audio modification, since most plugins will apply their modification data to the playback region with a transformation that does not affect content availability.This function's result is returned from ARA::PlugIn::DocumentControllerDelegate::doIsPlaybackRegionContentAvailable.