# SubtitleToJson
Converts subtitles to json with removing spaces and time details.

## Usage
To create json file run the following code. If you want start and end time, you have to pass `t` parameter after the subtitle's name.

`python sub_to_json.py [subtitle file name]`

##Example
test.srt:
```
1
00:01:56,840 --> 00:01:59,140
Dolores?

3
00:01:59,226 --> 00:02:00,675
Yes.

3
00:02:00,761 --> 00:02:03,061
Do you know where you are?

4
00:02:03,180 --> 00:02:04,679
I...

5
00:02:06,266 --> 00:02:08,900
I'm in a dream.
```
test.json which has been created with `python sub_to_json.py test.srt`:
```
[{"Number": 1, "Text": "Dolores?"},
{"Number": 2, "Text": "Yes."},
{"Number": 3, "Text": "Do you know where you are?"},
{"Number": 4, "Text": "I..."},
{"Number": 5, "Text": "I'm in a dream."}]
```

test.json which has been created with `python sub_to_json.py test.srt t`:
```
[{"Number": 1, "StartTime": 00:01:56:840, "EndTime": 00:01:59:140,"Text": " Dolores?"},
{"Number": 2, "StartTime": 00:01:59:226, "EndTime": 00:02:00:675,"Text": " Yes."},
{"Number": 3, "StartTime": 00:02:00:761, "EndTime": 00:02:03:061,"Text": " Do you know where you are?"},
{"Number": 4, "StartTime": 00:02:03:180, "EndTime": 00:02:04:679,"Text": " I..."},
{"Number": 5, "StartTime": 00:02:06:266, "EndTime": 00:02:08:900,"Text": " I'm in a dream."}]
```
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
