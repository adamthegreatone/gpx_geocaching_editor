import re
import math
import itertools

input_coordinates = input('zadej souradnice ve formatu NXX XX.XXX EYY YY.YYY: ')
input_distance = float(input('zadej vzdalenost v km: '))/71.6

extracted_coordinates = re.findall(r"[-+]?\d*\.\d+|\d+", input_coordinates)

n1 = float(extracted_coordinates[0])
n2 = float(extracted_coordinates[1])
w1 = float(extracted_coordinates[2])
w2 = float(extracted_coordinates[3])

input_n = n1 + (0.1/6)*n2
input_w = w1 + (0.1/6)*w2

with open ('D:\\dropbox\\gpx\\0_all_finar.gpx', 'r', encoding="utf8") as rf:
    with open ('D:\\dropbox\\gpx\\0_exported.gpx', 'w', encoding="utf8") as wf:

        for line in itertools.islice(rf, 0, 7):

            wf.write(line)

        wf.write('\n')

        for line in rf:

            if line.find("<wpt") == 0:

                coordinates = re.findall(r"[-+]?\d*\.\d+|\d+", line)

                wpt_n = float(coordinates[0])
                wpt_w = float(coordinates[1])

                distance = math.sqrt((input_n - wpt_n)**2 + (input_w - wpt_w)**2)

                if distance < input_distance:

                    wf.write(line)

                    for line in rf:

                        while line.find("</wpt>") != 0:
                            wf.write(line)
                            break                         #this break brings me to line 42

                        else:
                            wf.write(line)
                            break                         #this break brings me to line 27 ???

        wf.write('</gpx>')
