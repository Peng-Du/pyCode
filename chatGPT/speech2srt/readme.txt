1. Extract mp3 from mp4 via ffmpeg:
ffmpeg -i input.mp4 -vn -acodec libmp3lame output.mp3
2. Use the following speech2srt.py code to generate SRT subtitles from mp3

If the generated mp3 is too large, use the following command to adjust it:
ffmpeg -i test.mp3 -ar 44100 -b:a 128k -q:a 4 test-1.mp3

If timeouts occur, switch to a faster network