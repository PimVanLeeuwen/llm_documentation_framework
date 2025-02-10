#### setDocumentEditedStatus()


 virtual bool ComponentPeer::setDocumentEditedStatus ( bool edited ) virtual 
 

If this type of window is capable of indicating that the document in it has been edited, then this changes its status.For example in OSX, this changes the appearance of the close button.Returnstrue if the window has a mechanism for showing this, or false if not.