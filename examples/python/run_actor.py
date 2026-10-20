"""Run one DuarteLabs Actor with apify-client.

Usage:  python run_actor.py <b2b|gmaps|shopify|rag|seo>
Needs the APIFY_TOKEN environment variable.
"""
import os
import sys

from apify_client import ApifyClient

PRESETS = {
    "b2b": ("duartelabs/b2b-lead-whatsapp-pixel-scraper",
            {"startUrls": [{"url": "https://apify.com"}], "scanContactPages": True, "maxPagesPerDomain": 2}),
    "gmaps": ("duartelabs/google-maps-business-email-whatsapp-enricher",
              {"businessWebsites": [{"url": "https://apify.com"}], "scanContactPage": True, "reportLanguage": "en"}),
    "shopify": ("duartelabs/shopify-competitor-price-stock-spy",
                {"storeUrls": [{"url": "https://hiutdenim.co.uk"}], "maxProductsPerStore": 10, "reportLanguage": "en"}),
    "rag": ("duartelabs/ai-website-to-markdown-rag-chunker",
            {"targetUrls": [{"url": "https://apify.com/about"}], "chunkSizeTokens": 500, "reportLanguage": "en"}),
    "seo": ("duartelabs/seo-meta-schema-broken-links-auditor",
            {"targetUrls": [{"url": "https://apify.com"}], "verifyLinksLimit": 8, "reportLanguage": "en"}),
}

if len(sys.argv) != 2 or sys.argv[1] not in PRESETS:
    sys.exit("Usage: python run_actor.py <" + "|".join(PRESETS) + ">")

token = os.environ.get("APIFY_TOKEN")
if not token:
    sys.exit("Set the APIFY_TOKEN environment variable first.")

actor_id, run_input = PRESETS[sys.argv[1]]
client = ApifyClient(token)
run = client.actor(actor_id).call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
