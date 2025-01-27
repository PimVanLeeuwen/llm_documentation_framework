#### getCellComponent()


 Component \* TableListBox::getCellComponent ( int columnId, 
 
 int rowNumber ) const 

Returns the component that currently represents a given cell.If the component for this cell is offscreen or if the position is outofrange, this may return nullptr.See alsogetCellPosition