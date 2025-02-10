#### findIndexesInTrack()


 Array< int > AudioCDReader::findIndexesInTrack ( int trackNumber ) 
 

Scans a track to find the position of any indexes within it.Parameters

 trackNumber the track to look in, where 0 is the first track on the disc 
 



Returnsan array of sample positions of any index points found (not including the index that marks the start of the track)