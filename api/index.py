"""Vercel serverless 入口: 把 Flask app 暴露给 Vercel 的 Python 运行时。"""
import sys
from pathlib import Path

# 把项目根加入 sys.path，确保能 import app
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app  # noqa: E402
