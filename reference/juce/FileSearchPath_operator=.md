#### operator=() [2/2]


 FileSearchPath & FileSearchPath::operator= ( const String & path ) 
 

Uses a string containing a list of pathnames to reinitialise this list.This search path is cleared and the semicolon or commaseparated folders in this string are added instead. e.g. "/foo/bar;/foo/moose;/fish/moose"