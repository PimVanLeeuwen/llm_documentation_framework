#### getHelp()


 virtual String AccessibilityHandler::getHelp ( ) const virtual 
 

Some help text for the UI element (if required).This may be read out by the system. This string functions in a similar way to a tooltip, for example "Click to open window." for a button which opens a window.The default implementation will call `Component::getHelpText()`, but you can override this to return a different string if required.This must be a localised string.