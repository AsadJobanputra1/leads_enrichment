import os
import csv
import openai
import logging
from datetime import datetime
from pydantic import BaseModel, ConfigDict


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting main function.")
    check_and_create_directories()
    logging.info("Finished setting up directories.")
    display_menu()

def check_and_create_directories():
    logging.info("Checking and creating directories if they do not exist.")
    if not os.path.exists('conf'):
        os.makedirs('conf')
        create_default_config_files()
    if not os.path.exists('data'):
        os.makedirs('data')

def create_default_config_files():
    logging.info("Creating default configuration files if they don't exist.")
    accounts_file = 'conf/accounts.csv'
    categories_file = 'conf/categories.csv'
    if not os.path.exists(accounts_file):
        with open(accounts_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['account number', 'friendly name', 'process data'])
    if not os.path.exists(categories_file):
        with open(categories_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['search text', 'category name'])

def display_menu():
    logging.info("Displaying menu options.")
    print("1. Process CSV File")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        process_csv_file()
    else:
        exit_program()

def process_csv_file():
    logging.info("Starting CSV file processing.")
    input_file = input("Enter the input CSV file path: ")
    output_file = input("Enter the output CSV file path (optional): ") or 'output.csv'
    if not is_valid_csv(input_file):
        print("Error: Invalid CSV file.")
        return
    data_list = load_csv_to_list(input_file)
    enriched_data = enrich_data_with_openai(data_list)
    save_to_csv(enriched_data, output_file)

def is_valid_csv(file_path):
    valid = file_path.endswith('.csv') and os.path.exists(file_path)
    logging.info(f"CSV file validation result for {file_path}: {valid}")
    return valid

def load_csv_to_list(file_path):
    logging.info(f"Loading CSV file into list: {file_path}")
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def enrich_data_with_openai(data_list):
    logging.info("Starting data enrichment with OpenAI.")
    openai.api_key = os.getenv('OPENAI_API_KEY')
    enriched_data = []
    for row in data_list:
        response = query_openai(row['Company'])
        enriched_row = create_enriched_row(row, response)
        enriched_data.append(enriched_row)
    return enriched_data


class enrichedData(BaseModel):
        description: str
        NumStudents: str
        Recent_AI_work: str
        AI_link_1: str
        AI_link_2: str
        AI_link_3: str

def query_openai(company):
    logging.info(f"Querying OpenAI for company: {company}")
    prompt = f"Act as an online researcher for the given {company} field: how many students attend the university, what recent work have they done in AI, provide three links to AI work that {company} has done recently. Provide output in structured JSON format."
    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

 # Start the chat with the initial prompt
    response = openai.ChatCompletion.create(
        model=os.getenv('OPENAI_MODEL', 'gpt-4o-2024-08-06'),  # Default to 'gpt-4o-2024-08-06' if not set
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    logging.info(f"Querying OpenAI for company: {response.choices[0].message['content']}")
    return response.choices[0].message['content']

def create_enriched_row(row, response):
    logging.info("Creating enriched row from OpenAI {response}.")
    # This is a placeholder for parsing logic
    return {
        'ID': row.get('ID', ''),
        'firstname': row.get('FirstName', ''),
        'lastname': row.get('LastName', ''),
        'Title': row.get('Title', ''),
        'Company': row.get('Company', ''),
        'description': response.description,
        'Number of Students': response.NumStudents,  # Extract from response
        'Recent AI work': response.Recent_AI_work,      # Extract from response
        'AI link 1': response.AI_link_1,           # Extract from response
        'AI link 2': response.AI_link_2,           # Extract from response
        'AI link 3': response.AI_link_3            # Extract from response
    }

def save_to_csv(data, filename):
    logging.info(f"Saving enriched data to CSV file: {filename}")
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['ID', 'firstname', 'lastname', 'Title', 'Company', 'Number of Students', 'Recent AI work', 'AI link 1', 'AI link 2', 'AI link 3']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def exit_program():
    logging.info("Exiting the program.")
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main()
