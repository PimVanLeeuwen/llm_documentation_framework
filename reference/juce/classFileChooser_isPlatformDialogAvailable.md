#### isPlatformDialogAvailable()


 static bool FileChooser::isPlatformDialogAvailable ( ) static 
 

Returns if a native filechooser is currently available on this platform.Note: On iOS this will only return true if you have iCloud permissions and codesigning enabled in the Projucer and have added iCloud containers to your app in Apple's online developer portal. Additionally, the user must have installed the iCloud app on their device and used the app at least once.