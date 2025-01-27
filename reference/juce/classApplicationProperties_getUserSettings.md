#### getUserSettings()


 PropertiesFile \* ApplicationProperties::getUserSettings ( ) 
 

Returns the user settings file.The first time this is called, it will create and load the properties file.Note that when you search the user PropertiesFile for a value that it doesn't contain, the common settings are used as a secondchance place to look. This is done via the PropertySet::setFallbackPropertySet() method by default the common settings are set to the fallback for the user settings.See alsogetCommonSettings