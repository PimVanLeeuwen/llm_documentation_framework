#### getPlaybackRegions()


template<typename PlaybackRegion\_t = ARAPlaybackRegion> 

 const std::vector< PlaybackRegion\_t \* > & ARARegionSequence::getPlaybackRegions ( ) const noexcept 
 

Returns the result of ARA::PlugIn::RegionSequence::getPlaybackRegions() with the pointers within cast to ARAPlaybackRegion\*.If you have overridden ARADocumentControllerSpecialisation::doCreatePlaybackRegion(), then you can use the template parameter to cast the pointers to your subclass of ARAPlaybackRegion.