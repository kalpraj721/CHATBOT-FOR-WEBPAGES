"""Test available Gemini models"""

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env file")
    exit(1)

genai.configure(api_key=api_key)

print("=" * 60)
print("AVAILABLE MODELS FOR YOUR API KEY:")
print("=" * 60)

try:
    models = genai.list_models()

    for i, model in enumerate(models, 1):
        print(f"\n{i}. {model.name}")
        print(f"   Display Name: {model.display_name}")
        print(f"   Supported Methods:")
        if hasattr(model, 'supported_generation_methods'):
            for method in model.supported_generation_methods:
                print(f"     - {method}")
        print(f"   Description: {model.description[:100]}...")

except Exception as e:
    print(f"ERROR listing models: {e}")
    print("\nTrying alternative approach...")

    # Try individual models
    test_models = ["gemini-pro", "gemini-1.5-pro", "gemini-1.5-flash", "gemini-2.0-flash"]

    for model_name in test_models:
        try:
            model = genai.get_model(f"models/{model_name}")
            print(f"✓ {model_name} is available")
        except Exception as e:
            print(f"✗ {model_name} is NOT available: {e}")

print("\n" + "=" * 60)
