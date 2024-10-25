# Specification for Educause Leads Enrichment Service

## Project Overview

**Project Name**: Educause Leads Enrichment Service

**Project Goal**: To provide a utility that quickly processes a CSV file of contacts from a tradeshow and provides additional qualification information from OpenAI about the size of the organization and recent AI activities.

**Target Audience**: Technical users who can export files, run a CLI utility, and execute commands.

## Functional Requirements

1. Upload and process CSV files exported from Educause.
2. Provide an example script that calls the function using `./leadslist.csv` as input parameters, and outputs to the `/data` folder.

## Non-Functional Requirements

- **Cross-Platform CLI**: The program must run from the command line on Mac or Windows.
- **User-Friendly Interface**: The CLI must be easy to use, including a menu of commands and help.
- **No External Database**: The system can save data to the local file system but should not depend on a separate database runtime.
- **Documentation**: Provide a `readme.md` that describes the project, how it works, and key files.

## User Scenarios and User Flows

### Scenario 1: CSV Processing

1. User types in `/input [datafile.csv] /output [output.csv]` in the command line or via menu. Note: `/output` is optional and defaults to `output.csv` if not provided.
2. System opens the file.
   - If the filename can't be found, or if it is not a text-based CSV file, the system returns an error.
3. System filters `datafile.csv` and loads it into a list.
4. System creates an OpenAI session using the OpenAI SDK.
5. For each row in the CSV, the system queries OpenAI SDK with:
   - "Act as an online researcher for the given {company} field: how many students attend the university, what recent work have they done in AI, provide three links to AI work that {company} has done recently. Provide output in structured JSON format."
6. System creates `output.csv` with the following fields:
   - **ID** - from source [datafile.csv]
   - **firstname** - from source [datafile.csv]
   - **lastname** - from source [datafile.csv]
   - **Title** - from source [datafile.csv]
   - **Company** - from source [datafile.csv]
   - **Number of Students** - from OpenAI response
   - **Recent AI work** - from OpenAI response
   - **AI link 1** - from OpenAI response
   - **AI link 2** - from OpenAI response
   - **AI link 3** - from OpenAI response
7. Save the data in a new datafile in `/data/enriched{current datetime 'YYYYMMDD-HHMM'}.csv`.

### Scenario 2: Startup

1. System checks for the `/conf` folder:
   - If it doesn't exist, the system creates it with default configuration data.
2. System checks for the `/data` folder:
   - If it doesn't exist, the system creates the `/data` folder.
3. Creates default config files if they don't exist:
   - `/conf/accounts.csv` with columns: `account number`, `friendly name`, `process data`.
   - `/conf/categories.csv` with columns: `search text`, `category name`.
4. System displays a menu of commands showing the list of available actions.

## UI/UX Considerations

- Focus on a simple and clean command-line interface.
- Provide clear instructions and feedback messages.
- Use color coding where supported to highlight errors and important information.

## File Structure Proposal

- `/conf`: Configuration files
- `/data`: Data files
- `/src`: Source code
- `/docs`: Documentation
- `/test`: Test files

## Assumptions

- Sample data excerpts:
  ```
  FirstName,LastName,Title,Company
  Alana,DeAngelis,Director of Business Solutions,Georgia Institute of Technology
  Amanda,Schipman,LMS Administrator,University of North Carolina at Greensboro
  Amanda,Gutman,Growth Marketing Manager,Civitas
  Anastacia,Nelson,BCIS Faculty,Central New Mexico Community College
  Andrew,Lyssy,IT Manager II,Texas A&M University
  Arthur,Kelly,"Director, Business Development",Asurion
  Aurelio,Puente,Education Technology Specialist,Lewis & Clark College
  ```

## Reflection

- Each requirement is included to ensure the tool is functional, user-friendly, and meets the needs of the target audience.
- Potential challenges include handling large CSV files and ensuring accurate OpenAI responses. Mitigation strategies involve optimizing data processing and validating OpenAI outputs.
- The specification aligns with the overall project goals by providing a clear roadmap for development and deployment.
