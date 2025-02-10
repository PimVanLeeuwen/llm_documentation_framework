#### prepareToPlayForARA()


 bool AudioProcessorARAExtension::prepareToPlayForARA ( double sampleRate, int samplesPerBlock, int numChannels, AudioProcessor::ProcessingPrecision precision ) protected 
 

Implementation helper for AudioProcessor::prepareToPlay().If bound to ARA, this traverses the instance roles to prepare them for play and returns true. Otherwise returns false and does nothing.