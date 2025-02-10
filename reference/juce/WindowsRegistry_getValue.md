#### getValue()


 static String JUCE\_CALLTYPE WindowsRegistry::getValue ( const String & regValuePath, const String & defaultValue = String(), WoW64Mode mode = WoW64\_Default ) static 
 

Returns a string from the registry.The path is a string for the entire path of a value in the registry, e.g. "HKEY\_CURRENT\_USER\Software\foo\bar"