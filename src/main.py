import os
import csv
import openai
from datetime import datetime

def main():
    check_and_create_directories()
    display_menu()

def check_and_create_directories():
    if not os.path.exists('conf'):
        os.makedirs('conf')
        create_default_config_files()
    if not os.path.exists('data'):
        os.makedirs('data')

def create_default_config_files():
    # Create default configuration files if they don't exist
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
    print("1. Process CSV File")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        process_csv_file()
    else:
        exit_program()

def process_csv_file():
    input_file = input("Enter the input CSV file path: ")
    output_file = input("Enter the output CSV file path (optional): ") or 'output.csv'
    if not is_valid_csv(input_file):
        print("Error: Invalid CSV file.")
        return
    data_list = load_csv_to_list(input_file)
    enriched_data = enrich_data_with_openai(data_list)
    save_to_csv(enriched_data, output_file)

def is_valid_csv(file_path):
    return file_path.endswith('.csv') and os.path.exists(file_path)

def load_csv_to_list(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def enrich_data_with_openai(data_list):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    enriched_data = []
    for row in data_list:
        response = query_openai(row['Company'])
        enriched_row = create_enriched_row(row, response)
        enriched_data.append(enriched_row)
    return enriched_data

def query_openai(company):
    prompt = f"Act as an online researcher for the given {company} field: how many students attend the university, what recent work have they done in AI, provide three links to AI work that {company} has done recently. Provide output in structured JSON format."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def create_enriched_row(row, response):
    # Parse the OpenAI response and combine it with the original row
    # This is a placeholder for parsing logic
    return {
        'ID': row.get('ID', ''),
        'firstname': row.get('FirstName', ''),
        'lastname': row.get('LastName', ''),
        'Title': row.get('Title', ''),
        'Company': row.get('Company', ''),
        'Number of Students': 'N/A',  # Extract from response
        'Recent AI work': 'N/A',      # Extract from response
        'AI link 1': 'N/A',           # Extract from response
        'AI link 2': 'N/A',           # Extract from response
        'AI link 3': 'N/A'            # Extract from response
    }

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['ID', 'firstname', 'lastname', 'Title', 'Company', 'Number of Students', 'Recent AI work', 'AI link 1', 'AI link 2', 'AI link 3']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def exit_program():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main()
