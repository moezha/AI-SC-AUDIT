# AI Smart Contract Audit

## Overview

The AI Smart Contract Audit is an extension of the LLaMA 3.2 language model designed to assist in auditing smart contracts. It analyzes smart contract code and identifies potential vulnerabilities, offering suggestions for best practices and improvements.

## Features

- **Automated Vulnerability Detection**: Identifies common vulnerabilities such as reentrancy attacks, integer overflows, and gas limit issues.
- **Best Practice Recommendations**: Provides suggestions based on established best practices in smart contract development.
- **Natural Language Explanations**: Converts complex smart contract logic into easy-to-understand natural language descriptions.

## Use Cases

- **Smart Contract Auditors**: Streamline the auditing process by quickly identifying vulnerabilities.
- **Developers**: Get instant feedback on smart contract code and improve security practices.
- **Educators**: Use the tool as a teaching aid to explain smart contract vulnerabilities and best practices.

## Getting Started

### Prerequisites

- Python 3.x
- PyTorch
- Hugging Face Transformers
- A compatible GPU (recommended for fine-tuning)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/moezha/AI-SC-AUDIT.git
   cd AI-SC-AUDIT
    ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Testing and Linting

The project includes automated testing and linting to ensure code quality. Use the following commands with make to run these tools:

1. Run Linting: To check your code for stylistic errors and enforce coding standards:
   ```bash
   make lint
    ```

2. Run Tests: To execute the test suite and verify that everything works as expected:
   ```bash
   make test
   ```

3. Clean Up: To remove unnecessary files:
   ```bash
   make clean
   ```
4. Run All Checks: To execute both linting and testing in one command:
   ```bash
   make all
   ```
