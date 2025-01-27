#### selectRangeOfRows()


 void ListBox::selectRangeOfRows ( int firstRow, 
 
 int lastRow, 
 bool dontScrollToShowThisRange = false ) 

Selects a set of rows.This will add these rows to the current selection, so you might need to clear the current selection first with deselectAllRows()Parameters

 firstRow the first row to select (inclusive) 
 
 lastRow the last row to select (inclusive) 
 dontScrollToShowThisRange if true, the list's position won't change; if false and the selected range is offscreen, it'll scroll to make sure that the range of rows is onscreen