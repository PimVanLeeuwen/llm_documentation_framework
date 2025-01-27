#### textDragExit()


 virtual void TextDragAndDropTarget::textDragExit ( const String & text ) virtual 
 

Callback to indicate that the mouse has moved away from this component.This gets called when the user moves the mouse out of this component while dragging the text.If you've used textDragEnter() to repaint your component and give feedback, use this as a signal to repaint it in its normal state.Parameters

 text the text that the user is dragging