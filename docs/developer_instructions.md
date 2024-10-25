# Developer Instructions for Educause Leads Enrichment Service

## Overview

This document provides detailed instructions for developers to create the Educause Leads Enrichment Service, ensuring all components are correctly implemented and the project is ready for deployment.

## LLM Prompt for AI Agent

"Using the SPARC framework, assist in developing the Educause Leads Enrichment Service, which aims to provide a utility that quickly processes a CSV file of contacts from a tradeshow and provides additional qualification information from OpenAI about the size of the organization and recent AI activities. Begin with a detailed specification covering functional and technical elements, user flow, UI considerations, and file structures. Document findings in markdown files. Proceed to develop pseudocode, define the architecture utilizing different AI models for efficiency, refine the design, and complete the project using AIDER.chat, ensuring it is ready for deployment. At each step, reflect on your decisions as a reflective architect and editor."

## Project Setup

1. **Create Project Structure**:
   - `/docs`: Documentation files
   - `/src`: Source code files
   - `/test`: Test files
   - `/conf`: Configuration files
   - `/data`: Data files

2. **Environment Setup**:
   - Ensure Python is installed.
   - Set up a virtual environment and install necessary dependencies using `pip install -r requirements.txt`.

3. **Configuration**:
   - Store OpenAI API keys securely using environment variables.
   - Ensure default configuration files are present in the `/conf` directory.

## File Creation

1. **README.md**:
   - Include a project description, usage instructions, and deployment guidance.

2. **Source Code**:
   - Implement the pseudocode and architecture as outlined in the documentation.
   - Ensure code is modular and follows best practices.

3. **Test Files**:
   - Create unit tests for all major functions.
   - Use `pytest` or `unittest` for testing.

## Documentation

- Ensure all documentation is up-to-date and reflects the current state of the project.
- Include user documentation and support materials.

## Deployment

- Plan for post-deployment monitoring and maintenance.
- Ensure the system is scalable and secure.

## Reflection

- Reflect on the development process and document any challenges and solutions.
- Consider user feedback and potential improvements for future iterations.
