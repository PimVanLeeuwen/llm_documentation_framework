#### wantsLayerBackedView()


 virtual bool AudioProcessorEditor::wantsLayerBackedView ( ) const virtual 
 

The plugin wrapper will call this function to decide whether to use a layerbacked view to host the editor on macOS and iOS.Layerbacked views generally provide better performance, and are recommended in most situations. However, on older macOS versions (confirmed on 10.12 and 10.13), displaying an OpenGL context inside a layerbacked view can lead to deadlocks, so it is recommended to avoid layerbacked views when using OpenGL on these OS versions.The default behaviour of this function is to return false if and only if the juce\_opengl module is present and the current platform is macOS 10.13 or earlier.You may want to override this behaviour if your plugin has an option to enable and disable OpenGL rendering. If you know your plugin editor will never use OpenGL rendering, you can set this function to return true in all situations.

Member Data Documentation