#### saveAsInteractive()


 SaveResult FileBasedDocument::saveAsInteractive ( bool warnAboutOverwritingExistingFiles ) 
 

Prompts the user for a filename and tries to save to it.This will pop up a dialog box using the title, file extension and wildcard specified in the document's constructor, and asks the user for a file. If they pick one, the saveAs() method is used to try to save to this file.Parameters

 warnAboutOverwritingExistingFiles if true and the file exists, it'll ask the user first if they want to overwrite it 
 



See alsosaveIfNeededAndUserAgrees, save, saveAs