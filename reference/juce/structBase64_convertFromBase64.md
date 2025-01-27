#### convertFromBase64()


 static bool Base64::convertFromBase64 ( OutputStream & binaryOutput, StringRef base64TextInput ) static 
 

Converts a base64 string back to its binary representation.This will write the decoded binary data to the given stream. If the string is not valid base64, the method will terminate and return false.