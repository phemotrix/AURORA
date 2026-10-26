"""
Generates a pleasant 10-second demo .wav audio file with melodic synthesizer chords
and an accompanying .lrc lyrics file for immediate testing.
"""
import math
import os
import wave
import struct

output_dir = os.path.dirname(os.path.abspath(__file__))
sample_rate = 44100
duration = 10.0  # seconds
num_samples = int(sample_rate * duration)

# Frequencies for a lush ambient chord progression (Cmaj7 -> Am7)
chords = [
    ([261.63, 329.63, 392.00, 493.88], 5.0), # Cmaj7 for 5s
    ([220.00, 261.63, 329.63, 392.00], 5.0)  # Am7 for 5s
]

wav_filename = os.path.join(output_dir, "Aurora_Ambient_Demo.wav")

with wave.open(wav_filename, "w") as wav_file:
    wav_file.setnchannels(2) # Stereo
    wav_file.setsampwidth(2) # 16-bit
    wav_file.setframerate(sample_rate)

    t = 0.0
    dt = 1.0 / sample_rate

    for chord_freqs, chord_dur in chords:
        samples_in_chord = int(sample_rate * chord_dur)
        for i in range(samples_in_chord):
            # Attack and decay envelope
            env = min(i / (sample_rate * 0.4), 1.0) * min((samples_in_chord - i) / (sample_rate * 0.4), 1.0)
            
            sample_left = 0.0
            sample_right = 0.0
            for idx, freq in enumerate(chord_freqs):
                pan = (idx / (len(chord_freqs) - 1)) if len(chord_freqs) > 1 else 0.5
                val = math.sin(2.0 * math.pi * freq * t) * 0.22
                val += math.sin(4.0 * math.pi * freq * t) * 0.06
                
                sample_left += val * (1.0 - pan * 0.6)
                sample_right += val * (pan * 0.6 + 0.4)

            sample_left = int(max(-32767, min(32767, sample_left * env * 32767)))
            sample_right = int(max(-32767, min(32767, sample_right * env * 32767)))

            wav_file.writeframes(struct.pack('<hh', sample_left, sample_right))
            t += dt

print(f"Generated {wav_filename}")

# Also generate matching demo .lrc file
lrc_content = """[00:00.00] Welcome to Aurora Glass Audio
[00:02.50] Frosted Glass • Pure Offline Immersion
[00:05.00] Dynamic Mesh Colors Flow With Your Music
[00:07.50] Enjoy Seamless Desktop Audio
"""

lrc_filename = os.path.join(output_dir, "Aurora_Ambient_Demo.lrc")
with open(lrc_filename, "w", encoding="utf-8") as f:
    f.write(lrc_content)

print(f"Generated {lrc_filename}")
