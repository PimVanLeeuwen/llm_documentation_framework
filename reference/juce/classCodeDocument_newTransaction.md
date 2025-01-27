#### newTransaction()


 void CodeDocument::newTransaction ( ) 
 

Begins a new undo transaction.The document itself will not call this internally, so relies on whatever is using the document to periodically call this to break up the undo sequence into sensible chunks.See alsoUndoManager::beginNewTransaction