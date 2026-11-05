"""Модуль запуска unit-тестов и формирования отчёта."""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


class TestRunner:
    """Запускает pytest в указанном проекте и генерирует HTML-отчёт."""

    def __init__(self, project_path: str) -> None:
        """Инициализация"""
        self.project_path = Path(project_path)

    def run_tests(self) -> dict:
        """Запускает pytest через subprocess."""
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(self.project_path), "-v"],
            capture_output=True,
            text=True,
            check=False,
        )
        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }

    def generate_report(
            self, results: dict,
            output_path: str = "report.html"
            ) -> str:
        """
        Генерирует HTML-отчёт по результатам тестов.

        :param results: словарь из run_tests()
        :param output_path: куда сохранить HTML
        :return: путь к созданному файлу
        """
        status = "PASSED" if results["returncode"] == 0 else "FAILED"
        color = "green" if results["returncode"] == 0 else "red"
        html = f"""<!DOCTYPE html>
<html lang="ru">
<head><meta charset="utf-8"><title>Test Report</title></head>
<body>
  <h1>Отчёт о тестировании</h1>
  <p><b>Время:</b> {results['timestamp']}</p>
  <p><b>Статус:</b> <span style="color:{color}">{status}</span></p>
  <h2>Вывод pytest</h2>
  <pre>{results['stdout']}</pre>
  <h2>Ошибки (stderr)</h2>
  <pre>{results['stderr']}</pre>
</body>
</html>"""
        Path(output_path).write_text(html, encoding="utf-8")
        return output_path


if __name__ == "__main__":
    runner = TestRunner("tests")
    res = runner.run_tests()
    PATH = runner.generate_report(res)
    print(f"Отчёт сохранён: {PATH}")
