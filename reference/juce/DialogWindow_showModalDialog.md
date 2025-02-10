#### showModalDialog()


 static int DialogWindow::showModalDialog ( const String & dialogTitle, Component \* contentComponent, Component \* componentToCentreAround, Colour backgroundColour, bool escapeKeyTriggersCloseButton, bool shouldBeResizable = false, bool useBottomRightCornerResizer = false ) static 
 

Easy way of quickly showing a dialog box containing a given component.Note: This method has been superseded by the DialogWindow::LaunchOptions structure, which does the same job with some extra flexibility. The showDialog method is here for backwards compatibility, but please use DialogWindow::LaunchOptions in new code.This will open and display a DialogWindow containing a given component, returning when the user clicks its close button.It returns the value that was returned by the dialog box's runModalLoop() call.To close the dialog programmatically, you should call exitModalState (returnValue) on the DialogWindow that is created. To find a pointer to this window from your contentComponent, you can do something like this:if (DialogWindow\* dw = contentComponent>findParentComponentOfClass<DialogWindow>())
 dw>exitModalState (1234);
Parameters

 dialogTitle the dialog box's title 
 
 contentComponent the content component for the dialog box. Make sure that this has been set to the size you want it to be before calling this method. The component won't be deleted by this call, so you can reuse it or delete it afterwards 
 componentToCentreAround if this is not a nullptr, it indicates a component that you'd like to show this dialog box in front of. See the DocumentWindow::centreAroundComponent() method for more info on this parameter 
 backgroundColour a colour to use for the dialog box's background colour 
 escapeKeyTriggersCloseButton if true, then pressing the escape key will cause the close button to be triggered 
 shouldBeResizable if true, the dialog window has either a resizable border, or a corner resizer 
 useBottomRightCornerResizer if shouldBeResizable is true, this indicates whether to use a border or corner resizer component. See ResizableWindow::setResizable()