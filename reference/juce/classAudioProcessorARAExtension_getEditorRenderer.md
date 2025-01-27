#### getEditorRenderer()


template<typename EditorRenderer\_t = ARAEditorRenderer> 

 EditorRenderer\_t \* AudioProcessorARAExtension::getEditorRenderer ( ) const noexcept 
 

Returns the result of ARA::PlugIn::PlugInExtension::getEditorRenderer() with the pointer cast to ARAEditorRenderer\*.If you have overridden ARADocumentControllerSpecialisation::doCreateEditorRenderer(), then you can use the template parameter to cast the pointers to your subclass of ARAEditorRenderer.