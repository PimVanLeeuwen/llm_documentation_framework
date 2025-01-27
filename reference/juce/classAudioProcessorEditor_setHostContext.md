#### setHostContext()


 void AudioProcessorEditor::setHostContext ( AudioProcessorEditorHostContext \* context ) noexcept 
 

Sets a context object that can be queried to find information that the host makes available to the plugin.You will only need to call this function if you are implementing a plugin host.