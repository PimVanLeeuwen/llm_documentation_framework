#### noteOff()


 void MPEChannelAssigner::noteOff ( int noteNumber, 
 
 int midiChannel = 1 ) 

You must call this method for all noteoffs that you receive so that this class can keep track of the currently playing notes internally.You can specify the channel number the note off happened on. If you don't, it will look through all channels to find the registered midi note matching the given note number.