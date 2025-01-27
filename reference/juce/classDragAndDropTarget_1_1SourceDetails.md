Contains details about the source of a draganddrop operation.

Constructor & Destructor Documentation


◆ SourceDetails()


 DragAndDropTarget::SourceDetails::SourceDetails ( const var & description, Component \* sourceComponent, Point< int > localPosition ) noexcept 
 

Creates a SourceDetails object from its various settings.

Member Data Documentation


◆ description


 var DragAndDropTarget::SourceDetails::description 
 

A descriptor for the drag this is set DragAndDropContainer::startDragging().

◆ sourceComponent


 WeakReference<Component> DragAndDropTarget::SourceDetails::sourceComponent 
 

The component from the drag operation was started.

◆ localPosition


 Point<int> DragAndDropTarget::SourceDetails::localPosition 
 

The local position of the mouse, relative to the target component.Note that for calls such as isInterestedInDragSource(), this may be a null position.