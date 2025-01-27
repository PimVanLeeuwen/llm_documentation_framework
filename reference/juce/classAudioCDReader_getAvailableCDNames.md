#### getAvailableCDNames()


 static StringArray AudioCDReader::getAvailableCDNames ( ) static 
 

Returns a list of names of Audio CDs currently available for reading.If there's a CD drive but no CD in it, this might return an empty list, or possibly a device that can be opened but which has no tracks, depending on the platform.See alsocreateReaderForCD