#### maximiseButtonPressed()


 void MultiDocumentPanelWindow::maximiseButtonPressed ( ) overridevirtual 
 

Callback that is triggered when the maximise button is pressed, or when the titlebar is doubleclicked.This function is only called when using a nonnative titlebar.The default implementation of this calls ResizableWindow::setFullScreen(), but you can override it to do more customised behaviour.Reimplemented from DocumentWindow.