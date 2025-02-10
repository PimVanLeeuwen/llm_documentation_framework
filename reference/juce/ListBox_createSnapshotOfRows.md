#### createSnapshotOfRows()


 virtual ScaledImage ListBox::createSnapshotOfRows ( const SparseSet< int > & rows, int & x, int & y ) virtual 
 

This fairly obscure method creates an image that shows the row components specified in rows (for example, these could be the currently selected row components).It's a handy method for doing draganddrop, as it can be passed to the DragAndDropContainer for use as the drag image.Note that it will make the row components temporarily invisible, so if you're using custom components this could affect them if they're sensitive to that sort of thing.See alsoComponent::createComponentSnapshot