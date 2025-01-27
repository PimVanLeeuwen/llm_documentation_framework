#### performExternalDragDropOfText()


 static bool DragAndDropContainer::performExternalDragDropOfText ( const String & text, Component \* sourceComponent = nullptr, std::function< void()> callback = nullptr ) static 
 

This performs an asynchronous draganddrop of a block of text to some external application.You can call this function in response to a mouseDrag callback, and it will use a native operating system draganddrop operation to move or copy some text to another application.Parameters

 text the text to copy 
 
 sourceComponent Normally, JUCE will assume that the component under the mouse is the source component of the drag, but you can use this parameter to override this. 
 callback an optional completion callback that will be called when the operation has ended. 



Returnstrue if the drag operation was successfully started, or false if it failed for some reason
See alsoperformExternalDragDropOfFiles