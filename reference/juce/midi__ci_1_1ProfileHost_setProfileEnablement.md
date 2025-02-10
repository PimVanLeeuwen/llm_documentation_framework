#### setProfileEnablement()


 void midi\_ci::ProfileHost::setProfileEnablement ( ProfileAtAddress , 
 
 int numChannels ) 

Activates or deactivates a profile on the specified group/channel.The profile should previously have been added with addProfile(). A positive value of numChannels will enable the profile, and a nonpositive value will disable it. This includes group and functionblock profiles; passing any positive value will enable the profile on the entire group or block.