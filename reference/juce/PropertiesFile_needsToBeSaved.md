#### needsToBeSaved()


 bool PropertiesFile::needsToBeSaved ( ) const 
 

Returns true if the properties have been altered since the last time they were saved.The file is flagged as needing to be saved when you change a value, but you can explicitly set this flag with setNeedsToBeSaved().