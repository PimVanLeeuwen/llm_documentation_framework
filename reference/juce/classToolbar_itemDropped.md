#### itemDropped()


 void Toolbar::itemDropped ( const SourceDetails & dragSourceDetails ) overridevirtual 
 

Callback to indicate that the user has dropped something onto this component.When the user drops an item this get called, and you can use the description to work out whether your object wants to deal with it or not.Note that after this is called, the itemDragExit method may not be called, so you should clean up in here if there's anything you need to do when the drag finishes.Parameters

 dragSourceDetails contains information about the source of the drag operation. 
 


Implements DragAndDropTarget.