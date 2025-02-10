#### insertTextAtCaret()


 void TextEditor::insertTextAtCaret ( const String & textToInsert ) overridevirtual 
 

Inserts some text at the current caret position.If a section of the text is highlighted, it will be replaced by this string, otherwise it will be inserted.To delete a section of text, you can use setHighlightedRegion() to highlight it, and call insertTextAtCaret (String()).See alsosetCaretPosition, getCaretPosition, setHighlightedRegion Implements TextInputTarget.