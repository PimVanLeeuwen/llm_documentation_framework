#### processBlockForARA() [2/2]


 bool AudioProcessorARAExtension::processBlockForARA ( AudioBuffer< float > & buffer, AudioProcessor::Realtime isNonRealtime, AudioPlayHead \* playhead ) protected 
 

Implementation helper for AudioProcessor::processBlock().If bound to ARA, this traverses the instance roles to let them process the block and returns true. Otherwise returns false and does nothing.Use this overload if your rendering code does not have a current positionInfo available.