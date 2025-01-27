#### getEditorRendererInterface()


 EditorRendererInterface ARAHostModel::PlugInExtensionInstance::getEditorRendererInterface ( ) const 
 

Returns the EditorRendererInterface for the extension instance.Depending on what roles were passed into ARAHostDocumentController::bindDocumentToPluginInstance() one particular instance may not fulfill a given role. You can use EditorRendererInterface::isValid() to see if this interface was provided by the instance.