#### getRowContainingPosition()


 int ListBox::getRowContainingPosition ( int x, int y ) const noexcept 
 

Finds the row index that contains a given x,y position.The position is relative to the ListBox's topleft. If no row exists at this position, the method will return 1.See alsogetComponentForRowNumber