#### getTabContentComponent()


 Component \* TabbedComponent::getTabContentComponent ( int tabIndex ) const noexcept 
 

Returns the content component that was added for the given index.Be careful not to reposition or delete the components that are returned, as this will interfere with the TabbedComponent's behaviour.