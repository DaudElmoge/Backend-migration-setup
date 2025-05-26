#setup

- install the necessary packages with - pipenv install "fastapi[standard]" sqlalchemy alembic

#Migrations -> version control for databases

-To setup migration ,run pipenv shell then run `alembic init migrations` -> run this only once
-Edit alembic.ini and set this line to `sqlalchemy.url = sqlite:///e-commerce.db`
- Edit `env.py`in the migrations folder and import Base class from the models file and update the `target_metadata` see line (19 and 20)
-To create a migration, run `alembic revision --autogenerate -m "message"` (just similar with git commit)
-To apply the generated migration, run `alembic upgrade head` (similar to git push)