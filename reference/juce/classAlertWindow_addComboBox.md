#### addComboBox()


 void AlertWindow::addComboBox ( const String & name, 
 
 const StringArray & items, 
 const String & onScreenLabel = String() ) 

Adds a dropdown list of choices to the box.After the box has been shown, the getComboBoxComponent() method can be used to find out which item the user picked.Parameters

 name the label to use for the dropdown list 
 
 items the list of items to show in it 
 onScreenLabel if this is nonempty, it will be displayed next to the combobox to label it. 



See alsogetComboBoxComponent