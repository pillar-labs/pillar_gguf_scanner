# tests/smoke_test.py
import pillar_gguf_scanner


def test_import():
    assert hasattr(pillar_gguf_scanner, "__version__")
    assert hasattr(pillar_gguf_scanner, "__doc__")


def test_cli_entry_point():
    from pillar_gguf_scanner.cli import main

    assert callable(main)
