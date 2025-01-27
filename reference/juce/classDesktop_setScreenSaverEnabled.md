#### setScreenSaverEnabled()


 static void Desktop::setScreenSaverEnabled ( bool isEnabled ) static 
 

This lets you prevent the screensaver from becoming active.Handy if you're running some sort of presentation app where having a screensaver appear would be annoying.Pass false to disable the screensaver, and true to reenable it. (Note that this won't enable a screensaver unless the user has actually set one up).The disablement will only happen while the JUCE application is the foreground process if another task is running in front of it, then the screensaver will be unaffected.See alsoisScreenSaverEnabled