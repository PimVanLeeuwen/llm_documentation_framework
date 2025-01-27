#### getSelectedItemIndex()


 int ComboBox::getSelectedItemIndex ( ) const 
 

Returns the index of the item that's currently shown in the box.If no item is selected, or if the text is editable and the user has entered something which isn't one of the items in the list, then this will return 1.See alsosetSelectedItemIndex, getSelectedId, getText