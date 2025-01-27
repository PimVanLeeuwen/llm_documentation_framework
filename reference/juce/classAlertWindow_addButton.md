#### addButton()


 void AlertWindow::addButton ( const String & name, 
 
 int returnValue, 
 const KeyPress & shortcutKey1 = KeyPress(), 
 const KeyPress & shortcutKey2 = KeyPress() ) 

Adds a button to the window.Parameters

 name the text to show on the button 
 
 returnValue the value that should be returned from runModalLoop() if this is the button that the user presses. 
 shortcutKey1 an optional key that can be pressed to trigger this button 
 shortcutKey2 a second optional key that can be pressed to trigger this button