#### setCurrentMappings()


 static void LocalisedStrings::setCurrentMappings ( LocalisedStrings \* newTranslations ) static 
 

Selects the current set of mappings to be used by the system.The object you pass in will be automatically deleted when no longer needed, so don't keep a pointer to it. You can also pass in nullptr to remove the current mappings.See also the TRANS() macro, which uses the current set to do its translation.See alsotranslateWithCurrentMappings