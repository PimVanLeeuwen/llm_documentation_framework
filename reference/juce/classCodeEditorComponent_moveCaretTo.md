#### moveCaretTo()


 void CodeEditorComponent::moveCaretTo ( const CodeDocument::Position & newPos, 
 
 bool selecting ) 

Moves the caret.If selecting is true, the section of the document between the current caret position and the new one will become selected. If false, any currently selected region will be deselected.