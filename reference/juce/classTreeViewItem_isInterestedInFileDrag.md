#### isInterestedInFileDrag()


 virtual bool TreeViewItem::isInterestedInFileDrag ( const StringArray & files ) virtual 
 

If you want your item to be able to have files draganddropped onto it, implement this method and return true.If you return true and allow some files to be dropped, you'll also need to implement the filesDropped() method to do something with them.Note that this will be called often, so make your implementation very quick! There's certainly no time to try opening the files and having a think about what's inside them!For responding to internal draganddrop of other types of object, see isInterestedInDragSource().See alsoFileDragAndDropTarget::isInterestedInFileDrag, isInterestedInDragSource