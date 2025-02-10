#### isInterestedInFileDrag()


 virtual bool FileDragAndDropTarget::isInterestedInFileDrag ( const StringArray & files ) pure virtual 
 

Callback to check whether this target is interested in the set of files being offered.Note that this will be called repeatedly when the user is dragging the mouse around over your component, so don't do anything timeconsuming in here, like opening the files to have a look inside them!Parameters

 files the set of (absolute) pathnames of the files that the user is dragging 
 



Returnstrue if this component wants to receive the other callbacks regarding this type of object; if it returns false, no other callbacks will be made. Implemented in FilenameComponent, FileSearchPathListComponent, and TreeView.