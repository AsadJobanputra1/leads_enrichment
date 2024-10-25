# Educause Leads Enrichment Service

## Project Description

The Educause Leads Enrichment Service is a command-line utility designed to process CSV files of contacts from tradeshows. It enriches the contact data with additional qualification information from OpenAI, such as the size of the organization and recent AI activities.

## Features

- Processes CSV files to extract and enrich contact data.
- Integrates with OpenAI to provide additional insights.
- Outputs enriched data to a new CSV file.
- User-friendly command-line interface.

## Prerequisites

- Python 3.x
- OpenAI API key stored in an environment variable `OPENAI_API_KEY`.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your OpenAI API key is set in the environment:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

2. Run the program:
   ```bash
   python src/main.py
   ```

3. Follow the on-screen menu to process CSV files.

## File Structure

- `/docs`: Documentation files
- `/src`: Source code files
- `/test`: Test files
- `/conf`: Configuration files
- `/data`: Data files

## Deployment

- Ensure all dependencies are installed and the environment is configured.
- Monitor performance and handle any issues that arise during operation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
