#### applyChange()


 static bool ValueTreeSynchroniser::applyChange ( ValueTree & target, const void \* encodedChangeData, size\_t encodedChangeDataSize, UndoManager \* undoManager ) static 
 

Applies an encoded change to the given destination tree.When you implement a receiver for changes that were sent by the stateChanged() message, this is the function that you'll need to call to apply them to the target tree that you want to be synced.