# AI: SQL to ORM Refactoring and Security Analysis

## Objective
Use an AI assistant to refactor a raw-SQL Python script (mysql.connector)
into a SQLAlchemy ORM version, then analyze its security and
maintainability benefits.

## Files
- `initial_script.py`: original procedural script using parameterized raw SQL
- `refactored_orm.py`: SQLAlchemy 2.0 ORM version (declarative `User` model,
  Session-based CRUD, env-based credentials)

## Process
1. Wrote a single prompt specifying the model, create/add/query demo,
   and a security/professionalism explanation.
2. Ran it in [AI ASSISTANT NAME] and reviewed the output.
3. Verified and adjusted the code before saving it here.

## Key takeaways
- The ORM binds parameters automatically, which removes the main SQL injection risk.
- Table structure lives in one class, so schema changes happen in one place.
- Sessions give transaction handling (commit/rollback) a consistent shape.

## Run
    pip install sqlalchemy mysql-connector-python
    export DB_USER=root DB_PASSWORD=... DB_HOST=localhost DB_NAME=example_db
    python3 refactored_orm.py
