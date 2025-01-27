#### addKeyPress()


 void KeyPressMappingSet::addKeyPress ( CommandID commandID, 
 
 const KeyPress & newKeyPress, 
 int insertIndex = 1 ) 

Assigns a keypress to a command.If the keypress is already assigned to a different command, it will first be removed from that command, to avoid it triggering multiple functions.Parameters

 commandID the ID of the command that you want to add a keypress to. If this is 0, the keypress will be removed from anything that it was previously assigned to, but not reassigned 
 
 newKeyPress the new keypress 
 insertIndex if this is less than zero, the key will be appended to the end of the list of keypresses; otherwise the new keypress will be inserted into the existing list at this index