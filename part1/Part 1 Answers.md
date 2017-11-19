# Part 1:

13. When right clicking result.7z and opening it like so:

	<right click> -> <7zip> -> <open archive>

we are confronted with a message that states "Can not open file 'C:\Documents and Settings\Administrator\My Documents\Downloads\part1\result.7z' as archive"

But when opening result.7z like so:

	<right click> -> <7zip> -> <open archive> -> <7z>

we successfully open the result.7z archive but it only contains worm.bat. After, we successfully extracted and ran worm.bat

15. After renaming the file from "result.7z" to "result.gif", it immediately displayed the gif that was copied with "worm.7z." Prior to opening the gif, it is opened in Microsoft Picture and Fax Viewer

16. Explain what is happening....

- The main function for COPY is to copy one file from one location to another location. But it can also be used to create new files as seen in this part of the assignment. What this part of the assignment essentially did was append both "rick.gif" and "worm.7z" together as the source file and copied it to the target file named "result." /B allowed us to append the binary file "worm.bat" to "rick.gif" and copy it to the destination.

17. This is useful for hiding malicious files because we can hide malicious batch files behind pictures. After the batch file is successfully concatenated to the gif, a user will simply see a "harmless" gif but in reality a very malicious script is there as well. Essentially it is almost like a Trojan horse virus.

18. need to answer
