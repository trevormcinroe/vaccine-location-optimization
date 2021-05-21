import googlemaps
import configparser


class GMapsWrapper:
    def __init__(self, key_ini_file):

        self.key = None
        self._read_ini(key_ini_file)
        self.client = googlemaps.Client(key=self.key)

        self.distances = dict()

    def _read_ini(self, file):
        config = configparser.ConfigParser()
        config.read(file)
        key = config['KEY']
        self.key = key['KEY']

    def get_distances(self, origins, destinations):
        """

        Args:
            origins (list): list of origin addresses
            destinations (list): list of destination addresses

        Returns:
            self.distances = {origin_0: {destination_0: int, destination_1: int...}, ...}
        """

        for o in origins:
            self.distances[o] = dict()

            for d in destinations:
                dist = self.get_distance(o, d)
                self.distances[o][d] = dist

    def get_distance(self, origin, destination, km=True):
        """Returns distance from origin to destination in KMs"""
        distance = self.client.distance_matrix(origin, destination, mode='driving')

        if km:
            return distance['rows'][0]['elements'][0]['distance']['value'] / 1000
        else:
            return distance['rows'][0]['elements'][0]['distance']['value']
