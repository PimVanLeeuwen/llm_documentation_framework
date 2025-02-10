#### performExternalDragDropOfFiles()


 static bool DragAndDropContainer::performExternalDragDropOfFiles ( const StringArray & files, bool canMoveFiles, Component \* sourceComponent = nullptr, std::function< void()> callback = nullptr ) static 
 

This performs an asynchronous draganddrop of a set of files to some external application.You can call this function in response to a mouseDrag callback, and it will use a native operating system draganddrop operation to move or copy some files to another application.Parameters

 files a list of filenames to drag 
 
 canMoveFiles if true, the app that receives the files is allowed to move the files to a new location (if this is appropriate). If false, the receiver is expected to make a copy of them. 
 sourceComponent normally, JUCE will assume that the component under the mouse is the source component of the drag, but you can use this parameter to override this. 
 callback an optional completion callback that will be called when the operation has ended. 



Returnstrue if the drag operation was successfully started, or false if it failed for some reason
See alsoperformExternalDragDropOfText