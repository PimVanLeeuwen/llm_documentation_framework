#### getApproximateMinMax()


 virtual void AudioThumbnailBase::getApproximateMinMax ( double startTime, double endTime, int channelIndex, float & minValue, float & maxValue ) const pure virtualnoexcept 
 

Reads the approximate min and max levels from a section of the thumbnail.The lowest and highest samples are returned in minValue and maxValue, but obviously because the thumb only stores lowresolution data, these numbers will only be a rough approximation of the true values.Implemented in AudioThumbnail.