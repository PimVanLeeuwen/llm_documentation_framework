#### addTab()


 void TabbedComponent::addTab ( const String & tabName, 
 
 Colour tabBackgroundColour, 
 Component \* contentComponent, 
 bool deleteComponentWhenNotNeeded, 
 int insertIndex = 1 ) 

Adds a tab to the tabbar.The component passed in will be shown for the tab. If deleteComponentWhenNotNeeded is true, then the TabbedComponent will take ownership of the component and will delete it when the tab is removed or when this object is deleted.See alsoTabbedButtonBar::addTab