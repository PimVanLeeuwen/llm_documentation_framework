#### setInputFilter()


 void TextEditor::setInputFilter ( InputFilter \* newFilter, 
 
 bool takeOwnership ) 

Sets an input filter that should be applied to this editor.The filter can be nullptr, to remove any existing filters. If takeOwnership is true, then the filter will be owned and deleted by the editor when no longer needed.