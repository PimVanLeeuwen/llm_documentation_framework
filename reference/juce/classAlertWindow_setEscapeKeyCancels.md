#### setEscapeKeyCancels()


 void AlertWindow::setEscapeKeyCancels ( bool shouldEscapeKeyCancel ) 
 

If set to true and the window contains no buttons, then pressing the escape key will make the alert cancel its modal state.By default this setting is true turn it off if you don't want the box to respond to the escape key. Note that it is ignored if you have any buttons, and in that case you should give the buttons appropriate keypresses to trigger cancelling if you want to.