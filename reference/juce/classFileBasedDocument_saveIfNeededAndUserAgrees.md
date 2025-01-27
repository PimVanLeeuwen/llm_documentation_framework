#### saveIfNeededAndUserAgrees()


 SaveResult FileBasedDocument::saveIfNeededAndUserAgrees ( ) 
 

If the file needs saving, it'll ask the user if that's what they want to do, and save it if they say yes.If you've got a document open and want to close it (e.g. to quit the app), this is the method to call.If the document doesn't need saving it'll return the value savedOk so you can go ahead and delete the document.If it does need saving it'll prompt the user, and if they say "discard changes" it'll return savedOk, so again, you can safely delete the document.If the user clicks "cancel", it'll return userCancelledSave, so if you can abort the closedocument operation.And if they click "save changes", it'll try to save and either return savedOk, or failedToWriteToFile if there was a problem.See alsosave, saveAs, saveAsInteractive