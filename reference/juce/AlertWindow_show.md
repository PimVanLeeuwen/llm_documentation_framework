#### show()


 static int JUCE\_CALLTYPE AlertWindow::show ( const MessageBoxOptions & options ) static 
 

Shows a dialog box using the specified options.The box is shown modally, and the method will block until the user dismisses it.Parameters

 options the options to use when creating the dialog. 
 



Returnsthe index of the button that was clicked.
See alsoMessageBoxOptions