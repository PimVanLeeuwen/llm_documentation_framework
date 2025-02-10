#### getLastDocumentOpened()


 virtual File FileBasedDocument::getLastDocumentOpened ( ) protectedpure virtual 
 

This is used for dialog boxes to make them open at the last folder you were using.getLastDocumentOpened() and setLastDocumentOpened() are used to store the last document that was used you might want to store this value in a static variable, or even in your application's properties. It should be a global setting rather than a property of this object.This method works very well in conjunction with a RecentlyOpenedFilesList object to manage your recentfiles list.As a default value, it's ok to return File(), and the document object will use a sensible one instead.See alsoRecentlyOpenedFilesList