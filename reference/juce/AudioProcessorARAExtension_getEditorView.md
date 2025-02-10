#### getEditorView()


template<typename EditorView\_t = ARAEditorView> 

 EditorView\_t \* AudioProcessorARAExtension::getEditorView ( ) const noexcept 
 

Returns the result of ARA::PlugIn::PlugInExtension::getEditorView() with the pointer cast to ARAEditorView\*.If you have overridden ARADocumentControllerSpecialisation::doCreateEditorView(), then you can use the template parameter to cast the pointers to your subclass of ARAEditorView.