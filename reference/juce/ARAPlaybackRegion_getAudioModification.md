#### getAudioModification()


template<typename AudioModification\_t = ARAAudioModification> 

 AudioModification\_t \* ARAPlaybackRegion::getAudioModification ( ) const noexcept 
 

Returns the result of ARA::PlugIn::PlaybackRegion::getAudioModification() with the pointer cast to ARAAudioModification\*.If you have overridden ARADocumentControllerSpecialisation::doCreateAudioModification(), then you can use the template parameter to cast the pointers to your subclass of ARAAudioModification.