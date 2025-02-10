#### getColumnPosition()


 Rectangle< int > TableHeaderComponent::getColumnPosition ( int index ) const 
 

Returns the rectangle containing of one of the columns.The index is an index from 0 to the number of columns that are currently visible (hidden ones are not counted). It returns a rectangle showing the position of the column relative to this component's topleft. If the index is outofrange, an empty rectangle is returned.