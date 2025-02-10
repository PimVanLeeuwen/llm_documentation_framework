#### getPlaybackRendererInterface()


 PlaybackRendererInterface ARAHostModel::PlugInExtensionInstance::getPlaybackRendererInterface ( ) const 
 

Returns the PlaybackRendererInterface for the extension instance.Depending on what roles were passed into ARAHostDocumentController::bindDocumentToPluginInstance() one particular instance may not fulfill a given role. You can use PlaybackRendererInterface::isValid() to see if this interface was provided by the instance.