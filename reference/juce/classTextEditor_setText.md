#### setText()


 void TextEditor::setText ( const String & newText, 
 
 bool sendTextChangeMessage = true ) 

Sets the entire content of the editor.This will clear the editor and insert the given text (using the current text colour and font). You can set the current text colour usingsetColour (TextEditor::textColourId, ...);
Component::setColourvoid setColour(int colourID, Colour newColour)Registers a colour to be used for a particular purpose.
TextEditor::textColourId@ textColourIdThe colour that will be used when text is added to the editor.Definition juce\_TextEditor.h:224
Parameters

 newText the text to add 
 
 sendTextChangeMessage if true, this will cause a change message to be sent to all the listeners. 



See alsoinsertTextAtCaret