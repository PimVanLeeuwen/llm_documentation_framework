#### getComponentForRowNumber()


 Component \* ListBox::getComponentForRowNumber ( int rowNumber ) const noexcept 
 

Finds the row component for a given row in the list.The component returned will have been created using ListBoxModel::refreshComponentForRow().If the component for this row is offscreen or if the row is outofrange, this will return nullptr.See alsogetRowContainingPosition