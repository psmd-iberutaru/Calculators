# We first install or update the needed dependencies.
pip install -r requirements.txt --upgrade


# Then we execute all of the checks.
black . --preview --enable-unstable-feature=string_processing
black .

ruff check . --fix