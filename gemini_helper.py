import time

def generate_with_retry(client, prompt, model="gemini-2.5-flash", retries=3, delay=10):
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"\n[API Error] Attempt {attempt + 1}/{retries} failed: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise e