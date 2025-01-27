#### convertToBase64()


 static bool Base64::convertToBase64 ( OutputStream & base64Result, const void \* sourceData, size\_t sourceDataSize ) static 
 

Converts a binary block of data into a base64 string.This will write the resulting string data to the given stream. If a write error occurs with the stream, the method will terminate and return false.