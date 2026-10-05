def read_jobs():
    with open("jobs.txt", "r") as file:
        for line in file:
            yield line.strip()


def process(job):
    print(f"Processing: {job}")


for job in read_jobs():
    process(job)