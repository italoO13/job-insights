from src.pre_built.counter import count_ocurrences


def test_counter():
    count_min = count_ocurrences("data/jobs.csv", "python")
    count_masc = count_ocurrences("data/jobs.csv", "PYTHON")
    assert count_min == 1639
    assert count_masc == 1639
