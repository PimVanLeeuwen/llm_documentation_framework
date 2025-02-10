#### updateContent()


 void ListBox::updateContent ( ) 
 

Causes the list to refresh its content.Call this when the number of rows in the list changes, or if you want it to call refreshComponentForRow() on all the row components.This must only be called from the main message thread.