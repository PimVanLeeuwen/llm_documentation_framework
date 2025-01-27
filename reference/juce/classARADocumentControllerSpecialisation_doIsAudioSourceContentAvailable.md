#### doIsAudioSourceContentAvailable()


 virtual bool ARADocumentControllerSpecialisation::doIsAudioSourceContentAvailable ( const ARA::PlugIn::AudioSource \* audioSource, ARA::ARAContentType type ) protectedvirtual 
 

Override to implement isAudioSourceContentAvailable() for all your supported content types the default implementation always returns false, preventing any calls to doGetAudioSourceContentGrade() and doCreateAudioSourceContentReader().This function's result is returned from ARA::PlugIn::DocumentControllerDelegate::doIsAudioSourceContentAvailable.