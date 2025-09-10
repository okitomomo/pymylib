from mylib import LogType, log

def test_log(capsys):
    log(LogType.I, "testi")
    log(LogType.W, "testw")
    log(LogType.E, "teste")
    log(LogType.D, "testd")
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert "[INFO ]testi" in lines[0]
    assert "[WARN ]testw" in lines[1]
    assert "[ERROR]teste" in lines[2]
    assert "[DEBUG]testd" in lines[3]


