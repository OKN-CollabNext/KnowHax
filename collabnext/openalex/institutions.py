from pyalex import Institution, Institutions


def get_institutions() -> list[Institution]:
    # Get 3 random institutions for now
    return [Institutions().random() for _ in range(5)]
