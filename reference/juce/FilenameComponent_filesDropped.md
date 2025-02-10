#### filesDropped()


 void FilenameComponent::filesDropped ( const StringArray & files, int x, int y ) overridevirtual 
 

Callback to indicate that the user has dropped the files onto this component.When the user drops the files, this get called, and you can use the files in whatever way is appropriate.Note that after this is called, the fileDragExit method may not be called, so you should clean up in here if there's anything you need to do when the drag finishes.Parameters

 files the set of (absolute) pathnames of the files that the user is dragging 
 
 x the mouse x position, relative to this component 
 y the mouse y position, relative to this component 


Implements FileDragAndDropTarget.