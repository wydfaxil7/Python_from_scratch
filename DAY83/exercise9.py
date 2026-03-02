import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

voices = speaker.GetVoices()

# for i in range(voices.Count):
#     print(f"Voice {i}: {voices.Item(i).GetDescription()}")

speaker.Voice = voices.item(0)  # Change the index to select a different voice
l = ["Adil", "Fazil", "Shahbaz", "Sajid", "Shahid", "Shahid Afridi"]

for name in l: 
    s = f"Shoutout to {name}"
    print(s)
    speaker.Speak(s)