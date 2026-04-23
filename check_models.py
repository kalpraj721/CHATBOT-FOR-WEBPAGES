"""Check available models on Hugging Face"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient, list_inference_api_models

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_KEY")
if not hf_token:
    print("ERROR: HUGGINGFACEHUB_API_KEY not found in .env file")
    exit(1)

print("=" * 60)
print("AVAILABLE MODELS ON YOUR HUGGING FACE ACCOUNT:")
print("=" * 60)

try:
    # List all available models
    models = list_inference_api_models(token=hf_token)

    # Show first 20 models
    for i, model in enumerate(models[:20], 1):
        print(f"{i}. {model.id}")

    print(f"\n... and more. Total available: {len(list(models))}")

except Exception as e:
    print(f"Error listing models: {e}")
    print("\nTrying alternative approach...")

    # Test some common models
    test_models = [
        "mistralai/Mistral-7B-Instruct-v0.2",
        "meta-llama/Llama-2-7b-chat-hf",
        "google/flan-t5-large",
        "gpt2",
        "EleutherAI/gpt-j-6B"
    ]

    print("\nTesting common models:")
    for model_name in test_models:
        try:
            client = InferenceClient(model=model_name, token=hf_token)
            # Quick test
            response = client.text_generation("Hello", max_new_tokens=5)
            print(f"✓ {model_name}")
        except Exception as e:
            print(f"✗ {model_name}: {str(e)[:50]}")

print("\n" + "=" * 60)
