#### addShortcut()


 void Button::addShortcut ( const KeyPress & ) 
 

Assigns a shortcut key to trigger the button.The button registers itself with its toplevel parent component for keypresses.Note that a different way of linking buttons to keypresses is by using the setCommandToTrigger() method to invoke a command.See alsoclearShortcuts