#### getSampleRange()


 Range< int64 > ARAPlaybackRegion::getSampleRange ( double sampleRate, 
 
 IncludeHeadAndTail includeHeadAndTail = IncludeHeadAndTail::no ) const 

Returns the playback sample range of this playback region.Parameters

 sampleRate The rate at which the sample position should be calculated from the time range. 
 
 includeHeadAndTail Whether or not the range includes the head and tail time of all playback regions in the sequence.