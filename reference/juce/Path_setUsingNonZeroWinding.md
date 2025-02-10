#### setUsingNonZeroWinding()


 void Path::setUsingNonZeroWinding ( bool isNonZeroWinding ) noexcept 
 

Changes the windingrule to be used when filling the path.If set to true (which is the default), then the path uses a nonzerowinding rule to determine which points are inside the path. If set to false, it uses an alternatewinding rule.The windingrule comes into play when areas of the shape overlap other areas, and determines whether the overlapping regions are considered to be inside or outside.Changing this value just sets a flag it doesn't affect the contents of the path.See alsoisUsingNonZeroWinding Referenced by LowLevelGraphicsContext::drawEllipse().