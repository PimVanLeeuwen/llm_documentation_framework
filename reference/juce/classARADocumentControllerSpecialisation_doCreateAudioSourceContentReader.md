#### doCreateAudioSourceContentReader()


 virtual ARA::PlugIn::ContentReader \* ARADocumentControllerSpecialisation::doCreateAudioSourceContentReader ( ARA::PlugIn::AudioSource \* audioSource, ARA::ARAContentType type, const ARA::ARAContentTimeRange \* range ) protectedvirtual 
 

Override to implement createAudioSourceContentReader() for all your supported content types, returning a custom subclass instance of ContentReader providing data of the requested type.This function's result is returned from ARA::PlugIn::DocumentControllerDelegate::doCreateAudioSourceContentReader.