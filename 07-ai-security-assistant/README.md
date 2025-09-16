# AI Security Assistant

This project explores the use of large language models and machine learning to augment incident response and security policy development.

## Overview

AI Security Assistant is a proof-of-concept chatbot that ingests security logs and alerts, summarizes key findings, and generates recommended actions. Built using Python and the OpenAI API, it demonstrates how generative models can accelerate threat triage and knowledge sharing.

Key capabilities include:
- Parsing JSON and CSV logs, extracting notable events, and summarizing them in plain language.
- Answering questions about security policies, compliance requirements, and best practices.
- Generating template policies and procedures based on natural-language prompts.

The assistant is trained on synthetic log datasets and public policy frameworks. It can be extended to integrate with SIEM platforms or Slack for real-time collaboration.

## Requirements

- Python 3.x
- openai and pandas libraries (`pip install -r requirements.txt`)
- An OpenAI API key (or replace with another LLM provider)

## Usage

Run `python assistant.py --input sample_logs.csv` to generate a summary report. Use the interactive shell to ask follow-up questions.

## Deliverables

- `assistant.py` – script demonstrating LLM-based summarization and policy generation.
- `sample_logs.csv` – synthetic login and HTTP events used for testing.
- Documentation outlining how to adapt the assistant for real-world SIEM integrations.
