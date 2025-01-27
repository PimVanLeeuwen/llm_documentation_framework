#### fileDragExit()


 void TreeView::fileDragExit ( const StringArray & files ) overridevirtual 
 

Callback to indicate that the mouse has moved away from this component.This gets called when the user moves the mouse out of this component while dragging the files.If you've used fileDragEnter() to repaint your component and give feedback, use this as a signal to repaint it in its normal state.Parameters

 files the set of (absolute) pathnames of the files that the user is dragging 
 


Reimplemented from FileDragAndDropTarget.