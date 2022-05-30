import os
from pathlib import Path

c = get_config()  # noqa
root_dir = Path().resolve()
assign_db = (root_dir / "gradebook.db").resolve()
db_url = f"sqlite:///{str(assign_db)}"
c.CourseDirectory.db_url = db_url
c.CourseDirectory.root = str(root_dir)
c.ExecutePreprocessor.timeout = 300
c.CourseDirectory.course_id = "ExampleCourse"

