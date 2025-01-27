#### setName()


 void AudioProcessorParameterGroup::setName ( String newName ) 
 

Changes the name of the group.If you do this after the group has been added to an AudioProcessor, call updateHostDisplay() to inform the host of the change. Not all hosts support dynamic group name changes.