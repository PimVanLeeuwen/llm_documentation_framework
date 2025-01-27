#### textDragEnter()


 virtual void TextDragAndDropTarget::textDragEnter ( const String & text, int x, int y ) virtual 
 

Callback to indicate that some text is being dragged over this component.This gets called when the user moves the mouse into this component while dragging.Use this callback as a trigger to make your component repaint itself to give the user feedback about whether the text can be dropped here or not.Parameters

 text the text that the user is dragging 
 
 x the mouse x position, relative to this component 
 y the mouse y position, relative to this component