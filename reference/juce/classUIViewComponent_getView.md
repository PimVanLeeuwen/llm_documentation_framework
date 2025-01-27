#### getView()


 void \* UIViewComponent::getView ( ) const 
 

Returns the current UIView.Note: A void\* is returned here to avoid the needing to include the cocoa headers, so you should just cast the return value to an UIView\*.