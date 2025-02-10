#### fileDragEnter()


 void FilenameComponent::fileDragEnter ( const StringArray & files, int x, int y ) overridevirtual 
 

Callback to indicate that some files are being dragged over this component.This gets called when the user moves the mouse into this component while dragging.Use this callback as a trigger to make your component repaint itself to give the user feedback about whether the files can be dropped here or not.Parameters

 files the set of (absolute) pathnames of the files that the user is dragging 
 
 x the mouse x position, relative to this component 
 y the mouse y position, relative to this component 


Reimplemented from FileDragAndDropTarget.