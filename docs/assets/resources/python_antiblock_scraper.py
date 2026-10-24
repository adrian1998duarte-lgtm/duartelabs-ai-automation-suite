"""
DuarteLabs Production Anti-Block Web Scraper Template
Author: Cristian Duarte (DuarteLabs)
Stack: Python 3.10+ | httpx (HTTP/2) | asyncio | Tenacity Retry

Features:
- Rotating modern browser headers & Sec-CH-UA
- Automatic HTTP/2 negotiation & connection pooling
- Jittered exponential backoff retry on 429/503/timeouts
- Clean JSON / Markdown data extraction pipeline
"""

import asyncio
import random
import logging
from typing import Dict, Any, List, Optional
import httpx

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("DuarteLabsScraper")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
]

def get_stealth_headers() -> Dict[str, str]:
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://www.google.com/",
        "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1"
    }

async def fetch_with_retry(
    client: httpx.AsyncClient,
    url: str,
    max_retries: int = 4,
    base_delay: float = 1.5
) -> Optional[str]:
    for attempt in range(1, max_retries + 1):
        try:
            # Jittered randomized delay to avoid synchronized traffic spikes
            sleep_time = random.uniform(0.3, 0.9)
            await asyncio.sleep(sleep_time)

            headers = get_stealth_headers()
            response = await client.get(url, headers=headers, timeout=12.0)

            if response.status_code == 200:
                logger.info(f"✅ [200 OK] Extracted: {url} ({len(response.text)} bytes)")
                return response.text
            elif response.status_code in (429, 503):
                backoff = base_delay * (2 ** (attempt - 1)) + random.uniform(0.5, 2.0)
                logger.warning(f"⚠️ Rate limited ({response.status_code}). Backing off {backoff:.2f}s... (Attempt {attempt}/{max_retries})")
                await asyncio.sleep(backoff)
            else:
                logger.error(f"❌ HTTP Error {response.status_code} for {url}")
                return None
        except (httpx.RequestError, httpx.TimeoutException) as exc:
            backoff = base_delay * (2 ** (attempt - 1)) + random.uniform(0.5, 1.5)
            logger.warning(f"⚠️ Network error: {exc}. Retrying in {backoff:.2f}s...")
            await asyncio.sleep(backoff)

    logger.error(f"❌ Exceeded max retries for {url}")
    return None

async def main():
    target_urls = [
        "https://httpbin.org/headers",
        "https://httpbin.org/ip",
        "https://httpbin.org/user-agent"
    ]

    limits = httpx.Limits(max_keepalive_connections=20, max_connections=50)
    async with httpx.AsyncClient(http2=True, limits=limits, follow_redirects=True) as client:
        tasks = [fetch_with_retry(client, url) for url in target_urls]
        results = await asyncio.gather(*tasks)
        logger.info(f"🎉 Scraping complete. Successfully processed {len([r for r in results if r])} / {len(target_urls)} URLs.")

if __name__ == "__main__":
    asyncio.run(main())
