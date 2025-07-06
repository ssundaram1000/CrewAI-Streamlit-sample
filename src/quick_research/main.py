#!/usr/bin/env python
# --- force modern SQLite ---
# ---- modern SQLite shim (runs *before* CrewAI/Chroma) ----
# ---- stub that fools Chroma, no extra wheel needed ----
import types, sys
sqlite_stub = types.ModuleType("sqlite3")
sqlite_stub.sqlite_version = "3.99.0"          # any ≥ 3.35.0
sys.modules["sqlite3"] = sqlite_stub
# --------------------------------------------------------


import os, pathlib

# Tell Chroma to use DuckDB instead of SQLite
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"
# Optional: where to keep the *.parquet files
os.environ["CHROMA_PERSIST_DIRECTORY"] = str(
    pathlib.Path(__file__).parent / "chroma_store"
)


from quick_research.crew import QuickResearchCrew
from pathlib import Path
import crewai

def run_topic(topic: str) -> str:
    # Load crew + tasks defined in YAML
    inputs = {
        'topic': topic
    }
    return QuickResearchCrew().crew().kickoff(inputs=inputs)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    QuickResearchCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        QuickResearchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        QuickResearchCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        QuickResearchCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
