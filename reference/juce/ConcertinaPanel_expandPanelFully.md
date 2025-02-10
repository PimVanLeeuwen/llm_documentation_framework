#### expandPanelFully()


 bool ConcertinaPanel::expandPanelFully ( Component \* panelComponent, 
 
 bool animate ) 

Attempts to make one of the panels fullheight.The panelComponent must point to a valid panel component. If this component has had a maximum size set, then it will be expanded to that size. Otherwise, it'll fill as much of the total space as possible.