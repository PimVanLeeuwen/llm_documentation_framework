#### buttonPressed()


 virtual void AppleRemoteDevice::buttonPressed ( ButtonType buttonId, bool isDown ) pure virtual 
 

Override this method to receive the callback about a button press.The callback will happen on the application's message thread.Some buttons trigger matching up and down events, in which the isDown parameter will be true and then false. Others only send a single event when the button is pressed.