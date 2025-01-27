#### setPositionMaintained()


 void CodeDocument::Position::setPositionMaintained ( bool isMaintained ) 
 

Allows the position to be automatically updated when the document changes.If this is set to true, the position will register with its document so that when the document has text inserted or deleted, this position will be automatically moved to keep it at the same position in the text.