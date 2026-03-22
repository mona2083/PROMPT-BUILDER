"""
Desktop shell for AI Prompt Builder (Flask + pywebview).

  pip install pywebview
  python desktop_launcher.py

Optional: PyInstaller で exe/app 化する場合はこのファイルをエントリに指定。
"""
from __future__ import annotations

import os
import sys
import threading
import time

# ── Flask アプリをインポート（main の if __name__ は実行されない）────────
from main import app as flask_app

HOST = "127.0.0.1"
PORT = int(os.environ.get("PORT", "5001"))
URL = f"http://{HOST}:{PORT}"


def _run_flask() -> None:
    # use_reloader=False: デスクトップ起動時はリローダーを使わない
    flask_app.run(
        host=HOST,
        port=PORT,
        debug=False,
        use_reloader=False,
        threaded=True,
    )


def main() -> None:
    try:
        import webview
    except ImportError:
        print("pywebview が入っていません: pip install pywebview", file=sys.stderr)
        sys.exit(1)

    t = threading.Thread(target=_run_flask, daemon=True)
    t.start()

    # サーバー起動待ち（簡易）
    deadline = time.time() + 30.0
    while time.time() < deadline:
        try:
            import urllib.request

            urllib.request.urlopen(URL, timeout=0.5)
            break
        except OSError:
            time.sleep(0.1)
    else:
        print("Flask が起動しませんでした。", file=sys.stderr)
        sys.exit(1)

    webview.create_window(
        "AI Prompt Builder",
        URL,
        width=1200,
        height=800,
        min_size=(800, 600),
    )
    webview.start()


if __name__ == "__main__":
    main()
