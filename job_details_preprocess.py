import openai

openai.organization = "org-IakVZOX3HTBgfcW488pjcEZk"
openai.api_key = "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"


def job_details_prompt_optimize(job_details):
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "system",
                 "content": "Generate the keywords for candidates vetting from the job details."},
                {"role": "user", "content": f"Job details: {job_details}"}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        # auto is default, but we'll be explicit
        max_tokens=256,
        temperature=0.8,
    )
    print(response)


def test():
    with open('ibm_rpa_intern.txt', encoding="utf_8") as f:
        contents = f.read()
    job_details_prompt_optimize(contents)


test()
