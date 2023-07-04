import os
import openai

def transcribe_audio_to_srt(audio_path, api_key, output_path):
    openai.api_key = api_key

    audio_file= open(audio_path, "rb")

    # 调用 OpenAI 的 Audio.transcribe 方法进行音频转录
    response = openai.Audio.transcribe(
        "whisper-1",
        audio_file,
        audio="mp3",
        language="en",
        response_format="srt"
    )

    #print('response:', response)

    # 生成 SRT 字幕文件
    with open(output_path, 'w') as srt_file:
        srt_file.write(response)

    print("SRT 字幕文件已生成。")

# 输入 MP3 文件路径、OpenAI API 密钥和输出 SRT 文件路径
audio_path = 'test.mp3'
api_key = os.environ.get('OPENAI_API_KEY')
output_path = 'test.srt'

transcribe_audio_to_srt(audio_path, api_key, output_path)
