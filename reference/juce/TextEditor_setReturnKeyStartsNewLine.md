#### setReturnKeyStartsNewLine()


 void TextEditor::setReturnKeyStartsNewLine ( bool shouldStartNewLine ) 
 

Changes the behaviour of the return key.If set to true, the return key will insert a newline into the text; if false it will trigger a call to the TextEditor::Listener::textEditorReturnKeyPressed() method. By default this is set to false, and when true it will only insert newlines when in multiline mode (see setMultiLine()).