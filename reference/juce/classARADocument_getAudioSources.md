#### getAudioSources()


template<typename AudioSource\_t = ARAAudioSource> 

 const std::vector< AudioSource\_t \* > & ARADocument::getAudioSources ( ) const noexcept 
 

Returns the result of ARA::PlugIn::Document::getAudioSources() with the pointers within cast to ARAAudioSource\*.If you have overridden ARADocumentControllerSpecialisation::doCreateAudioSource(), then you can use the template parameter to cast the pointers to your subclass of ARAAudioSource.