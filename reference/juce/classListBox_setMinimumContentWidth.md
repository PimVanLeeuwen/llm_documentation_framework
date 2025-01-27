#### setMinimumContentWidth()


 void ListBox::setMinimumContentWidth ( int newMinimumWidth ) 
 

Changes the width of the rows in the list.This can be used to make the list's row components wider than the list itself the width of the rows will be either the width of the list or this value, whichever is greater, and if the rows become wider than the list, a horizontal scrollbar will appear.The default value for this is 0, which means that the rows will always be the same width as the list.