#### findFormatForFileExtension()


 AudioFormat \* AudioFormatManager::findFormatForFileExtension ( const String & fileExtension ) const 
 

Looks for which of the known formats is listed as being for a given file extension.The extension may have a dot before it, so e.g. ".wav" or "wav" are both ok.