#### setReadOnly()


 void TextEditor::setReadOnly ( bool shouldBeReadOnly ) 
 

Changes the editor to readonly mode.By default, the text editor is not readonly. If you're making it readonly, you might also want to call setCaretVisible (false) to get rid of the caret.The text can still be highlighted and copied when in readonly mode.See alsoisReadOnly, setCaretVisible