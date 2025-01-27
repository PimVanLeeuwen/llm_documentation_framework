#### searchForLevel()


 int64 AudioFormatReader::searchForLevel ( int64 startSample, 
 
 int64 numSamplesToSearch, 
 double magnitudeRangeMinimum, 
 double magnitudeRangeMaximum, 
 int minimumConsecutiveSamples ) 

Scans the source looking for a sample whose magnitude is in a specified range.This will read from the source, either forwards or backwards between two sample positions, until it finds a sample whose magnitude lies between two specified levels.If it finds a suitable sample, it returns its position; if not, it will return 1.There's also a minimumConsecutiveSamples setting to help avoid spikes or zerocrossing points when you're searching for a continuous range of samplesParameters

 startSample the first sample to look at 
 
 numSamplesToSearch the number of samples to scan. If this value is negative, the search will go backwards 
 magnitudeRangeMinimum the lowest magnitude (inclusive) that is considered a hit, from 0 to 1.0 
 magnitudeRangeMaximum the highest magnitude (inclusive) that is considered a hit, from 0 to 1.0 
 minimumConsecutiveSamples if this is > 0, the method will only look for a sequence of this many consecutive samples, all of which lie within the target range. When it finds such a sequence, it returns the position of the first inrange sample it found (i.e. the earliest one if scanning forwards, the latest one if scanning backwards)