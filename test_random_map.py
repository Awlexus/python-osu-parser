import os
import beatmapparser
import datetime
from random import shuffle

if __name__ == "__main__":

    osu_songs_directory = os.path.join(os.getenv('LOCALAPPDATA'), 'osu!', 'Songs')
    script_folder = os.getcwd()

    maps = os.listdir(osu_songs_directory)
    shuffle(maps)
    map_path = os.path.join(osu_songs_directory, maps[0])
    files = [x for x in os.listdir(map_path) if x.endswith(".osu")]
    parser = beatmapparser.BeatmapParser()
    osu_path = os.path.join(map_path, files[0])
    print(osu_path)
    time = datetime.datetime.now()
    parser.parseFile(osu_path)

    print("Parsing done. Time: ", (datetime.datetime.now() - time).microseconds / 1000, 'ms')

    time = datetime.datetime.now()
    parser.build_beatmap()

    # Debug at the line below to see the contents of the object
    print("Building done. Time: ", (datetime.datetime.now() - time).microseconds / 1000, 'ms')
    quit()