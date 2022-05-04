""" https://leetcode.com/problems/design-underground-system/ """

from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.delta = defaultdict(int)
        self.counts = defaultdict(int)
        self.check_in = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_check_in, check_in_time = self.check_in.pop(id)
        key = station_check_in + "_" + stationName
        self.counts[key] += 1
        self.delta[key] += t - check_in_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "_" + endStation
        return self.delta[key] / self.counts[key]
