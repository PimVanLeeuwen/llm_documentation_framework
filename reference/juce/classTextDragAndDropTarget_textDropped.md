#### textDropped()


 virtual void TextDragAndDropTarget::textDropped ( const String & text, int x, int y ) pure virtual 
 

Callback to indicate that the user has dropped the text onto this component.When the user drops the text, this get called, and you can use the text in whatever way is appropriate.Note that after this is called, the textDragExit method may not be called, so you should clean up in here if there's anything you need to do when the drag finishes.Parameters

 text the text that the user is dragging 
 
 x the mouse x position, relative to this component 
 y the mouse y position, relative to this component