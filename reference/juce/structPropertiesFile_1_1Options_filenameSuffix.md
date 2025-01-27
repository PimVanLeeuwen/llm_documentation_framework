#### filenameSuffix


 String PropertiesFile::Options::filenameSuffix 
 

The suffix to use for your properties file.It doesn't really matter what this is you may want to use ".settings" or ".properties" or something. If the suffix includes the prefixing dot (for example ".settings") then the suffix of applicationName will be replaced with your suffix ("MyApp.exe" > "MyApp.settings"). If your filenameSuffix does NOT include the dot, then the suffix will be appended to the applicationName ("MyApp.exe" > "MyApp.exe.settings").