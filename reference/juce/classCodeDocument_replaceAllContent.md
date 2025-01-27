#### replaceAllContent()


 void CodeDocument::replaceAllContent ( const String & newContent ) 
 

Clears the document and replaces it with some new text.This operation is undoable if you're trying to completely reset the document, you might want to also call clearUndoHistory() and setSavePoint() after using this method.