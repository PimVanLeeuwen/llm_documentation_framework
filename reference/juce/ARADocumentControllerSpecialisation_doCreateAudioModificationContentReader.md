#### doCreateAudioModificationContentReader()


 virtual ARA::PlugIn::ContentReader \* ARADocumentControllerSpecialisation::doCreateAudioModificationContentReader ( ARA::PlugIn::AudioModification \* audioModification, ARA::ARAContentType type, const ARA::ARAContentTimeRange \* range ) protectedvirtual 
 

Override to implement createAudioModificationContentReader() for all your supported content types, returning a custom subclass instance of ContentReader providing data of the requested `type`.For readonly data directly inherited from the underlying audio source you can just delegate the call to the audio source, but usereditable modification data must be specifically handled here.This function's result is returned from ARA::PlugIn::DocumentControllerDelegate::doCreateAudioModificationContentReader.