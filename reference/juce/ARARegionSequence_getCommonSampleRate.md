#### getCommonSampleRate()


 double ARARegionSequence::getCommonSampleRate ( ) const 
 

If all audio sources used by the playback regions in this region sequence have the same sample rate, this rate is returned here, otherwise 0.0 is returned.If the region sequence has no playback regions, this also returns 0.0.