#### withFileToUpload()


 URL URL::withFileToUpload ( const String & parameterName, const File & fileToUpload, const String & mimeType ) const nodiscard 
 

Returns a copy of this URL, with a fileupload type parameter added to it.When performing a POST where one of your parameters is a binary file, this lets you specify the file.Note that the filename is stored, but the file itself won't actually be read until this URL is later used to create a network input stream. If you want to upload data from memory, use withDataToUpload().See alsowithDataToUpload