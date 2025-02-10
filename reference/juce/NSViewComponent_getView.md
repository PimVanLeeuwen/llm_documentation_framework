#### getView()


 void \* NSViewComponent::getView ( ) const 
 

Returns the current NSView.Note: A void\* is returned here to avoid the needing to include the cocoa headers, so you should just cast the return value to an NSView\*.