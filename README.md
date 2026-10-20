# DuarteLabs AI Automation Suite

Examples, n8n workflows and MCP configuration for the DuarteLabs Actors on [Apify Store](https://apify.com/duartelabs).

All Actors use lightweight HTTP requests (no headless browser) and return a summary in one of 6 languages: `en`, `es`, `pt`, `fr`, `de`, `it`.

| Actor | Use it for |
| :--- | :--- |
| [B2B Lead, WhatsApp, Email & Ad-Pixel Scraper](https://apify.com/duartelabs/b2b-lead-whatsapp-pixel-scraper) | Enrich company domains with emails, WhatsApp links, ad pixels |
| [Google Maps Business Email & WhatsApp Enricher](https://apify.com/duartelabs/google-maps-business-email-whatsapp-enricher) | Enrich Google Maps website URLs for local lead generation |
| [Shopify Competitor Price & Stock Spy](https://apify.com/duartelabs/shopify-competitor-price-stock-spy) | Monitor competitor catalogs, prices, discounts, stock |
| [Website to Clean Markdown & RAG Chunker](https://apify.com/duartelabs/ai-website-to-markdown-rag-chunker) | Prepare web pages for LLMs and vector databases |
| [Technical SEO & Broken Links Auditor](https://apify.com/duartelabs/seo-meta-schema-broken-links-auditor) | Audit meta tags, Schema.org, ALT text, 404 links |

Pricing is pay-per-result and can change; check each Store page for current rates.

## Quick start

You need an [Apify API token](https://console.apify.com/settings/integrations). Never commit it; use an environment variable.

### Python
```bash
pip install apify-client
export APIFY_TOKEN=your_token        # Windows PowerShell: $env:APIFY_TOKEN="your_token"
python examples/python/run_actor.py seo
```

### Node.js
```bash
npm install apify-client
node examples/node/run-actor.mjs seo
```

Available presets: `b2b`, `gmaps`, `shopify`, `rag`, `seo`.

## n8n
Import any file from [`n8n/`](n8n/) (`Workflows -> Import from File`) and replace `YOUR_APIFY_API_TOKEN`.

## Claude Desktop / Cursor (MCP)
Copy [`mcp/claude_cursor_mcp_config.json`](mcp/claude_cursor_mcp_config.json) into your client's MCP settings and set `APIFY_TOKEN`.

## Clay.com
Add an **HTTP API** column: `POST https://api.apify.com/v2/acts/duartelabs~<actor-name>/run-sync-get-dataset-items?token=YOUR_TOKEN` with the Actor's JSON input as the body.

## License
MIT. See [LICENSE](LICENSE). The Actors themselves run on Apify and are billed by Apify.
