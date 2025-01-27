#### getTitle()


 virtual String AccessibilityHandler::getTitle ( ) const virtual 
 

The title of the UI element.This will be read out by the system and should be concise, preferably matching the visible title of the UI element (if any). For example, this might be the text of a button or a simple label.The default implementation will call `Component::getTitle()`, but you can override this to return a different string if required.If neither a name nor a description is provided then the UI element may be ignored by accessibility clients.This must be a localised string.