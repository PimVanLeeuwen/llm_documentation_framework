#### getIndexInLine()


 int CodeDocument::Position::getIndexInLine ( ) const noexcept 
 

Returns the number of characters from the start of the line.Note that this value is NOT the column at which the position appears in an editor. If the line contains any tab characters, the relationship of the index to its visual position depends on the number of spaces per tab being used!