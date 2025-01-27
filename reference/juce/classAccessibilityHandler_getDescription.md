#### getDescription()


 virtual String AccessibilityHandler::getDescription ( ) const virtual 
 

A short description of the UI element.This may be read out by the system. It should not include the type of the UI element and should ideally be a single word, for example "Open" for a button that opens a window.The default implementation will call `Component::getDescription()`, but you can override this to return a different string if required.If neither a name nor a description is provided then the UI element may be ignored by accessibility clients.This must be a localised string.