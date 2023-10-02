from src.data_capture import DataCapture

def test_data_capture():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    assert stats.less(4) == 2, "Expected 2"
    assert stats.between(3, 6) == 4, "Expected 4"
    assert stats.greater(4) == 2, "Expected 2"
