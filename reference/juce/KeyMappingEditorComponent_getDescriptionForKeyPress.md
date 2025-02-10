#### getDescriptionForKeyPress()


 virtual String KeyMappingEditorComponent::getDescriptionForKeyPress ( const KeyPress & key ) virtual 
 

This can be overridden to let you change the format of the string used to describe a keypress.This is handy if you're using nonstandard KeyPress objects, e.g. for custom keys that are triggered by something else externally. If you override the method, be sure to let the base class's method handle keys you're not interested in.