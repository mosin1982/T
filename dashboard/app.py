python -m black dashboard/app.py
python -m ruff check dashboard/app.py --fix
python -m pytest -q
git add dashboard/app.py
git commit -m "Add formatted dashboard app"
git push