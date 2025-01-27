#### setHeaderComponent()


 void ListBox::setHeaderComponent ( std::unique\_ptr< Component > newHeaderComponent ) 
 

Sets a component that the list should use as a header.This will position the given component at the top of the list, maintaining the height of the component passedin, but rescaling it horizontally to match the width of the items in the listbox.The component will be deleted when setHeaderComponent() is called with a different component, or when the listbox is deleted.