## Commit Message Notes

### Commit message standard template:
```
    <type>[optional scope]: <description>
    [optional body]
    [optional footer(s)]
```

### Commit types with their purpose/intent:
- `build`: Changes that affect the build system or external dependencies (e.g., glp, npm, pip, poetry, Dockerfile)
- `chore`: Routine maintenance tasks that do not modify production app code or test suites (e.g., updating dependencies, modifying .gitignore, version bumps)
- `ci`: Changes to continuous integration configuration files and scripts (e.g., GitHub Actions, GitLab CI, CircleCI, Travis)
- `docs`: Documentation-only changes (e.g., modifying README.md, writing docstrings, updating internal wiki pages)
- `feat`: A brand new feature or functional capabilities introduced specifically to the production codebase.
- `fix`: A bug fix or patch resolving an active issue in the production codebase
- `perf`: A production code modification specifically aimed at improving application speed, memory usage, or performance
- `refactor`: Rewriting production code that neither fixes a bug nor adds a feature (e.g., cleaning up logic, renaming variables)
- `revert`: Reverts a previous commit from the repository history back to a stable state
- `style`: Formatting edits that do not alter operational code logic (e.g., fixing white-spaces, missing semicolons, linter warnings)
- `test`: Adding missing test coverage, correcting broken unit tests, or refactoring existing testing suites

### Hierarchy of commit types:
```feat -> fix -> perf -> refactor -> test -> style -> docs -> build -> ci -> revert -> chore```


### The seven rules of a great Git commit message:
1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how

### Common Scopes:
- deps: Modifying third-party packages or lockfiles
- config: Changing environmental setup or settings
- db: Database connections, models, or migrations
- auth: User registration, login, JWT verification, or hashing
- api: Endpoint routing and HTTP handling
- users: Managing user profiles, roles, or database entries

### Examples:
- Example 1:
```git commit -m "chore(deps): install fastapi and backend package ecosystem"```
- Example 2:
```
    feat(auth): implement jwt token generation

    Introduce pyjwt to encode user payloads upon successful login. 
    This replaces the old basic auth stub with a secure, stateless 
    session mechanism. Tokens expire automatically after 15 minutes.
```
- Example 3:
```
    fix(database): resolve connection pool timeout under high load

    Increase pool_size to 20 and max_overflow to 10 in the SQLAlchemy
    engine setup. This prevents application crashes when multiple
    concurrent requests attempt to read user profiles simultaneously.

    Resolves: #142
```
- Example 4:
```
    refactor(users)!: migration to sqlalchemy 2.0 2.0 syntax

    Update all user repository database queries from the legacy 1.x 
    v1 execution syntax over to the modern select() scalars format.

    BREAKING CHANGE: The old database execution helper functions 
    have been completely removed from the utils module.
```
- Example 5:
```
    fix(database): resolve connection pool timeout under high load

    Increase pool_size to 20 and max_overflow to 10 in the SQLAlchemy 
    engine setup. This prevents application crashes when multiple 
    concurrent requests attempt to read user profiles simultaneously.

    Resolves: #142
    Signed-off-by: Developer Name <dev@example.com>
```
