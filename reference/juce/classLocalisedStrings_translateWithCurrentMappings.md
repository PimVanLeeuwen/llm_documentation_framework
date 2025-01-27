#### translateWithCurrentMappings() [2/2]


 static String LocalisedStrings::translateWithCurrentMappings ( const char \* text ) static 
 

Tries to translate a string using the currently selected set of mappings.If no mapping has been set, or if the mapping doesn't contain a translation for the string, this will just return the original string.See also the TRANS() macro, which uses this method to do its translation.See alsosetCurrentMappings, getCurrentMappings