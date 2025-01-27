#### filterNewText()


 String TextEditor::LengthAndCharacterRestriction::filterNewText ( TextEditor & , const String & newInput ) overridevirtual 
 

This method is called whenever text is entered into the editor.An implementation of this class should check the input string, and return an edited version of it that should be used.Implements TextEditor::InputFilter.