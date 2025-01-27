#### scrollEditorToPositionCaret()


 void TextEditor::scrollEditorToPositionCaret ( int desiredCaretX, 
 
 int desiredCaretY ) 

Attempts to scroll the text editor so that the caret ends up at a specified position.This won't affect the caret's position within the text, it tries to scroll the entire editor vertically and horizontally so that the caret is sitting at the given position (relative to the topleft of this component).Depending on the amount of text available, it might not be possible to scroll far enough for the caret to reach this exact position, but it will go as far as it can in that direction.