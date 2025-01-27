#### getAudioSource()


template<typename AudioSource\_t = ARAAudioSource> 

 AudioSource\_t \* ARAAudioModification::getAudioSource ( ) const noexcept 
 

Returns the result of ARA::PlugIn::AudioModification::getAudioSource() with the pointer cast to ARAAudioSource\*.If you have overridden ARADocumentControllerSpecialisation::doCreateAudioSource(), then you can use the template parameter to cast the pointers to your subclass of ARAAudioSource.