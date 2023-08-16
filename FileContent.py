import os
import openpyxl
import requests
from bs4 import BeautifulSoup


excel_file = 'Input.xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active
output_dir = 'Data Extracted'
os.makedirs(output_dir, exist_ok=True)

for row in sheet.iter_rows(min_row=2, values_only=True):
    url_id, url = row

    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')


        title_element = soup.find(class_='entry-title')
        if title_element is None:
            title_element = soup.find(class_='tdb-title-text')
        title = title_element.text if title_element else 'No Title'


        content_elements = soup.find_all('p')
        content = '\n'.join([element.get_text() for element in content_elements])


        lines_to_remove = [
            "Automate the Data Management Process",
            "Realtime Kibana Dashboard for a financial tech firm",
            "Data Management, ETL, and Data Automation",
            "Data Management – EGEAS",
            "How To Secure (SSL) Nginx with Let’s Encrypt on Ubuntu (Cloud VM, GCP, AWS, Azure, Linode) and Add Domain",
            "Deploy and view React app(Nextjs) on cloud VM such as GCP, AWS, Azure, Linode",
            "Deploy Nodejs app on a cloud VM such as GCP, AWS, Azure, Linode",
            "Grafana Dashboard – Oscar Awards",
            "Rise of telemedicine and its Impact on Livelihood by 2040",
            "Rise of e-health and its impact on humans by the year 2030",
            "Rise of telemedicine and its Impact on Livelihood by 2040",
            "Rise of e-health and its impact on humans by the year 2030",
            "AI/ML and Predictive Modeling",
            "Solution for Contact Centre Problems",
            "How to Setup Custom Domain for Google App Engine Application?",
            "Code Review Checklist",
            "Contact us: hello@blackcoffer.com",
            "© All Right Reserved, Blackcoffer(OPC) Pvt. Ltd"
        ]

        for line in lines_to_remove:
            content = content.replace(line, "")


        file_name = f"{url_id}.txt"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\n")
            file.write(f"Content:\n{content}\n")

        print(f"Extracted and saved data for URL_ID {url_id}.")

    else:
        print(f"Failed to fetch URL_ID {url_id}: {response.status_code}")


workbook.close()
