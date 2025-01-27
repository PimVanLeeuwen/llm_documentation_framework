#### getRegionSequence()


template<typename RegionSequence\_t = ARARegionSequence> 

 RegionSequence\_t \* ARAPlaybackRegion::getRegionSequence ( ) const noexcept 
 

Returns the result of ARA::PlugIn::PlaybackRegion::getRegionSequence() with the pointer cast to ARARegionSequence\*.If you have overridden ARADocumentControllerSpecialisation::doCreateRegionSequence(), then you can use the template parameter to cast the pointers to your subclass of ARARegionSequence.