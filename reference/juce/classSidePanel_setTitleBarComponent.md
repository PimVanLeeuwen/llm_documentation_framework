#### setTitleBarComponent()


 void SidePanel::setTitleBarComponent ( Component \* titleBarComponentToUse, 
 
 bool keepDismissButton, 
 bool deleteComponentWhenNoLongerNeeded = true ) 

Sets a custom component to be used for the title bar of this SidePanel, replacing the default.You can pass a nullptr to revert to the default title bar.Parameters

 titleBarComponentToUse the component to use as the title bar, or nullptr to use the default 
 
 keepDismissButton if false the specified component will take up the full width of the title bar including the dismiss button but if true, the default dismiss button will be kept 
 deleteComponentWhenNoLongerNeeded if true, the component will be deleted automatically when the SidePanel is deleted or when a different component is added. If false, the caller must manage the lifetime of the component 



See alsogetTitleBarComponent