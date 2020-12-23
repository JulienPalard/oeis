import sys
from pathlib import Path

import pytest

import oeis


def test_main(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["oeis"])
    with pytest.raises(SystemExit):
        oeis.main()
    captured = capsys.readouterr()
    assert "--help" in captured.err


def test_main_unimplemented(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["oeis", "APOUETTE"])
    with pytest.raises(SystemExit):
        oeis.main()
    captured = capsys.readouterr()
    assert "Unimplemented" in captured.err


def test_main_help(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["oeis", "--help"])
    with pytest.raises(SystemExit):
        oeis.main()
    captured = capsys.readouterr()
    assert "usage:" in captured.out


def test_main_list(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["oeis", "--list"])
    oeis.main()
    captured = capsys.readouterr()
    assert "A00" in captured.out


def test_main_random(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["oeis", "--random"])
    oeis.main()
    captured = capsys.readouterr()
    assert "A" in captured.out


def test_main_plot_to_file(monkeypatch, capsys, tmpdir):
    tmpdir = Path(tmpdir)
    pngfile = tmpdir / "test.png"
    monkeypatch.setattr(sys, "argv", ["oeis", "A000290", "--file", str(pngfile)])
    oeis.main()
    assert pngfile.exists()


def test_main_start_out_of_bound_due_to_offset(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["oeis", "A001462", "--start", "0"])
    with pytest.raises(SystemExit):
        oeis.main()
    assert "offset" in capsys.readouterr().err
