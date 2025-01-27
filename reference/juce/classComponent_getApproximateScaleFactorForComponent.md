#### getApproximateScaleFactorForComponent()


 static float JUCE\_CALLTYPE Component::getApproximateScaleFactorForComponent ( const Component \* targetComponent ) static 
 

Returns the approximate scale factor for a given component by traversing its parent hierarchy and applying each transform and finally scaling this by the global scale factor.