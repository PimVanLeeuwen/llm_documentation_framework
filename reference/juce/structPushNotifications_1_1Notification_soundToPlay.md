#### soundToPlay


 URL PushNotifications::Notification::soundToPlay 
 

Optional: empty when the notification should be silent.When the name is set to "default\_os\_sound", then a default sound will be used.For a custom sound on OSX, set the URL to the name of a sound file (preferably without an extension) and place the sound file directly in bundle's "Resources" directory (you can use "Xcode Resource" tickbox in Projucer to achieve that), i.e. it cannot be in a subdirectory of "Resources" like "Resources/sound". Alternatively, if a sound file cannot be found in bundle's "Resources" directory, the OS may look for the sound in the following paths: "~/Library/Sounds", "/Library/Sounds", "/Network/Library/Sounds", "/System/Library/Sounds".For a custom sound on iOS, set the URL to a relative path within your bundle, including file extension. For instance, if your bundle contains "sounds" folder with "my\_sound.caf" file, then the URL should be "sounds/my\_sound.caf".For a custom sound on Android, set URL to the name of a raw resource file (without an extension) that was included when exporting an Android project in Projucer (see "Extra Android Raw Resources" setting).