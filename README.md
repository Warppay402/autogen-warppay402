# AutoGen Tools Integration for WarpPay402

This package integrates 29 WarpPay402 x402 monetized tools into Microsoft AutoGen agents.

## Installation

```bash
pip install autogen-warppay402
```

## Usage

```python
import autogen
from autogen_warppay402 import WarpPayAutoGenTools

assistant = autogen.AssistantAgent(
    "assistant",
    llm_config={"config_list": [{"model": "gpt-4o"}]},
)
user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    code_execution_config=False,
)

warppay_tools = WarpPayAutoGenTools()
warppay_tools.register_all(assistant, user_proxy)

user_proxy.initiate_chat(
    assistant,
    message="What is the ETH spot price on Arc Mainnet?",
)
```

## What this package provides

- AutoGen-compatible registration helpers for WarpPay402 tools
- Support for 29 built-in x402 monetized tool actions
- Easy integration with an existing AutoGen assistant and user proxy setup

## Example tools

This package registers tools including:

- `public_data_feed`
- `base_analytics`
- `arc_analytics`
- `arc_dex_oracle`
- `pdf_extractor`
- `weather_oracle`
- `forex_oracle`
- `github_health_analyzer`
- `smart_contract_verifier`
- `render_screenshot`

For the full list, see the `WarpPayAutoGenTools.get_tool_functions()` method in the package source.
