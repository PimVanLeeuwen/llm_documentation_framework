#### doGetPlaybackRegionContentGrade()


 virtual ARA::ARAContentGrade ARADocumentControllerSpecialisation::doGetPlaybackRegionContentGrade ( const ARA::PlugIn::PlaybackRegion \* playbackRegion, ARA::ARAContentType type ) protectedvirtual 
 

Override to implement getPlaybackRegionContentGrade() for all your supported content types.Typically, this call can directly delegate to the underlying audio modification, since most plugins will apply their modification data to the playback region with a transformation that does not affect content grade.This function's result is returned from ARA::PlugIn::DocumentControllerDelegate::doGetPlaybackRegionContentGrade.