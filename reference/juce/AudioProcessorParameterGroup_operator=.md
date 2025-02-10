#### operator=()


 AudioProcessorParameterGroup & AudioProcessorParameterGroup::operator= ( AudioProcessorParameterGroup && ) 
 

Once a group has been added to an AudioProcessor don't try to mutate it by moving or swapping it this will crash most hosts.