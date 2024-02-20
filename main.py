from midiutil import MIDIFile
import random

def generate_random_chord_progression(length):
    chords = ["C", "Dm", "Em", "F", "G", "Am", "Bdim"]  # You can modify this list with your preferred chords
    progression = [random.choice(chords) for _ in range(length)]
    return progression

def chord_to_degrees(chord_name):
    # Define the mapping of chord names to pitch classes (degrees)
    chord_mappings = {
        "C": [60, 64, 67],
        "Dm": [62, 65, 69],
        "Em": [64, 67, 71],
        "F": [65, 69, 72],
        "G": [67, 71, 74],
        "Am": [69, 72, 76],
        "Bdim": [71, 74, 77]
    }
    return chord_mappings.get(chord_name, [])

def export_to_midi(chord_progression, output_file="output.mid"):
    track = 0
    channel = 0
    time = 0
    beats_per_bar = 1
    ticks_per_beat = 4  # assuming quarter note resolution
    ticks_per_bar = beats_per_bar * ticks_per_beat
    tempo = 120

    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)

    for chord_name in chord_progression:
        chord_degrees = chord_to_degrees(chord_name)
        for pitch in chord_degrees:
            midi.addNote(track, channel, pitch, time, ticks_per_beat, 64)  # 64 is the velocity, adjust as needed
        time += ticks_per_bar

    with open(output_file, 'wb') as midi_file:
        midi.writeFile(midi_file)

if __name__ == "__main__":
    progression_length = 8  # Number of bars in the progression
    random_chord_progression = generate_random_chord_progression(progression_length)
    
    export_to_midi(random_chord_progression, output_file="random_chord_progression17.mid")
