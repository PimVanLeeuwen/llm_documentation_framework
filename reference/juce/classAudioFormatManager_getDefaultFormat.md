#### getDefaultFormat()


 AudioFormat \* AudioFormatManager::getDefaultFormat ( ) const 
 

Returns the format which has been set as the default one.You can set a format as being the default when it is registered. It's useful when you want to write to a file, because the best format may change between platforms, e.g. AIFF is preferred on the Mac, WAV on Windows.If none has been set as the default, this method will just return the first one in the list.