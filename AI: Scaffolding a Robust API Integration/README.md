# AI: Scaffolding a Robust API Integration

## Objective

This task demonstrates the use of contextual prompting in an AI-assisted software engineering workflow. The original sentiment analysis tool was provided as context to an AI, which was instructed to improve authentication security and error handling while preserving the existing application behavior.

## Files

### sentiment_analyzer_initial.py

Contains the original sentiment analysis implementation provided in the assignment. The original implementation sends the text to the Text Processing API without authentication headers and handles HTTP, request, and response-format errors.

### sentiment_analyzer.py

Contains the refactored implementation generated through contextual prompting. The refactored code:

- Imports the `os` module.
- Reads the API key from the `TEXT_PROCESSING_API_KEY` environment variable.
- Sends the API key using the `Authorization: Bearer <key>` header.
- Handles `requests.exceptions.Timeout` explicitly.
- Handles `requests.exceptions.ConnectionError` explicitly.
- Retains HTTP error handling.
- Retains general request error handling.
- Retains invalid response-format handling.
- Preserves the original sentiment mapping and command-line interface.

### contextual_prompt.txt

Contains the complete contextual prompt used to instruct the AI to refactor the original sentiment analyzer. The prompt includes the full original code and specifies the security and robustness requirements.

## AI Tool Used

ChatGPT was used to analyze the supplied code and generate the refactored implementation.

## Contextual Prompting

The complete original `sentiment_analyzer.py` code was provided to the AI as context before the requested modifications were specified. The prompt explicitly required secure API-key handling through the `TEXT_PROCESSING_API_KEY` environment variable, Bearer-token authentication, and dedicated handling for timeout and connection failures.

Providing the existing code as context allowed the AI to preserve the application's existing behavior while making targeted improvements rather than generating an unrelated implementation.

## Security

The API key is not hard-coded in the source code. It is retrieved at runtime using `os.getenv("TEXT_PROCESSING_API_KEY")` and included in the request through the standard `Authorization: Bearer <key>` header.

The test environment uses the placeholder value `DUMMY_KEY`; no real secret is stored in the repository.

## Robustness

The refactored implementation explicitly handles `Timeout` and `ConnectionError` separately and prints distinct diagnostic messages to `sys.stderr`. It also retains the existing `HTTPError`, general `RequestException`, and invalid response-format handling.

This provides more specific failure information while maintaining the original sentiment-processing behavior.

## Verification

The refactored Python file was syntax-checked using:

```bash
python3 -m py_compile sentiment_analyzer.py

