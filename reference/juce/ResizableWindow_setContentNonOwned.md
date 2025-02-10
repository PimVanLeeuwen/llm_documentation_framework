#### setContentNonOwned()


 void ResizableWindow::setContentNonOwned ( Component \* newContentComponent, 
 
 bool resizeToFitWhenContentChangesSize ) 

Changes the current content component.This sets a component that will be placed in the centre of the ResizableWindow, (leaving a space around the edge for the border).You should never add components directly to a ResizableWindow (or any of its subclasses) with addChildComponent(). Instead, add them to the content component.Parameters

 newContentComponent the new component to use this component will NOT be deleted by this component, so it's the caller's responsibility to manage its lifetime (it's ok to delete it while this window is still using it). To set a content component that the window will delete, call setContentOwned() instead. 
 
 resizeToFitWhenContentChangesSize if true, then the ResizableWindow will maintain its size such that it always fits around the size of the content component. If false, the new content will be resized to fit the current space available.