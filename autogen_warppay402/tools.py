from typing import Dict, Any, Callable, List, Optional
import json
import warppay402_mcp as mcp

class WarpPayAutoGenTools:
    """Provides AutoGen-compatible tool registrations for WarpPay402 x402 tools."""

    def __init__(self):
        # Instantiate individual tool objects exported by warppay402_mcp
        self.tools = {
            "public_data_feed": mcp.PublicDataFeedTool(),
            "data_feeds": mcp.DataFeedsTool(),
            "web_scraper": mcp.WebScraperTool(),
            "browser_scraper": mcp.BrowserScraperTool(),
            "base_analytics": mcp.BaseAnalyticsTool(),
            "arc_analytics": mcp.ArcAnalyticsTool(),
            "arc_network_oracle_query": mcp.ArcNetworkQueryTool(),
            "arc_dex_oracle": mcp.ArcDexOracleTool(),
            "pdf_extractor": mcp.PdfExtractorTool(),
            "render_screenshot": mcp.RenderScreenshotTool(),
            "extract_json": mcp.ExtractJsonTool(),
            "smart_contract_verifier": mcp.SmartContractVerifierTool(),
            "get_aerodrome_yields": mcp.AerodromeYieldsTool(),
            "aerodrome_swap": mcp.AerodromeSwapTool(),
            "aerodrome_clamm": mcp.AerodromeClammTool(),
            "aerodrome_veaero": mcp.AerodromeVeaeroTool(),
            "deploy_contract": mcp.DeployBaseContractTool(),
            "deploy_solana_contract": mcp.DeploySolanaContractTool(),
            "deploy_arc_contract": mcp.DeployArcContractTool(),
            "arc_cctp_bridge": mcp.ArcCctpBridgeTool(),
            "real_estate_calculator": mcp.RealEstateCalculatorTool(),
            "address_normalizer": mcp.AddressNormalizerTool(),
            "weather_oracle": mcp.WeatherOracleTool(),
            "forex_oracle": mcp.ForexOracleTool(),
            "shipping_rate_estimator": mcp.ShippingRateEstimatorTool(),
            "github_health_analyzer": mcp.GithubHealthAnalyzerTool(),
            "property_comps_estimator": mcp.PropertyCompsEstimatorTool(),
            "outage_oracle": mcp.OutageOracleTool(),
            "ucp_deals_oracle": mcp.UcpDealsOracleTool(),
        }

    def get_tool_functions(self) -> Dict[str, Callable]:
        """Returns a dictionary mapping tool names to executable functions for AutoGen."""
        functions = {}
        for name, tool_obj in self.tools.items():
            # Wrap execution via the tool's .invoke() interface
            functions[name] = lambda kwargs, t=tool_obj: str(t.invoke(kwargs))
        return functions

    def register_all(self, assistant_agent, user_proxy_agent):
        """Helper to register all 29 tools between an AssistantAgent and UserProxyAgent."""
        for name, tool_obj in self.tools.items():
            func = lambda **kwargs: str(tool_obj.invoke(kwargs))
            assistant_agent.register_for_llm(name=name, description=tool_obj.description)(func)
            user_proxy_agent.register_for_execution(name=name)(func)