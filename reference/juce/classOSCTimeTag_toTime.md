#### toTime()


 Time OSCTimeTag::toTime ( ) const noexcept 
 

Returns a juce::Time object representing the same time as the OSCTimeTag.If the OSCTimeTag has the special value representing "immediately", the resulting juce::Time object will represent an arbitrary point of time (but guaranteed to be in the past), since juce::Time does not have such a special value.