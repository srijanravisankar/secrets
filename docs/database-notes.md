```
────────────────────────────────────────────────────────┐
│                      SQLAlchemy                        │
│   (Manages DML: Data Manipulation Language)            │
│   - SELECT, INSERT, UPDATE, DELETE                     │
│   - Queries rows, updates user details, saves records  │
└──────────────────────────┬─────────────────────────────┘
                           │ Utilizes Models to Define Schema
                           ▼
┌────────────────────────────────────────────────────────┐
│                        Alembic                         │
│   (Manages DDL: Data Definition Language)              │
│   - CREATE TABLE, ALTER COLUMN, DROP TABLE             │
│   - Modifies the structural "blueprint" of database    │
└────────────────────────────────────────────────────────┘
```