#### withParentComponent()


 Options PopupMenu::Options::withParentComponent ( Component \* parentComponent ) const nodiscard 
 

Sets a component that the popup menu will be drawn into.Some plugin formats, such as AUv3, dislike it when the plugin editor spawns additional windows. Some AUv3 hosts display pink backgrounds underneath transparent popup windows, which is confusing and can appear as though the plugin is malfunctioning. Setting a parent component will avoid this unwanted behaviour, but with the downside that the menu size will be constrained by the size of the parent component.