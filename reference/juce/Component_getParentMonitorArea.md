#### getParentMonitorArea()


 Rectangle< int > Component::getParentMonitorArea ( ) const 
 

Returns the screen coordinates of the monitor that contains this component.If there's only one monitor, this will return its size if there are multiple monitors, it will return the area of the monitor that contains the component's centre.