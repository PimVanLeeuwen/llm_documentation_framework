#### minimiseButtonPressed()


 virtual void DocumentWindow::minimiseButtonPressed ( ) virtual 
 

Callback that is triggered when the minimise button is pressed.This function is only called when using a nonnative titlebar.The default implementation of this calls ResizableWindow::setMinimised(), but you can override it to do more customised behaviour.