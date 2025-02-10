#### close()


 void ScopedMessageBox::close ( ) 
 

Closes the message box, if it is currently showing.This is also called automatically during ~ScopedMessageBox. This is useful if you want to display a message corresponding to a particular view, and hide the message automatically when the view is hidden. This situation commonly arises when displaying messages in plugin editors.