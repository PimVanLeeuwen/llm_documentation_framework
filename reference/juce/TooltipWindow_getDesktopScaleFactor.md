#### getDesktopScaleFactor()


 float TooltipWindow::getDesktopScaleFactor ( ) const overridevirtual 
 

Returns the default scale factor to use for this component when it is placed on the desktop.The default implementation of this method just returns the value from Desktop::getGlobalScaleFactor(), but it can be overridden if a particular component has different requirements. The method only used if this component is added to the desktop it has no effect for child components.Reimplemented from Component.