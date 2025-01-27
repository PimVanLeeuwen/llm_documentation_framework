#### filename


 String DirectoryContentsList::FileInfo::filename 
 

The filename.This isn't a full pathname, it's just the last part of the path, same as you'd get from File::getFileName().To get the full pathname, use DirectoryContentsList::getDirectory().getChildFile (filename).