#### removeRedundantPaths()


 void FileSearchPath::removeRedundantPaths ( ) 
 

Removes any directories that are actually subdirectories of one of the other directories in the search path.If the search is intended to be recursive, there's no point having nested folders in the search path, because they'll just get searched twice and you'll get duplicate results.e.g. if the path is "c:\abc\de;c:\abc", this method will simplify it to "c:\abc"