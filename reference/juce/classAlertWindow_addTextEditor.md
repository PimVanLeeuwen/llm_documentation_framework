#### addTextEditor()


 void AlertWindow::addTextEditor ( const String & name, 
 
 const String & initialContents, 
 const String & onScreenLabel = String(), 
 bool isPasswordBox = false ) 

Adds a textbox to the window for entering strings.Parameters

 name an internal name for the textbox. This is the name to pass to the getTextEditorContents() method to find out what the user typedin. 
 
 initialContents a string to show in the text box when it's first shown 
 onScreenLabel if this is nonempty, it will be displayed next to the textbox to label it. 
 isPasswordBox if true, the text editor will display asterisks instead of the actual text 



See alsogetTextEditorContents