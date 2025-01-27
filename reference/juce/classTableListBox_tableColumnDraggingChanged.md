#### tableColumnDraggingChanged()


 void TableListBox::tableColumnDraggingChanged ( TableHeaderComponent \* tableHeader, int columnIdNowBeingDragged ) overridevirtual 
 

This is called when the user begins or ends dragging one of the columns around.When the user starts dragging a column, this is called with the ID of that column. When they finish dragging, it is called again with 0 as the ID.Reimplemented from TableHeaderComponent::Listener.