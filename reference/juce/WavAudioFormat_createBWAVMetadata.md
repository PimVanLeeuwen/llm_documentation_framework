#### createBWAVMetadata()


 static StringPairArray WavAudioFormat::createBWAVMetadata ( const String & description, const String & originator, const String & originatorRef, Time dateAndTime, int64 timeReferenceSamples, const String & codingHistory ) static 
 

Utility function to fill out the appropriate metadata for a BWAV file.This just makes it easier than using the property names directly, and it fills out the time and date in the right format.