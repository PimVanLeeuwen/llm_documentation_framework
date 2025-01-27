#### hasControlPanel()


 virtual bool AudioIODevice::hasControlPanel ( ) const virtual 
 

True if this device can show a popup control panel for editing its settings.This is generally just true of ASIO devices. If true, you can call showControlPanel() to display it.