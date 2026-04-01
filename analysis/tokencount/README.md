# Token Counter Microservice

A Docker microservice for counting tokens in markdown files using HuggingFace tokenizers.

## Features

- Counts tokens in all markdown files within a specified directory and its subdirectories
- Configurable tokenizer (any HuggingFace model)
- Outputs results to CSV with detailed file-by-file breakdown
- Dockerized for easy deployment and consistent environment

## Configuration

Edit `settings.json` to configure the service:

```json
{
  "tokenizer": "gpt2",
  "input_directory": "../../data/filtered_data/Accepted",
  "output_directory": "../../data/filtered_data/Accepted",
  "output_filename": "token_counts.csv"
}
```

### Configuration Options

- **tokenizer**: HuggingFace model identifier (e.g., "gpt2", "microsoft/DialoGPT-medium", "bert-base-uncased")
- **input_directory**: Path to directory containing markdown files to process
- **output_directory**: Where to save the token count CSV file
- **output_filename**: Name of the output CSV file

## Usage

### Using Docker Compose (Recommended)

1. **Build and run the service:**
   ```bash
   docker-compose up --build
   ```

2. **Run with custom profile (if you modified settings.json):**
   ```bash
   docker-compose --profile custom up --build tokencount-custom
   ```

### Using Docker directly

1. **Build the image:**
   ```bash
   docker build -t tokencount .
   ```

2. **Run the container:**
   ```bash
   docker run --rm \
     -v $(pwd)/../../data:/app/data:ro \
     -v $(pwd)/../../data/filtered_data/Accepted:/app/output:rw \
     tokencount
   ```

### Running locally (without Docker)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script:**
   ```bash
   python token_counter.py
   ```

## Output

The service generates a CSV file with the following columns:

- **file_path**: Relative path to the markdown file
- **absolute_path**: Full path to the markdown file
- **token_count**: Number of tokens in the file
- **tokenizer**: Tokenizer used for counting

The last row contains a summary with total token count across all files.

## Example Output

```csv
file_path,absolute_path,token_count,tokenizer
www.telenor.dk/example.md,/app/data/filtered_data/Accepted/www.telenor.dk/example.md,1250,gpt2
www.telenor.no/help.md,/app/data/filtered_data/Accepted/www.telenor.no/help.md,890,gpt2
TOTAL,2 files processed,2140,gpt2
```

## Changing Tokenizers

To use a different tokenizer, update the `tokenizer` field in `settings.json`. Examples:

- `"gpt2"` - GPT-2 tokenizer
- `"microsoft/DialoGPT-medium"` - DialoGPT tokenizer
- `"bert-base-uncased"` - BERT tokenizer
- `"facebook/opt-350m"` - OPT tokenizer

## Troubleshooting

- **Permission errors**: Ensure the output directory is writable
- **Memory issues**: Large files or models may require more memory
- **Network issues**: First run requires internet to download the tokenizer

## Logs

The service provides detailed logging including:
- Settings loaded
- Tokenizer initialization
- File processing progress
- Final statistics 