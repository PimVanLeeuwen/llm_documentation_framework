#### shouldDropFilesWhenDraggedExternally()


 virtual bool DragAndDropContainer::shouldDropFilesWhenDraggedExternally ( const DragAndDropTarget::SourceDetails & sourceDetails, StringArray & files, bool & canMoveFiles ) protectedvirtual 
 

Override this if you want to be able to perform an external drag of a set of files when the user drags outside of this container component.This method will be called when a drag operation moves outside the JUCE window, and if you want it to then perform a file draganddrop, add the filenames you want to the array passed in, and return true.Parameters

 sourceDetails information about the source of the drag operation 
 
 files on return, the filenames you want to drag 
 canMoveFiles on return, true if it's ok for the receiver to move the files; false if it must make a copy of them (see the performExternalDragDropOfFiles() method) 



See alsoperformExternalDragDropOfFiles, shouldDropTextWhenDraggedExternally