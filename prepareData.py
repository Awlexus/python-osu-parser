import os
import sys
from random import shuffle
import beatmapparser

osu_folder = 'C:\\Users\\Alex Wieser\\AppData\\Local\\osu!\\Songs'
script_folder = os.getcwd()
training_data_folder = os.path.join(script_folder, "training_data")
test_data_folder = os.path.join(script_folder, "test_data")


def prepare_data(mappath: str, outputpath: str):
    # Get .osu files
    files = [x for x in os.listdir(mappath) if x.endswith(".osu")]
    beatmapparser.parseFile(os.path.join(mappath, files[0]))
    #
    # for file in files:
    #     with open(os.path.join(mappath, file), 'r') as map:
    #         while True:
    #             if map.readline() != "[HitObjects]":
    #                 break
    #
    #         # hitobject data
    #         data = []
    #         # read until hitobject data is reached
    #         while True:
    #             line = map.readline()
    #             if not line:
    #                 break
    #             data.append(line[:line.rfind(',')].split(','))
    #
    #         # write inputdata
    #         with open(os.path.join(outputpath, file.replace('.osu', '.in'))) as input:
    #             for objects in data:
    #                 for object in objects:
    #                     input.write('%u,%u' % (object[2], object[3]))
    #                     if type & 1:
    #                         input.write(';')
    #                     elif type & 2:
    #                         input.write('%s;' % object[5][:object[5].find('|')])
    #                     elif type & 8:
    #                         input.write()
    #
    #
    #
    #         # write outputdata
    #         with open(os.path.join(outputpath, file.replace('.osu', '.out'))) as output:
    #             break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        datacount = sys.argv[1]
    else:
        datacount = 1

    # Create folders for training/test data
    # if os.path.join(script_folder, )

    maps = os.listdir(osu_folder)
    shuffle(maps)
    prepare_data(os.path.join(osu_folder, maps[1]), test_data_folder)

    # training_data = maps[datacount / 10 * 9:]
    # test_data = maps[:datacount / 10 * 9]
