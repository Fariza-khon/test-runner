"""Unit-тесты для модуля TestRunner."""

from src.test_runner import TestRunner


def test_run_tests_returns_dict(tmp_path):
    """Проверяем, что run_tests возвращает словарь с нужными ключами."""
    runner = TestRunner(str(tmp_path))
    result = runner.run_tests()
    assert isinstance(result, dict)
    assert "returncode" in result
    assert "stdout" in result
    assert "stderr" in result
    assert "timestamp" in result


def test_generate_report_creates_file(tmp_path):
    """Проверяем, что generate_report создаёт HTML-файл."""
    runner = TestRunner(str(tmp_path))
    fake_results = {
        "returncode": 0,
        "stdout": "1 passed",
        "stderr": "",
        "timestamp": "2024-01-01T00:00:00",
    }
    report_path = tmp_path / "report.html"
    result_path = runner.generate_report(fake_results, str(report_path))
    assert result_path == str(report_path)
    assert report_path.exists()
    content = report_path.read_text(encoding="utf-8")
    assert "PASSED" in content
    assert "1 passed" in content
