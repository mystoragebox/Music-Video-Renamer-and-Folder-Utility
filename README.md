# Music Video Renamer and Folder Utility
 I was trying to find an easy way to make my music video collection more Jellyfin and Emby friendly. It's not limited to videos, it can rename and move any file as long as it meets the requirements.
## What Does It Do?
 For example it will turn `folder/artist - song.mp4` into `folder/artist/song.mp4`. All my videos are in this format so it has no problems. If the script can't find the delimiter, in this case ` - ` it will skip the file. After it's finished the operation it will print all the changes it's made.
### How To Use It
 It requires Python and basic knowledge of command line.
### Variables You Can Change
 base is the location of the files to be edited. Recommended to copy script to same folder and leave as is.
```python
base = ''
```
 The delimiter is what you use to break up the filename to make the folder.
```python
delimiter = ' - '
```
 The script asks you if you would like to continue on each file. If you want to disable this delete line 26 
```python
print('This Ok? Artist: ' + splt[0] + ' Song: ' + splt[1])
```
 and change line 27 to
```python
contin = 'y'
```
