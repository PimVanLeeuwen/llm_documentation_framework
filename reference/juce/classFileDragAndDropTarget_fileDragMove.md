#### fileDragMove()


 virtual void FileDragAndDropTarget::fileDragMove ( const StringArray & files, int x, int y ) virtual 
 

Callback to indicate that the user is dragging some files over this component.This gets called when the user moves the mouse over this component while dragging. Normally overriding itemDragEnter() and itemDragExit() are enough, but this lets you know what happens inbetween.Parameters

 files the set of (absolute) pathnames of the files that the user is dragging 
 
 x the mouse x position, relative to this component 
 y the mouse y position, relative to this component 


Reimplemented in TreeView.