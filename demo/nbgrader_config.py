import os
from pathlib import Path

gradebook = "gradebook.db"

root_dir = Path()

assign_db = (root_dir / gradebook).resolve()

db_url = f"sqlite:///{str(assign_db)}"
exchange_dir = root_dir / Path("exchange")

print(f"assignment db is {assign_db}")

c = get_config()  # noqa

c.CourseDirectory.db_url = db_url
c.CourseDirectory.root = str(root_dir)
print(f"setting root to {c.CourseDirectory.root}")
c.ExecutePreprocessor.timeout = 300

c.CourseDirectory.course_id = "EOSC001"
c.Exchange.root = str(root_dir)
print(f"in nbgrader_config.py: setting exchange to {c.Exchange.root}")

# Apply this regular expression to the extracted file filename (absolute path)
c.FileNameCollectorPlugin.named_regexp = (
    r".*_(?P<student_id>\w+)_attempt_" "(?P<file_id>.*)"
)
