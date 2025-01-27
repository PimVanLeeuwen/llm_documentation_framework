#### getAudioProcessor()


 AudioProcessor \* AudioProcessorEditor::getAudioProcessor ( ) const noexcept 
 

Returns a pointer to the processor that this editor represents.This method is here to support legacy code, but it's easier to just use the AudioProcessorEditor::processor member variable directly to get this object.