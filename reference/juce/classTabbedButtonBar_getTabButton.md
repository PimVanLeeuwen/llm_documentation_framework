#### getTabButton()


 TabBarButton \* TabbedButtonBar::getTabButton ( int index ) const 
 

Returns the button for a specific tab.The button that is returned may be deleted later by this component, so don't hang on to the pointer that is returned. A null pointer may be returned if the index is out of range.