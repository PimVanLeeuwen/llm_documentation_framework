#### paintRowBackground()


 virtual void TableListBoxModel::paintRowBackground ( Graphics & , int rowNumber, int width, int height, bool rowIsSelected ) pure virtual 
 

This must draw the background behind one of the rows in the table.The graphics context has its origin at the row's topleft, and your method should fill the area specified by the width and height parameters.Note that the rowNumber value may be greater than the number of rows in your list, so be careful that you don't assume it's less than getNumRows().