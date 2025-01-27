#### vibrationPattern


 Array<int> PushNotifications::Notification::vibrationPattern 
 

Optional: sets the vibration pattern in milliseconds.The first value indicates how long to wait until vibration starts. The second value indicates how long to vibrate. The third value will say how long to not vibrate and so on. For instance, if the pattern is: 1000, 2000, 3000, 4000 then one second after receiving a notification the device will vibrate for two seconds, followed by 3 seconds of no vibration and finally, 4 seconds of vibration.