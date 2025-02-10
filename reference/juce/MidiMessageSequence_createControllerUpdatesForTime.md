#### createControllerUpdatesForTime()


 void MidiMessageSequence::createControllerUpdatesForTime ( int channelNumber, 
 
 double time, 
 Array< MidiMessage > & resultMessages ) 

Scans through the sequence to determine the state of any midi controllers at a given time.This will create a sequence of midi controller changes that can be used to set all midi controllers to the state they would be in at the specified time within this sequence.As well as controllers, it will also recreate the midi program number and pitch bend position.This function has special handling for the "bank select" and "data entry" controllers (0x00, 0x20, 0x06, 0x26, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65).If the sequence contains multiple bank select and program change messages, only the bank select messages immediately preceding the final program change message will be kept.All "data increment" and "data decrement" messages will be retained. Some hardware will ignore the requested increment/decrement values, so retaining all messages is the only way to ensure compatibility with all hardware."Parameter number" changes will be slightly condensed. Only the parameter number events immediately preceding each data entry event will be kept. The parameter number will also be set to its final value at the end of the sequence, if necessary.Parameters

 channelNumber the midi channel to look for, in the range 1 to 16. Controllers for other channels will be ignored. 
 
 time the time at which you want to find out the state there are no explicit units for this time measurement, it's the same units as used for the timestamps of the messages 
 resultMessages an array to which midi controllerchange messages will be added. This will be the minimum number of controller changes to recreate the state at the required time.