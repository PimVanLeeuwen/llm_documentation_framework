#### doGetAudioModificationContentGrade()


 virtual ARA::ARAContentGrade ARADocumentControllerSpecialisation::doGetAudioModificationContentGrade ( const ARA::PlugIn::AudioModification \* audioModification, ARA::ARAContentType type ) protectedvirtual 
 

Override to implement getAudioModificationContentGrade() for all your supported content types.For readonly data directly inherited from the underlying audio source you can just delegate the call to the audio source, but usereditable modification data must be specifically handled here.This function's result is returned from ARA::PlugIn::DocumentControllerDelegate::doGetAudioModificationContentGrade.