#### paintListBoxItem()


 void FileSearchPathListComponent::paintListBoxItem ( int rowNumber, Graphics & g, int width, int height, bool rowIsSelected ) overridevirtual 
 

This method must be implemented to draw a row of the list.Note that the rowNumber value may be greater than the number of rows in your list, so be careful that you don't assume it's less than getNumRows().Implements ListBoxModel.