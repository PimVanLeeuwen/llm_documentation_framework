#### addChild() [2/2]


template<typename ParameterOrGroup , typename... Args> 

 void AudioProcessorParameterGroup::addChild ( std::unique\_ptr< ParameterOrGroup > firstChild, 
 
 Args &&... remainingChildren ) 

Adds multiple parameters or subgroups to this group.Do not add children to a group which has itself already been added to the AudioProcessor the new elements will be ignored.