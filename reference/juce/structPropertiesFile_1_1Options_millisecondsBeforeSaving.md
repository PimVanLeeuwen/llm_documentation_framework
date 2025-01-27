#### millisecondsBeforeSaving


 int PropertiesFile::Options::millisecondsBeforeSaving 
 

If this is zero or greater, then after a value is changed, the object will wait for this amount of time and then save the file.If this zero, the file will be written to disk immediately on being changed (which might be slow, as it'll rewrite synchronously each time a valuechange method is called). If it is less than zero, the file won't be saved until save() or saveIfNeeded() are explicitly called. The default constructor sets this to a reasonable value of a few seconds, so you only need to change it if you need a special case.