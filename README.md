# DevHack: BitVerse

## Requirements

- Python 3.10 and above
- Virtual environment (recommended)
- Libraries: `openai`, `langchain`, `streamlit`, and "unstructured[all-docs]"

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/xinghao2003/DevHack-BitVerse
    ```

2. Navigate to the project directory:

    ```bash
    cd DevHack-BitVerse
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\Activate.ps1
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install required libraries:

    ```bash
    pip install openai langchain streamlit "unstructured[all-docs]"
    ```

6. Setup OpenAI API key:

    - Edit a file named `config.py` in the project directory.
    - Inside `config.py`, set up your OpenAI API key:

        ```python
        client = OpenAI(
            organization='your-organization-id',
            api_key='your-api-key'
        )
        ```

    Replace `'your-organization-id'` and `'your-api-key'` with your actual OpenAI API key.

7. Run the application:

    ```bash
    streamlit run app.py
    ```

This will launch the application, and you can access it through your web browser at the specified address.

## License

This project is licensed under the [MIT License](LICENSE).