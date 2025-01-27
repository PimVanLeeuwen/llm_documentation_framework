#### doGetAudioSourceContentGrade()


 virtual ARA::ARAContentGrade ARADocumentControllerSpecialisation::doGetAudioSourceContentGrade ( const ARA::PlugIn::AudioSource \* audioSource, ARA::ARAContentType type ) protectedvirtual 
 

Override to implement getAudioSourceContentGrade() for all your supported content types.This function's result is returned from ARA::PlugIn::DocumentControllerDelegate::doGetAudioSourceContentGrade.