#### getAudioModifications()


template<typename AudioModification\_t = ARAAudioModification> 

 const std::vector< AudioModification\_t \* > & ARAAudioSource::getAudioModifications ( ) const noexcept 
 

Returns the result of ARA::PlugIn::AudioSource::getAudioModifications() with the pointers within cast to ARAAudioModification\*.If you have overridden ARADocumentControllerSpecialisation::doCreateAudioModification(), then you can use the template parameter to cast the pointers to your subclass of ARAAudioModification.