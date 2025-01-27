#### getBinaryValue()


 static uint32 JUCE\_CALLTYPE WindowsRegistry::getBinaryValue ( const String & regValuePath, MemoryBlock & resultData, WoW64Mode mode = WoW64\_Default ) static 
 

Reads a binary block from the registry.The path is a string for the entire path of a value in the registry, e.g. "HKEY\_CURRENT\_USER\Software\foo\bar"Returnsa DWORD indicating the type of the key.