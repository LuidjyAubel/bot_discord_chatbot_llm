import os
import json

# Lire le fichier de configuration existant
with open("config.json", "r") as f:
    config = json.load(f)

# Mettre à jour les valeurs avec les variables d'environnement
config["llm_settings"]["providers"]["openai"]["api_key"] = os.getenv("API_KEY_OPENAI", "default_api_key")
config["llm_settings"]["providers"]["mistral"]["api_key"] = os.getenv("API_KEY_MISTRAL", "default_api_key")
config["llm_settings"]["providers"]["groq"]["api_key"] = os.getenv("API_KEY_GROQ", "default_api_key")
config["llm_settings"]["providers"]["openrouter"]["api_key"] = os.getenv("API_KEY_OPENROUTER", "default_api_key")
config["llm_settings"]["providers"]["ollama"]["api_key"] = os.getenv("API_KEY_OLLAMA", "default_api_key")
config["llm_settings"]["providers"]["oobabooga"]["api_key"] = os.getenv("API_KEY_OOBABOOGA", "default_api_key")
config["llm_settings"]["providers"]["jan"]["api_key"] = os.getenv("API_KEY_JAN", "default_api_key")
config["llm_settings"]["providers"]["lmstudio"]["api_key"] = os.getenv("API_KEY_LMSTUDIO", "default_api_key")
config["llm_settings"]["model"] = os.getenv("MODEL","openai/gpt-4o")
config["llm_settings"]["extra_api_parameters"]["max_tokens"] = os.getenv("MAX_TOKEN",4096)
config["discord_settings"]["bot_token"] = os.getenv("BOT_TOKEN", "default_bot_token")
config["discord_settings"]["client_id"] = int(os.getenv("CLIENT_ID", "default_client_id"))
config["discord_settings"]["status_message"] = int(os.getenv("STATUS", "Attente"))
# Écrire les modifications dans le fichier config.json
with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

print("Fichier config.json mis à jour avec les nouvelles valeurs.")