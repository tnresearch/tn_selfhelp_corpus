#!/usr/bin/env python3
"""
Token Counter Service
Counts tokens in markdown files using specified HuggingFace tokenizer
"""

import json
import os
import pandas as pd
from pathlib import Path
from transformers import AutoTokenizer
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TokenCounter:
    def __init__(self, settings_path="settings.json"):
        """Initialize the token counter with settings"""
        self.settings = self.load_settings(settings_path)
        self.tokenizer = self.load_tokenizer()
        
    def load_settings(self, settings_path):
        """Load settings from JSON file"""
        try:
            with open(settings_path, 'r') as f:
                settings = json.load(f)
            logger.info(f"Settings loaded from {settings_path}")
            return settings
        except FileNotFoundError:
            logger.error(f"Settings file {settings_path} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in settings file {settings_path}")
            raise
    
    def load_tokenizer(self):
        """Load the specified tokenizer from HuggingFace"""
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.settings['tokenizer'])
            logger.info(f"Tokenizer '{self.settings['tokenizer']}' loaded successfully")
            return tokenizer
        except Exception as e:
            logger.error(f"Failed to load tokenizer '{self.settings['tokenizer']}': {e}")
            raise
    
    def count_tokens_in_file(self, file_path):
        """Count tokens in a single markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Tokenize the content
            tokens = self.tokenizer.encode(content)
            token_count = len(tokens)
            
            logger.debug(f"File: {file_path}, Tokens: {token_count}")
            return token_count
        
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {e}")
            return 0
    
    def find_markdown_files(self, directory):
        """Find all markdown files in directory and subdirectories"""
        markdown_files = []
        directory_path = Path(directory)
        
        if not directory_path.exists():
            logger.error(f"Directory {directory} does not exist")
            return markdown_files
        
        # Find all .md files recursively
        for md_file in directory_path.rglob("*.md"):
            markdown_files.append(md_file)
        
        logger.info(f"Found {len(markdown_files)} markdown files in {directory}")
        return markdown_files
    
    def process_files(self):
        """Process all markdown files and generate token count report"""
        input_dir = self.settings['input_directory']
        output_dir = self.settings['output_directory']
        output_file = self.settings['output_filename']
        
        # Find all markdown files
        markdown_files = self.find_markdown_files(input_dir)
        
        if not markdown_files:
            logger.warning("No markdown files found to process")
            return
        
        # Process each file and collect results
        results = []
        total_tokens = 0
        
        for file_path in markdown_files:
            token_count = self.count_tokens_in_file(file_path)
            relative_path = os.path.relpath(file_path, input_dir)
            
            results.append({
                'file_path': str(relative_path),
                'absolute_path': str(file_path),
                'token_count': token_count,
                'tokenizer': self.settings['tokenizer']
            })
            
            total_tokens += token_count
        
        # Create DataFrame and save to CSV
        df = pd.DataFrame(results)
        
        # Add summary row
        summary_row = {
            'file_path': 'TOTAL',
            'absolute_path': f"{len(markdown_files)} files processed",
            'token_count': total_tokens,
            'tokenizer': self.settings['tokenizer']
        }
        df = pd.concat([df, pd.DataFrame([summary_row])], ignore_index=True)
        
        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Save to CSV
        output_path = Path(output_dir) / output_file
        df.to_csv(output_path, index=False)
        
        logger.info(f"Token count report saved to: {output_path}")
        logger.info(f"Total files processed: {len(markdown_files)}")
        logger.info(f"Total tokens: {total_tokens:,}")
        
        return df

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Count tokens in markdown files')
    parser.add_argument('--settings', default='settings.json', 
                       help='Path to settings JSON file (default: settings.json)')
    
    args = parser.parse_args()
    
    try:
        counter = TokenCounter(args.settings)
        counter.process_files()
        logger.info("Token counting completed successfully")
    
    except Exception as e:
        logger.error(f"Token counting failed: {e}")
        exit(1)

if __name__ == "__main__":
    main() 