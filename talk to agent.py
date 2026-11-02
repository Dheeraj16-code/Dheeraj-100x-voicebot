# 1. Install
# macOS: brew install portaudio   ·   Ubuntu: apt-get install portaudio19-dev
pip install "sarvam-conv-ai-sdk[all]"

# 2. talk-to-agent.py
import asyncio
from pydantic import SecretStr
from sarvam_conv_ai_sdk import (
    AsyncSamvaadAgent, AsyncDefaultAudioInterface,
    InteractionConfig, InteractionType,
)

async def main():
    config = InteractionConfig(
        org_id="019f4bc4-d91b-761c-ae41-7d27e90a912d",
        workspace_id="019f4bc4-d924-7e6e-95ae-c6d5265a4d20",
        app_id="Conversatio-029b45a4-d37f",
        user_identifier="demo_user",
        interaction_type=InteractionType.CALL,
        sample_rate=16000,
        agent_variables={"call_outcome": "<call_outcome>", "call_summary": "<call_summary>", "user_name": "<user_name>"},
    )
    agent = AsyncSamvaadAgent(
        api_key=SecretStr("<your-api-key>"),
        config=config,
        audio_interface=AsyncDefaultAudioInterface(input_sample_rate=16000),
    )
    await agent.start()
    await agent.wait_for_disconnect()

asyncio.run(main())
