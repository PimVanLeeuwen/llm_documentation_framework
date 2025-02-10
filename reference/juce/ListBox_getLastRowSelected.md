#### getLastRowSelected()


 int ListBox::getLastRowSelected ( ) const 
 

Returns the last row that the user selected.This isn't the same as the highest row number that is currently selected if the user had multiplyselected rows 10, 5 and then 6 in that order, this would return 6.If nothing is selected, it will return 1.