#### releaseResourcesForARA()


 bool AudioProcessorARAExtension::releaseResourcesForARA ( ) protected 
 

Implementation helper for AudioProcessor::releaseResources().If bound to ARA, this traverses the instance roles to let them release resources and returns true. Otherwise returns false and does nothing.