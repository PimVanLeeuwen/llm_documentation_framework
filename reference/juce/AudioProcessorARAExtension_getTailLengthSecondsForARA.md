#### getTailLengthSecondsForARA()


 bool AudioProcessorARAExtension::getTailLengthSecondsForARA ( double & tailLength ) const protected 
 

Implementation helper for AudioProcessor::getTailLengthSeconds().If bound to ARA, this traverses the instance roles to retrieve the respective tail time and returns true. Otherwise returns false and leaves tailLength unmodified.