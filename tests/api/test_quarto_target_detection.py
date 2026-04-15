"""Tests for Quarto target detection and auto-display mimebundle output."""

import json

import pandas as pd

import maketables as mt
import maketables.mtable as mtable_module


def _write_execute_info(tmp_path, target_format: str, base_format: str | None = None):
    info_path = tmp_path / "quarto-execute-info.json"
    payload = {
        "document-path": "doc.qmd",
        "format": {
            "identifier": {
                "target-format": target_format,
                "base-format": base_format or target_format,
            }
        },
    }
    info_path.write_text(json.dumps(payload), encoding="utf-8")
    return info_path


def test_quarto_target_detects_typst(monkeypatch, tmp_path):
    """Read Quarto target format from QUARTO_EXECUTE_INFO."""
    execute_info_path = _write_execute_info(tmp_path, "typst")
    monkeypatch.setenv("QUARTO_EXECUTE_INFO", str(execute_info_path))

    table = mt.MTable(pd.DataFrame({"A": [1]}, index=["row1"]))

    assert table._quarto_target_format() == "typst"
    assert table._is_quarto_typst_target() is True


def test_make_none_uses_typst_markdown_bundle_in_quarto_typst(monkeypatch, tmp_path):
    """When Quarto target is Typst, auto-display should emit raw Typst markdown."""
    execute_info_path = _write_execute_info(tmp_path, "typst")
    monkeypatch.setenv("QUARTO_EXECUTE_INFO", str(execute_info_path))

    captured = []

    def _capture_display(obj):
        captured.append(obj)

    monkeypatch.setattr(mtable_module, "display", _capture_display)

    table = mt.MTable(pd.DataFrame({"A": [1]}, index=["row1"]))
    result = table.make(type=None)

    assert result is None
    assert len(captured) == 1
    bundle = captured[0]._repr_mimebundle_()
    assert "text/markdown" in bundle
    assert "```{=typst}" in bundle["text/markdown"]
    assert "#table(" in bundle["text/markdown"]
    assert "text/latex" not in bundle


def test_make_none_uses_latex_bundle_when_not_typst(monkeypatch, tmp_path):
    """When Quarto target is not Typst, auto-display should keep LaTeX output."""
    execute_info_path = _write_execute_info(tmp_path, "pdf", base_format="latex")
    monkeypatch.setenv("QUARTO_EXECUTE_INFO", str(execute_info_path))

    captured = []

    def _capture_display(obj):
        captured.append(obj)

    monkeypatch.setattr(mtable_module, "display", _capture_display)

    table = mt.MTable(pd.DataFrame({"A": [1]}, index=["row1"]))
    result = table.make(type=None)

    assert result is None
    assert len(captured) == 1
    bundle = captured[0]._repr_mimebundle_()
    assert "text/latex" in bundle
    assert "text/markdown" not in bundle
