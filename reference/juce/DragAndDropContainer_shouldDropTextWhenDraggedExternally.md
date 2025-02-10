#### shouldDropTextWhenDraggedExternally()


 virtual bool DragAndDropContainer::shouldDropTextWhenDraggedExternally ( const DragAndDropTarget::SourceDetails & sourceDetails, String & text ) protectedvirtual 
 

Override this if you want to be able to perform an external drag of text when the user drags outside of this container component.This method will be called when a drag operation moves outside the JUCE window, and if you want it to then perform a text draganddrop, copy the text you want to be dragged into the argument provided and return true.Parameters

 sourceDetails information about the source of the drag operation 
 
 text on return, the text you want to drag 



See alsoshouldDropFilesWhenDraggedExternally