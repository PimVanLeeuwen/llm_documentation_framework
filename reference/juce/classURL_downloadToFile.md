#### downloadToFile() [2/2]


 std::unique\_ptr< DownloadTask > URL::downloadToFile ( const File & targetLocation, 
 
 const DownloadTaskOptions & options ) 

Download the URL to a file.This method attempts to download the URL to a given file location.Using this method to download files on mobile is less flexible but more reliable than using createInputStream or WebInputStreams as it will attempt to download the file using a native OS background network task. Such tasks automatically deal with network reconnections and continuing your download while your app is suspended.