#### withDataToUpload()


 URL URL::withDataToUpload ( const String & parameterName, const String & filename, const MemoryBlock & fileContentToUpload, const String & mimeType ) const nodiscard 
 

Returns a copy of this URL, with a fileupload type parameter added to it.When performing a POST where one of your parameters is a binary file, this lets you specify the file content.Note that the filename parameter should not be a full path, it's just the last part of the filename.See alsowithFileToUpload