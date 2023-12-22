import speech_recognition as sr

# 设置音频文件的位置
audio_file = 'AudioFrequency/'

# 创建sr对象
r = sr.Recognizer()

# 读取音频文件
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

# 识别音频文件
try:
    print(r.recognize_google_cloud(audio,language='zh-CN'))
except sr.UnknownValueError:
    raise 'Google Speech Recognition could not understand audio'
except sr.RequestError as e:
    raise 'Could not request results from Google Speech Recognition Service'
