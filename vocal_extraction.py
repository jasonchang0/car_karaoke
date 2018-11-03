'''
from pydub import AudioSegment
from pydub.playback import play

# read in audio file and get the two mono tracks
sound_stereo = AudioSegment.from_file('audioFile.mp3', format="mp3")
sound_monoL = sound_stereo.split_to_mono()[0]
sound_monoR = sound_stereo.split_to_mono()[1]

# Invert phase of the Right audio file
sound_monoR_inv = sound_monoR.invert_phase()

# Merge two L and R_inv files, this cancels out the centers
sound_instrumentals = sound_monoL.overlay(sound_monoR_inv)

# Export merged audio file
fh = sound_instrumentals.export('audioFile_CentersOut.mp3', format="mp3")
'''

from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize

# read in audio file and get the two mono tracks
sound_stereo = AudioSegment.from_file('audioFile.mp3', format="mp3")
sound_monoL = sound_stereo.split_to_mono()[0]
sound_monoR = sound_stereo.split_to_mono()[1]

sound_monoL.export('audioFile_monoL.mp3', format="mp3")
sound_monoR.export('audioFile_monoR.mp3', format="mp3")

# Invert phase of the Right audio file
sound_monoR_inv = sound_monoR.invert_phase()

# Merge two L and R_inv files, this cancels out the centers
# sound_instrumentals = sound_monoL.overlay(sound_monoR_inv)

# sound_instrumentals = sound_monoL.fade(from_gain=+0.3, start=0, end=sound_monoL.duration_seconds).overlay(
#     sound_monoR.fade(from_gain=+0.7, start=0, end=sound_monoR.duration_seconds))

sound_instrumentals = sound_monoL.overlay(sound_monoR_inv)

# sound_instrumentals = sound_instrumentals + 10
sound_instrumentals = sound_instrumentals.apply_gain(+sound_instrumentals.max_dBFS * 1000)

sound_instrumentals.export('sound_instrumentals.mp3', format='mp3')

# sound_instrumentals = (sound_monoL - sound_monoL.max_possible_amplitude * 0.7).overlay(
#     sound_monoR - sound_monoR.max_possible_amplitude * 0.3)

sound_instrumentals_inv = sound_instrumentals.invert_phase()

sound_vocal = sound_stereo.overlay(sound_instrumentals_inv.apply_gain(-100000))
sound_vocal.export('sound_vocal.mp3', format='mp3')

sound_vocalL = sound_vocal.split_to_mono()[0]
sound_vocalL.export('sound_vocalL.mp3', format='mp3')

sound_vocalR = sound_vocal.split_to_mono()[1]
sound_vocalR.export('sound_vocalR.mp3', format='mp3')

'''
for _ in range(2):
    sound_vocalL = normalize(sound_vocalL.apply_gain(-sound_vocalL.dBFS * 0.7))
    # sound_vocalL = normalize(sound_vocalL)

    sound_vocalR = normalize(sound_vocalR.apply_gain(-sound_vocalL.dBFS * 0.3))
    # sound_vocalR = normalize(sound_vocalR)

    sound_vocal = sound_vocalL.overlay(sound_vocalR)
    # sound_vocal = AudioSegment.from_mono_audiosegments(sound_vocalL, sound_vocalR)

    # Export merged audio file
    sound_vocal.export('audioFile_CentersOut_' + str(_) + '.mp3', format="mp3")

    sound_vocalL, sound_vocalR = sound_vocalR, sound_vocalL
'''
