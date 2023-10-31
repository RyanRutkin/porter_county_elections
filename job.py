from datetime import datetime

with open('file.txt', 'w') as f:
    f.write(f"JOB DONE {datetime.now()}")