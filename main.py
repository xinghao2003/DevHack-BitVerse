import csv
from unittest import result
import openai
import json
import pandas as pd

# Initialize OpenAI API
openai.organization = "org-IakVZOX3HTBgfcW488pjcEZk"
openai.api_key = "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"


def get_result(candidates_df, job_text, result_container):
    run_conversation(candidates_df, job_text, result_container)


def save_potential_candidates(candidates, response, result_container):
    try:
        res = json.loads(response["choices"][0]
                         ["message"]["function_call"]["arguments"])
        df = pd.DataFrame()
        for id in res["candidates_id"]:
            df = pd.concat([df, candidates[candidates["Candidate ID"] == id]])
        result_container.dataframe(df)
        result_container.write(response)
    except:
        result_container.write(response)
    # potential_candidates = candidates


def run_conversation(candidates, job_details, result_container):
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "system", "content": "Question: What's the candidates id who meet the job details given? Step 1: Answer the question based on Candidates list and Job details. Return only the candidates id. Step 2: Call save_potential_candidates function to save the candidates id in array format."},
                {"role": "user", "content": f"Candidates list: {candidates.to_dict()} \n Job details: {job_details}"}]
    functions = [
        {
            "name": "save_potential_candidates",
            "description": "Save potential candidates id after vetting",
            "parameters": {
                "type": "object",
                "properties": {
                    "candidates_id": {
                        "type": "array",
                        "description": "The potential candidates id",
                        "items": {
                            "type": "integer"
                        }
                    }
                },
                "required": ["candidates_id"],
            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        # auto is default, but we'll be explicit
        function_call={"name": "save_potential_candidates"},
        max_tokens=10+6*len(candidates.index),
        temperature=0.2,
    )
    save_potential_candidates(candidates, response, result_container)
