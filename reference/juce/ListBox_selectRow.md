#### selectRow()


 void ListBox::selectRow ( int rowNumber, 
 
 bool dontScrollToShowThisRow = false, 
 bool deselectOthersFirst = true ) 

Selects a row.If the row is already selected, this won't do anything.Parameters

 rowNumber the row to select 
 
 dontScrollToShowThisRow if true, the list's position won't change; if false and the selected row is offscreen, it'll scroll to make sure that row is onscreen 
 deselectOthersFirst if true and there are multiple selections, these will first be deselected before this item is selected 



See alsoisRowSelected, selectRowsBasedOnModifierKeys, flipRowSelection, deselectRow, deselectAllRows, selectRangeOfRows