import Piskvorky_AI
import pytest

def test_tah_ai():
    vracena_hodnota_1 = Piskvorky_AI.tah_ai("-" * 10, "x", "o")
    assert vracena_hodnota_1 == 2 or vracena_hodnota_1 == 6

    vracena_hodnota_2 = Piskvorky_AI.tah_ai("--x-x-------", "o", "x" )
    assert vracena_hodnota_2 == 3

    vracena_hodnota_3 = Piskvorky_AI.tah_ai("---x-x---", "o", "x" )
    assert vracena_hodnota_3 == 4

    vracena_hodnota_4 = Piskvorky_AI.tah_ai("---i-i---", "i", "g")
    assert vracena_hodnota_4 == 4

    with pytest.raises(ValueError):
        Piskvorky_AI.tah_ai("----", "x", "o")
