from opengit.main import main


def test_main():
    returncode = main([""])
    assert returncode == 0


def test_error(capsys):
    returncode = main(["/"])

    out, err = capsys.readouterr()
    assert out == "ERROR: No remote url found!\n"
    assert err == ""
    assert returncode != 0
