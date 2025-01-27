#### getPositionOfTrackStart()


 int AudioCDReader::getPositionOfTrackStart ( int trackNum ) const 
 

Finds the sample offset of the start of a track.Parameters

 trackNum the track number, where trackNum = 0 is the first track and trackNum = getNumTracks() means the end of the CD.