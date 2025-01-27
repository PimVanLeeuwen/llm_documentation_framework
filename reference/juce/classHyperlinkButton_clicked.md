#### clicked()


 void HyperlinkButton::clicked ( ) overrideprotectedvirtual 
 

This method is called when the button has been clicked.Subclasses can override this to perform whatever actions they need to do. In general, you wouldn't use this method to receive clicks, but should get your callbacks by attaching a std::function to the onClick callback, or adding a Button::Listener.See alsotriggerClick, onClick Reimplemented from Button.