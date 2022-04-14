import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    
    writer.writerow(['title', 'company', 'location', 'link'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

# save_to_file({'title':1, 'company':2, 'location':3, 'link':4})