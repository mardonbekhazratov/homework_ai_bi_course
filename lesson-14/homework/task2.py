import time
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

def main():
    current_dir = Path(__file__).resolve().parent

    url = "https://realpython.github.io/fake-jobs"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    f = time.time()
    # print(f)
    job_count = 0
    for job in soup.find_all("div",class_="card-content"):
        job_count += 1
        if job_count > 5:
            break
        apply_url = job.find_all("a",class_="card-footer-item")[1]["href"]
        # print(apply_url)
        job = BeautifulSoup(requests.get(apply_url).text, "html.parser")
        # print(job)

        job_title = job.find("h1", class_="title is-2").text.strip()
        # print(job_title)
        job_company = job.find("h2",class_="company").text.strip()
        # print(job_company)
        job_location = job.find("p", id="location").text.strip()[10:]
        # print(job_location)
        job_description = job.find("div",class_="content").find("p").text.strip()
        # print(job_description)
        job_application_link = apply_url
        jobs.append((job_title,job_company,job_location,job_description,job_application_link))
    # print(jobs)

    con = sqlite3.connect(current_dir / "jobs.db")
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Jobs 
                (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                   Title TEXT NOT NULL, 
                   Company TEXT NOT NULL, 
                   Location TEXT NOT NULL, 
                   Description TEXT,
                   Apply TEXT,
                   UNIQUE(Title, Company, Location)
                )
                """)

    for job_title, company_name, location, description, application_link in jobs:
        cursor.execute("""
        SELECT Description, Apply FROM Jobs 
        WHERE Title = ? AND Company = ? AND Location = ?
        """, (job_title, company_name, location))
        result = cursor.fetchone()
        
        if result:
            if result[0] != description or result[1] != application_link:
                cursor.execute("""
                UPDATE jobs 
                SET Description = ?, Apply = ? 
                WHERE Title = ? AND Company = ? AND Location = ?
                """, (description, application_link, job_title, company_name, location))
                print(f"Updated job: {job_title} at {company_name}")
        else:
            cursor.execute("""
            INSERT INTO Jobs (Title, Company, Location, Description, Apply)
            VALUES (?, ?, ?, ?, ?)
            """, (job_title, company_name, location, description, application_link))
            print(f"Added job: {job_title} at {company_name}")
    # print(cursor.execute("SELECT * FROM Jobs WHERE ID = 1").fetchall())
    
    query = "SELECT Title, Company, Location, Description, Apply FROM jobs WHERE Location = ? AND Company = ?"
    
    location = input("Enter name of location where you want to work:\n")
    company_name = input("Enter company name:\n")
    cursor.execute(query, [location, company_name])
    results = cursor.fetchall()

    # Write to CSV
    with open(current_dir / "jobs.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Job Title", "Company Name", "Location", "Description", "Application Link"])
        writer.writerows(results)
    print(f"Filtered results exported to jobs.csv")

    con.commit()
    con.close()

    # print(f"{time.time()-f:.6f}")

if __name__=="__main__":
    main()