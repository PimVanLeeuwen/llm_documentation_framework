#### removeCustomComponent()


 Component \* AlertWindow::removeCustomComponent ( int index ) 
 

Removes one of the custom components in the dialog box.Note that this won't delete it, it just removes the component from the windowParameters

 index a value 0 to (getNumCustomComponents() 1). Outofrange indexes will return nullptr 
 



Returnsthe component that was removed (or null) 
See alsogetNumCustomComponents, addCustomComponent