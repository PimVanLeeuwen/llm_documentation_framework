#### getCurrentDragDescription()


 var DragAndDropContainer::getCurrentDragDescription ( ) const 
 

Returns the description of the thing that's currently being dragged.If nothing's being dragged, this will return a null var, otherwise it'll return the var that was passed into startDragging().If you are using drag and drop in a multitouch environment then you should use the getDragDescriptionForIndex() method instead which takes a touch index parameter.See alsostartDragging, getDragDescriptionForIndex