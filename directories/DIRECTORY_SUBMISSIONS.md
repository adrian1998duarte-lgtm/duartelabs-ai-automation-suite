# Listing text for MCP / AI-tool directories

Submit the same entry to each directory. These need your own account or a pull request, so do them by hand.

| Directory | How to submit |
| :--- | :--- |
| mcp.so | Sign in with GitHub, use "Submit" |
| glama.ai/mcp/servers | Add the GitHub repo URL, or submit through the site |
| smithery.ai | Sign in with GitHub, add a server |
| pulsemcp.com | Use the "Submit" form on the site |

I could not verify each site's current submission flow from here, so check the page before filling it in. These directories list MCP *servers*; this repo is a configuration plus examples built on Apify's official `@apify/actors-mcp-server`, so describe it that way and do not claim it is a standalone server.

## Name
DuarteLabs Automation Suite

## One-line description
Apify Actors for lead enrichment, Google Maps enrichment, Shopify price monitoring, website-to-Markdown/RAG preparation, technical SEO audits and sitemap-to-llms.txt dataset builders, usable from Claude Desktop and Cursor through Apify's MCP server.

## Long description
Six lightweight HTTP-based Actors published on Apify Store by DuarteLabs. They return structured JSON and a short summary in English, Spanish, Portuguese, French, German or Italian. Connect them to an MCP client with the config in `mcp/claude_cursor_mcp_config.json` (requires an Apify API token). Also includes n8n workflow templates and Python/Node examples.

## Install / config
```json
{
  "mcpServers": {
    "duartelabs": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server", "--actors",
        "duartelabs/b2b-lead-whatsapp-pixel-scraper,duartelabs/google-maps-business-email-whatsapp-enricher,duartelabs/shopify-competitor-price-stock-spy,duartelabs/ai-website-to-markdown-rag-chunker,duartelabs/seo-meta-schema-broken-links-auditor,duartelabs/sitemap-to-llms-txt-markdown-rag-builder"],
      "env": { "APIFY_TOKEN": "YOUR_APIFY_API_TOKEN" }
    }
  }
}
```

## Links
- Apify profile: https://apify.com/duartelabs
- Repository: https://github.com/adrian1998duarte-lgtm/duartelabs-ai-automation-suite

## Tags
apify, mcp, lead-generation, google-maps, shopify, seo, rag, markdown, n8n, clay
