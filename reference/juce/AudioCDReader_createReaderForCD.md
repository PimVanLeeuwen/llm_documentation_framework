#### createReaderForCD()


 static AudioCDReader \* AudioCDReader::createReaderForCD ( int index ) static 
 

Tries to create an AudioFormatReader that can read from an Audio CD.Parameters

 index the index of one of the available CDs use getAvailableCDNames() to find out how many there are. 
 



Returnsa new AudioCDReader object, or nullptr if it couldn't be created. The caller will be responsible for deleting the object returned.