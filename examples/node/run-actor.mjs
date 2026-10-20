// Run one DuarteLabs Actor with apify-client.
// Usage: node run-actor.mjs <b2b|gmaps|shopify|rag|seo>   (needs APIFY_TOKEN)
import { ApifyClient } from 'apify-client';

const PRESETS = {
  b2b: ['duartelabs/b2b-lead-whatsapp-pixel-scraper',
    { startUrls: [{ url: 'https://apify.com' }], scanContactPages: true, maxPagesPerDomain: 2 }],
  gmaps: ['duartelabs/google-maps-business-email-whatsapp-enricher',
    { businessWebsites: [{ url: 'https://apify.com' }], scanContactPage: true, reportLanguage: 'en' }],
  shopify: ['duartelabs/shopify-competitor-price-stock-spy',
    { storeUrls: [{ url: 'https://hiutdenim.co.uk' }], maxProductsPerStore: 10, reportLanguage: 'en' }],
  rag: ['duartelabs/ai-website-to-markdown-rag-chunker',
    { targetUrls: [{ url: 'https://apify.com/about' }], chunkSizeTokens: 500, reportLanguage: 'en' }],
  seo: ['duartelabs/seo-meta-schema-broken-links-auditor',
    { targetUrls: [{ url: 'https://apify.com' }], verifyLinksLimit: 8, reportLanguage: 'en' }],
};

const key = process.argv[2];
if (!PRESETS[key]) {
  console.error(`Usage: node run-actor.mjs <${Object.keys(PRESETS).join('|')}>`);
  process.exit(1);
}
if (!process.env.APIFY_TOKEN) {
  console.error('Set the APIFY_TOKEN environment variable first.');
  process.exit(1);
}

const [actorId, input] = PRESETS[key];
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor(actorId).call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
