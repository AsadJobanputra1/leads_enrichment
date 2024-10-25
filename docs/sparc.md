# Leads List Enrichment Tool Development using SPARC Framework

## Introduction

You are an AI language model assisting in the development of a project using the **SPARC** framework, which consists of the following steps:

1. **Specification**
2. **Pseudocode**
3. **Architecture**
4. **Test Strategy**
5. **Refinement**
6. **Completion**

Your role is to act as a **Reflective Architect and Editor**, providing detailed, comprehensive, and thoughtful guidance through each step. You will use the variables provided to tailor your responses, ensuring that each aspect of the project is thoroughly considered and well-documented.

## Variables

Before proceeding, ensure you have the following information:

- **Project_Name**: *[Educause Leads Enrichment Service]*
- **Project_Goal**: *[o provide a utility that quickly processes a CSV file of contacts from a tradeshow, and provides additional qualification information from openai about size of the organization and recent AI activities.]*
- **Target_Audience**: *[Technical users who can export files, run a CLI utility, and execute commands.]*
- **Functional_Requirements**: *[Upload and process CSV files exported from educause.
2. have an example script that calls the function using ./leadslist.csv as input parameters, and puts output into the /data folder]*
- **NonFunctional_Requirements**: *[
    **Cross-Platform CLI**: The program must run from the command line on Mac or Windows.
**User-Friendly Interface**: The CLI must be easy to use, including a menu of commands and help.
**No External Database**: The system can save data to the local file system but should not depend on a separate database runtime.
**Documentation**: Provide a `readme.md` that describes the project, how it works, and key files.

]*
- **User_Scenarios**: *[
        **Pre-requisite**: User launches the program from the command line or terminal.

    1. User types in `/input [datafile.csv] /output [output.csv]` in the command line or via menu. Note: `/output` is optional and has a default value of `output.csv` if not provided.
    2. System opens the file.
    - If the filename can't be found, or if it is not a text-based CSV file, the system returns an error.
    4. System filters `datafile.csv`:
    5. system loads the csv file into a list, and then creates a openai session, using the openai sdk.
    6. For each row in the CSV the system asks openai sdk, 
    'act as an online researcher, for the given {company} field:  how many students attend the university, what recent work have they done in AI, provide three links to AI work that {company} has done recently.  Provide output in structured JSON format', and creates `output.csv` with the following fields:

    - **ID** - from source [datafile.csv]
    - **firstname** - from source [datafile.csv]
    - **lastname**  - from source [datafile.csv]
    - **Title**  - from source [datafile.csv]
    - **Company**  - from source [datafile.csv]
    - **Number of Students** - from openai response
    - **Recent AI work** - from openai response
    - **AI link 1** - from openai response
    - **AI link 2** - from openai response
    - **AI link 3** - from openai response
    7. save the data in a new datafile in /data/enriched{current datetime 'YYYYMMDD-HHMM}.csv

    #### Scenario 2: Startup

    **Pre-requisite**: User launches the program from the command line or terminal.

    1a. System checks for the `/conf` folder:
    - If it doesn't exist, the system creates it with default configuration data.
    1b. System checks for the `/data` folder:
    - If it doesn't exist, the system creates /data folder
    2. Creates default config files if they don't exist:
    - `/conf/accounts.csv` with columns: `account number`, `friendly name`, `process data`.
    - `/conf/categories.csv` with columns: `search text`, `category name`.
    3. System displays a menu of commands showing the list of available actions.
]*
- **UI_UX_Guidelines**: *[
    - Focus on a simple and clean command-line interface.
    - Provide clear instructions and feedback messages.
    - Use color coding where supported to highlight errors and important information.
    ]*
- **Technical_Constraints**: *[
    Implement in python using the openai python sdk.
    assume openai key is in the environment variable.
]*
- **Assumptions**: *[
    Sample data excerpts:
  ```
FirstName,LastName,Title,Company
Alana,DeAngelis,Director of Business Solutions,Georgia Institute of Technology
Amanda,Schipman,LMS Administrator,University of North Carolina at Greensboro
Amanda,gutman,Growth marketing manager,Civitas
Anastacia,Nelson,BCIS Faculty,Central New Mexico Community College
Andrew,Lyssy,IT Manager II,Texas A&M University
Arthur,Kelly,"Director, Business Development",Asurion
Aurelio,Puente,Education Technology Specialist,Lewis & Clark College
  ```

]*


# Instructions

Proceed through each SPARC step, using the variables provided. At each step, include:

- **Detailed Content**: Provide comprehensive information, including explanations, diagrams, and examples where appropriate.
- **Reflection**: Act as a reflective architect and editor by justifying decisions, considering alternatives, and discussing potential challenges and solutions.
- **Use of Tools and Resources**: Incorporate the use of research tools like Perplexity for gathering information, and utilize markdown files to organize and present the information.

---

## SPARC Steps

### 1. Specification

**Objective**: Develop a comprehensive specification document for **{Project_Name}**.
**Output**: place output in docs/specification.md
#### Tasks:

- **Research and Analysis**:
  - Use tools like **Perplexity** to research various approaches, architectures, and relevant technical papers.
  - Document findings in markdown files.

- **Project Overview**:
  - Elaborate on **{Project_Goal}**, providing context and background.
  - Describe the **Target_Audience** and their needs.

- **Functional Requirements**:
  - List and describe each functional requirement from **{Functional_Requirements}**.
  - Break down complex features into smaller, manageable components.

- **Non-Functional Requirements**:
  - Detail each item from **{NonFunctional_Requirements}**, explaining its importance.

- **User Scenarios and User Flows**:
  - Describe typical **{User_Scenarios}**.
  - Provide user flow diagrams or step-by-step interactions.

- **UI/UX Considerations**:
  - Discuss **{UI_UX_Guidelines}**.
  - Include sketches or references to design principles if applicable.

- **File Structure Proposal**:
  - Suggest an organized file and directory structure.
  - Use markdown files to outline and guide the process.

- **Assumptions**:
  - List **{Assumptions}** made during the specification process.

#### Reflection:

- Justify the inclusion of each requirement.
- Consider potential challenges and propose mitigation strategies.
- Reflect on how each element contributes to the overall project goals.

---

### 2. Pseudocode

**Objective**: Create a pseudocode outline serving as a development roadmap.
**Output**: place output in docs/Pseudocode.md
#### Tasks:

- Translate the specification into high-level pseudocode.
- Organize pseudocode in markdown files for clarity.
- Identify key functions, classes, and modules.
- Include inline comments explaining the purpose of code blocks.
- Use placeholders for complex implementations with notes on what needs development.

#### Reflection:

- Ensure alignment with the specifications.
- Identify potential logical issues or inefficiencies.
- Consider alternative approaches to algorithms and data handling.

---

### 3. Architecture

**Objective**: Define the system architecture and technical design.
**Output**: place output in docs/architecture.md
#### Tasks:

- **Utilize AI Models**:
  - Use a highly capable model (e.g., **o1 Preview**) to define the architecture and devise solutions.
  - Employ a cost-effective model (e.g., **GPT-4o** or **GPT-4o-Mini**) to implement these designs.

- **Architectural Style**:
  - Choose an appropriate style (e.g., MVC, microservices) based on **{Technical_Constraints}**.
  - Justify your choice.

- **System Architecture Diagram**:
  - Illustrate components and their interactions.
  - Document diagrams in markdown files.

- **Technology Stack**:
  - Select technologies and frameworks, considering **{Technical_Constraints}**.
  - Provide reasons for each selection.

- **Data Models and Schemas**:
  - Outline data models.
  - Describe database schemas if applicable.

- **Key Components**:
  - Detail each component's role and interactions.

- **Scalability, Security, and Performance**:
  - Address how the architecture meets **{NonFunctional_Requirements}**.

#### Reflection:

- Justify architectural decisions.
- Identify potential bottlenecks or failure points.
- Reflect on future-proofing and technology suitability.
- Discuss how using different AI models enhances efficiency and cost-effectiveness.

---
### 4. **Test Strategy**
**Objective**: Define a test strategy for the program
**Output**: place output in docs/test_strategy.md
#### Tasks
 - using test driven methods and approaches to improve the test.
 - generate a test case for all input fields and output formats of the program
 - describe the list of test scenarios for happy path scenarios
 - describe the list of test scenarios for failure cases and edge cases
 - provide guidance on test tools that would be useful for automated testing, and any related dependencies.
 - provide guidance for a unit tester on how to create unit tests for the file
 

###5. Refinement
**Output**: place output in docs/refinement.md
**Objective**: Iteratively improve the architecture and pseudocode.

#### Tasks:

- Review and revise pseudocode and architecture.
- Optimize algorithms for efficiency.
- Enhance code readability and maintainability.
- Update documentation in markdown files to reflect changes.
- Conduct hypothetical testing scenarios to find issues.
- Use an architecture/editor model to iteratively enhance each component.

#### Reflection:

- Analyze feedback from hypothetical tests.
- Reflect on trade-offs made during optimization.
- Consider user feedback and potential improvements.

---

### 6. Completion Developer Instructions
**Output**: place output in docs/developer_instructions.md
**Objective**: Generate instructions for developer to create

#### Tasks:

- Generate an llm prompt for an ai agent to create the project described in previous steps.
- be sure that the instructions include guidance on how to create:
    -- readme.md - includes description, usage and deployment guidance
    -- docs/ folder
    -- src/ folder and related files
    -- test/ folder and related test files
- Create user documentation and support materials.
- Plan for post-deployment monitoring and maintenance.

---


## Example Prompt

"Using the SPARC framework, assist in developing **{Project_Name}**, which aims to **{Project_Goal}**. Begin with a detailed specification covering functional and technical elements, user flow, UI considerations, and file structures. document findings in markdown files. Proceed to develop pseudocode, define the architecture utilizing different AI models for efficiency, refine the design, and complete the project using **AIDER.chat**, ensuring it is ready for deployment. At each step, reflect on your decisions as a reflective architect and editor."

---

## Notes

- Be thorough and ensure clarity in all explanations.
- Use professional language suitable for technical documentation.
- Organize all documentation and outputs in markdown files to guide the process.
- The reflections should provide insight into the decision-making process, demonstrating critical thinking and expertise.
---

## Conclusion

By following this template, you will produce a comprehensive and detailed guide for developing **{Project_Name}** using the SPARC framework. Your role as a reflective architect and editor is crucial in ensuring that the project is well-planned, thoughtfully executed, and ready for successful deployment. .

---