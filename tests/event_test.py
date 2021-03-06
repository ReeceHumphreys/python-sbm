import pytest
import numpy as np
from nasa_sbm.configuration import SatType
from nasa_sbm.satellite import Satellite
from nasa_sbm.event import Explosion, Collision


class TestEvent:

    @pytest.fixture(scope="session")
    def satellites(self):
        class MySatellite(Satellite):

            def __init__(self, mass, characteristic_length, type):
                self._mass = mass
                self._characteristic_length = characteristic_length,
                self._type = type

            @property
            def mass(self):
                return self._mass

            @property
            def characteristic_length(self):
                return self._characteristic_length

            @property
            def type(self):
                return self._type

            @property
            def position(self):
                return np.array([1, 1, 1])

            @property
            def velocity(self):
                return np.array([1, 1, 1])

        sat_1 = MySatellite(500, 0.1, SatType("SC"))
        sat_2 = MySatellite(1000, 0.3, SatType("RB"))
        return np.array([sat_1, sat_2])

    @pytest.mark.parametrize("test_input, expected", [
        (0, ZeroDivisionError),
    ])
    def test_collision_number_fragments_raises(self, satellites, test_input, expected):
        collision_event = Collision()

        with pytest.raises(expected):
            fragment_count = collision_event.fragment_count(satellites, test_input)
            assert fragment_count is expected

    # @pytest.mark.parametrize("test_input, expected", [
    #     (1, 100),
    # ])
    # def test_collision_number_fragments(self, satellites, test_input, expected):
    #     collision_event = Collision()

    #     fragment_count = collision_event.fragment_count(satellites, test_input)

    #     assert fragment_count is expected

    @pytest.mark.parametrize("test_input, expected", [
        (1, 6),
    ])
    def test_explosion_number_fragments(self, satellites, test_input, expected):
        explosion_event = Explosion()

        fragment_count = explosion_event.fragment_count(satellites, test_input)

        assert fragment_count is expected

    @pytest.mark.parametrize("test_input, expected", [
        (0, ZeroDivisionError),
    ])
    def test_explosion_number_fragments_raises(self, satellites, test_input, expected):
        explosion_event = Explosion()

        with pytest.raises(expected):
            fragment_count = explosion_event.fragment_count(satellites, test_input)
            assert fragment_count is expected
