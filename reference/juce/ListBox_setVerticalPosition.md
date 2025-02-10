#### setVerticalPosition()


 void ListBox::setVerticalPosition ( double newProportion ) 
 

Scrolls the list to a particular position.The proportion is between 0 and 1.0, so 0 scrolls to the top of the list, 1.0 scrolls to the bottom.If the total number of rows all fit onto the screen at once, then this method won't do anything.See alsogetVerticalPosition