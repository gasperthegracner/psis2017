#!/usr/bin/python3.5

"""
Command line utility to extract basic statistics from a gpx file
"""

import pdb

import sys as mod_sys
import logging as mod_logging
import math as mod_math

import gpxpy as mod_gpxpy

#hack for heart rate
import xml.etree.ElementTree as ET

#heart rate statistics
import numpy as np

import os
import sys


#mod_logging.basicConfig(level=mod_logging.DEBUG,
#                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

header = 'id, duration, avgHeartRate, maxHeartRate, dateOfTraining, elevation, uphill, downhill, length_2d, length_3d, moving_time, stopped_time'



def format_time(time_s):
    if not time_s:
        return 'n/a'
    minutes = mod_math.floor(time_s / 60.)
    hours = mod_math.floor(minutes / 60.)

    return '%s:%s:%s' % (str(int(hours)).zfill(2), str(int(minutes % 60)).zfill(2), str(int(time_s % 60)).zfill(2))


def print_gpx_part_info(gpx_part, csvFile, heartRate, athleteId):
    #multivariable returns
    start_time, end_time = gpx_part.get_time_bounds()
    moving_time, stopped_time, moving_distance, stopped_distance, max_speed = gpx_part.get_moving_data()
    uphill, downhill = gpx_part.get_uphill_downhill()

    duration = gpx_part.get_duration()
    avgHeartRate = round(np.mean(heartRate), 2)
    maxHeartRate = np.max(heartRate)
    dateOfTraining = start_time
    elevation = round(uphill + downhill, 2)
    uphill = round(uphill, 2)
    downhill = round(downhill, 2)
    length_2d = round(gpx_part.length_2d(), 2)
    length_3d = round(gpx_part.length_3d(), 2)

    #id is written seperately
    data = [
        duration,
        avgHeartRate,
        maxHeartRate,
        dateOfTraining,
        elevation,
        uphill,
        downhill,
        length_2d,
        length_3d,
        moving_time,
        stopped_time
    ]

    csvFile.write('\n' + athleteId)
    for d in data:
        csvFile.write(", " + str(d))


def print_gpx_info(gpx, gpx_file, csvFile):
    print('File: %s' % gpx_file)

    if gpx.name:
        print('  GPX name: %s' % gpx.name)
    if gpx.description:
        print('  GPX description: %s' % gpx.description)
    if gpx.author_name:
        print('  Author: %s' % gpx.author_name)
    if gpx.author_email:
        print('  Email: %s' % gpx.author_email)

    print_gpx_part_info(gpx, csvFile)

    '''for track_no, track in enumerate(gpx.tracks):
        for segment_no, segment in enumerate(track.segments):
            print('    Track #%s, Segment #%s' % (track_no, segment_no))
            print_gpx_part_info(segment, indentation='        ')'''


def parseHeartRate(file):
    hrs = []
    tree = ET.parse(file)
    root = tree.getroot()
    for hr in root.iter('{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}hr'):
        hrs.append(int(hr.text))
    return hrs


def run(gpx_files, csvFilePath, athleteId):
    if not gpx_files:
        print('No GPX files given')
        mod_sys.exit(1)

    csvFile = open(csvFilePath, "w")
    csvFile.write(header)

    i = 0
    fLen = str(len(gpx_files))
    for gpx_file in gpx_files:
        sys.stdout.write("\rProgressing file " + str(i) + " out of " + fLen + "       ")
        #sys.stdout.write("\rDoing thing %i % i" % i, fLen)
        sys.stdout.flush()
        i += 1
        try:
            heartRate = parseHeartRate(gpx_file)
            if not heartRate:
                continue
            gpx = mod_gpxpy.parse(open(gpx_file))
            print_gpx_part_info(gpx, csvFile, heartRate, athleteId)
        except Exception as e:
            mod_logging.exception(e)
            print('Error processing %s' % gpx_file)
            mod_sys.exit(1)


def parserMain(directoryPath, outDirectoryPath):
    for dir in os.listdir(directoryPath):
        filePaths = os.listdir(directoryPath + dir)
        for i in range(0, len(filePaths)):
            filePaths[i] = directoryPath + dir + '/' + filePaths[i]
        run(filePaths, outDirectoryPath + dir + ".csv", dir)


def joinFiles(dirPath, outFilePath):
    outFile = open(outFilePath, "w")
    outFile.write(header + '\n')

    for fileName in os.listdir(dirPath):
        with open(dirPath + fileName) as f:
            f.readline() #throw away first line
            content = f.readline()
            while content != "":
                outFile.write(content)
                content = f.readline()


parserMain("../Data/Sport/", "../Data/Parsed/")
joinFiles('../Data/Parsed/', '../Data/summed.csv')