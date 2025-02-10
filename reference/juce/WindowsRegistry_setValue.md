#### setValue() [4/4]


 static bool JUCE\_CALLTYPE WindowsRegistry::setValue ( const String & regValuePath, const MemoryBlock & value, WoW64Mode mode = WoW64\_Default ) static 
 

Sets a registry value as a binary block.This will take care of creating any groups needed to get to the given registry value.