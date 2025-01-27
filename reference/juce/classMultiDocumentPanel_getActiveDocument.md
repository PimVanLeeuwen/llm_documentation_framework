#### getActiveDocument()


 Component \* MultiDocumentPanel::getActiveDocument ( ) const noexcept 
 

Returns the document component that is currently focused or on top.If currently using floating windows, then this will be the component in the currently active window, or the top component if none are active.If it's currently in tabbed mode, then it'll return the component in the active tab.See alsosetActiveDocument