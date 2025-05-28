import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the API key
client = openai.OpenAI(api_key=os.getenv("CHATGPT_API_KEY"))

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

# ========== MENU OF OPTIONS ==========

print("Welcome to Job Search GPT Assistant!\nChoose an option:")
print("1. Generate a Cover Letter")
print("2. Create a LinkedIn Post")
print("3. Summarize a Job Description")
print("4. Exit")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    job_title = input("Enter the job title: ")
    company = input("Enter the company name: ")
    prompt = f"Write a 1-page cover letter for a {job_title} role at {company}. Be professional and highlight leadership and project management skills."
    print("\nGenerating cover letter...\n")
    print(get_completion(prompt))

elif choice == "2":
    focus = input("What is the post about? (e.g., looking for TPM roles, career advice, etc.): ")
    prompt = f"Write a professional and engaging LinkedIn post for someone {focus}. Add relevant hashtags and a friendly tone."
    print("\nGenerating LinkedIn post...\n")
    print(get_completion(prompt))

elif choice == "3":
    print("Paste the job description below. Press Enter twice when done:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    job_desc = "\n".join(lines)
    prompt = f"Summarize this job description into 5 bullet points:\n{job_desc}"
    print("\nSummarizing job description...\n")
    print(get_completion(prompt))

else:
    print("Goodbye!")
