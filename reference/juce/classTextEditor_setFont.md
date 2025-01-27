#### setFont()


 void TextEditor::setFont ( const Font & newFont ) 
 

Sets the font to use for newly added text.This will change the font that will be used next time any text is added or entered into the editor. It won't change the font of any existing text to do that, use applyFontToAllText() instead.See alsoapplyFontToAllText