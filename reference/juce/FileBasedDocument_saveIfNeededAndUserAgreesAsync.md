#### saveIfNeededAndUserAgreesAsync()


 void FileBasedDocument::saveIfNeededAndUserAgreesAsync ( std::function< void(SaveResult)> callback ) 
 

If the file needs saving, it'll ask the user if that's what they want to do, and save it if they say yes.If you've got a document open and want to close it (e.g. to quit the app), this is the method to call.If the document doesn't need saving the callback will be called with the value savedOk so you can go ahead and delete the document.If it does need saving it'll prompt the user, and if they say "discard changes" the callback will be called with savedOk, so again, you can safely delete the document.If the user clicks "cancel", the callback will be called with userCancelledSave, so you can abort the closedocument operation.And if they click "save changes", it'll try to save and the callback will be called with either savedOk, or failedToWriteToFile if there was a problem.See alsosaveAsync, saveAsAsync, saveAsInteractiveAsync