#### getSelectedId()


 int ComboBox::getSelectedId ( ) const noexcept 
 

Returns the ID of the item that's currently shown in the box.If no item is selected, or if the text is editable and the user has entered something which isn't one of the items in the list, then this will return 0.See alsosetSelectedId, getSelectedItemIndex, getText