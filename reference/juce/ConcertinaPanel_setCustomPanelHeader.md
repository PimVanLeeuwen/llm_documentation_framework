#### setCustomPanelHeader()


 void ConcertinaPanel::setCustomPanelHeader ( Component \* panelComponent, 
 
 Component \* customHeaderComponent, 
 bool takeOwnership ) 

Sets a custom header Component for one of the panels.Parameters

 panelComponent the panel component to add the custom header to. 
 
 customHeaderComponent the custom component to use for the panel header. This can be nullptr to clear the custom header component and just use the standard LookAndFeel panel. 
 takeOwnership if true, then the PanelHolder will take ownership of the custom header component, and will delete it later when it's no longer needed. If false, it won't delete it, and you must make sure it doesn't get deleted while in use.