#### getCommonSettings()


 PropertiesFile \* ApplicationProperties::getCommonSettings ( bool returnUserPropsIfReadOnly ) 
 

Returns the common settings file.The first time this is called, it will create and load the properties file.Parameters

 returnUserPropsIfReadOnly if this is true, and the common properties file is readonly (e.g. because the user doesn't have permission to write to shared files), then this will return the user settings instead, (like getUserSettings() would do). This is handy if you'd like to write a value to the common settings, but if that's no possible, then you'd rather write to the user settings than none at all. If returnUserPropsIfReadOnly is false, this method will always return the common settings, even if any changes to them can't be saved. 
 



See alsogetUserSettings