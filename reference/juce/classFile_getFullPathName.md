#### getFullPathName()


 const String & File::getFullPathName ( ) const noexcept 
 

Returns the complete, absolute path of this file.This includes the filename and all its parent folders. On Windows it'll also include the drive letter prefix; on Mac or Linux it'll be a complete path starting from the root folder.If you just want the file's name, you should use getFileName() or getFileNameWithoutExtension().See alsogetFileName, getRelativePathFrom Referenced by File::NaturalFileComparator::compareElements(), PluginHostType::getHostPath(), and StandalonePluginHolder::setLastFile().