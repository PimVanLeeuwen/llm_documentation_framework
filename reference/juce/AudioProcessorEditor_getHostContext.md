#### getHostContext()


 AudioProcessorEditorHostContext \* AudioProcessorEditor::getHostContext ( ) const noexcept 
 

Gets a context object, if one is available.Returns nullptr if the host does not provide any information that the editor can query.The returned pointer is nonowning, so do not attempt to free it.