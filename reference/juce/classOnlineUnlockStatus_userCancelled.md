#### userCancelled()


 virtual void OnlineUnlockStatus::userCancelled ( ) virtual 
 

This method will be called if the user cancels the connection to the webserver by clicking the cancel button in OnlineUnlockForm::OverlayComp.The default implementation of this method does nothing but you should use it to cancel any WebInputStreams that may be connecting.Reimplemented in TracktionMarketplaceStatus.