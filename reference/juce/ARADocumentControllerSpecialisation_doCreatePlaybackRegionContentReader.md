#### doCreatePlaybackRegionContentReader()


 virtual ARA::PlugIn::ContentReader \* ARADocumentControllerSpecialisation::doCreatePlaybackRegionContentReader ( ARA::PlugIn::PlaybackRegion \* playbackRegion, ARA::ARAContentType type, const ARA::ARAContentTimeRange \* range ) protectedvirtual 
 

Override to implement createPlaybackRegionContentReader() for all your supported content types, returning a custom subclass instance of ContentReader providing data of the requested type.This function's result is returned from ARA::PlugIn::DocumentControllerDelegate::doCreatePlaybackRegionContentReader.