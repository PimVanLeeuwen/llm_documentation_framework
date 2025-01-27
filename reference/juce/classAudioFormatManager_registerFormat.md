#### registerFormat()


 void AudioFormatManager::registerFormat ( AudioFormat \* newFormat, 
 
 bool makeThisTheDefaultFormat ) 

Adds a format to the manager's list of available file types.The object passedin will be deleted by this object, so don't keep a pointer to it!If makeThisTheDefaultFormat is true, then the getDefaultFormat() method will return this one when called.