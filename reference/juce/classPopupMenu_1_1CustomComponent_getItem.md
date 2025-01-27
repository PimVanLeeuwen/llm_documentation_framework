#### getItem()


 const PopupMenu::Item \* PopupMenu::CustomComponent::getItem ( ) const noexcept 
 

Returns a pointer to the Item that holds this custom component, if this component is currently held by an Item.You can query the Item for information that you might want to use in your paint() method, such as the item's enabled and ticked states.