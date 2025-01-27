#### setKioskModeComponent()


 void Desktop::setKioskModeComponent ( Component \* componentToUse, 
 
 bool allowMenusAndBars = true ) 

Takes a component and makes it fullscreen, removing the taskbar, dock, etc.The component must already be on the desktop for this method to work. It will be resized to completely fill the screen and any extraneous taskbars, menu bars, etc will be hidden.To exit kiosk mode, just call setKioskModeComponent (nullptr). When this is called, the component that's currently being used will be resized back to the size and position it was in before being put into this mode.If allowMenusAndBars is true, things like the menu and dock (on mac) are still allowed to pop up when the mouse moves onto them. If this is false, it'll try to hide as much onscreen paraphernalia as possible.