#### setContentOwned()


 void ResizableWindow::setContentOwned ( Component \* newContentComponent, 
 
 bool resizeToFitWhenContentChangesSize ) 

Changes the current content component.This sets a component that will be placed in the centre of the ResizableWindow, (leaving a space around the edge for the border).You should never add components directly to a ResizableWindow (or any of its subclasses) with addChildComponent(). Instead, add them to the content component.Parameters

 newContentComponent the new component to use this component will be deleted when it's no longer needed (i.e. when the window is deleted or a new content component is set for it). To set a component that this window will not delete, call setContentNonOwned() instead. 
 
 resizeToFitWhenContentChangesSize if true, then the ResizableWindow will maintain its size such that it always fits around the size of the content component. If false, the new content will be resized to fit the current space available.