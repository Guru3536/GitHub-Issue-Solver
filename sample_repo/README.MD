readme = '''
# Sample Flask Login Repository

This repository intentionally contains a bug.

Issue:
Login endpoint crashes when password is empty.

Expected:
Return HTTP 400

Observed:
Returns HTTP 500
'''

with open("sample_repo/README.md", "w") as f:
    f.write(readme)
