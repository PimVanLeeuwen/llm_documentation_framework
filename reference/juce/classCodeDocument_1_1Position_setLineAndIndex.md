#### setLineAndIndex()


 void CodeDocument::Position::setLineAndIndex ( int newLineNumber, 
 
 int newIndexInLine ) 

Moves the position to a new line and index within the line.Note that the index is NOT the column at which the position appears in an editor. If the line contains any tab characters, the relationship of the index to its visual position depends on the number of spaces per tab being used!Lines are numbered from zero, and if the line or index are beyond the bounds of the document, they will be adjusted to keep them within its limits.