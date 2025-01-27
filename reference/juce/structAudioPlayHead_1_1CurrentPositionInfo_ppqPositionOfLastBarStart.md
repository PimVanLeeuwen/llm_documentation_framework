#### ppqPositionOfLastBarStart


 double AudioPlayHead::CurrentPositionInfo::ppqPositionOfLastBarStart = 0 
 

The position of the start of the last bar, in units of quarternotes.This is the time from the start of the timeline to the start of the current bar, in ppq units.Note this value may be unavailable on some hosts, e.g. ProTools. If it's not available, the value will be 0.Referenced by AudioPlayHead::getCurrentPosition().