# 🚀 n8n Community Showcase & Forum Post

Use this ready-to-publish template to post on:
1. **n8n Official Forum** ([community.n8n.io](https://community.n8n.io) -> Category: **Workflows / Share your workflow**)
2. **Reddit** (`r/n8n`, `r/webscraping`, `r/GrowthHacking`)

---

## 📌 Post Title (High Click-Through Rate)
> **[Template] Enrich Google Maps & B2B leads with WhatsApp Click-to-Chat + Ad Pixels for $0.0009 (Zero Apollo/Clay fees)**

---

## 📝 Post Body (Copy & Paste)

Hey n8n community! 👋

Like many of you running lead generation and outreach workflows, I got tired of paying $99 to $149/month on Apollo and Clay just to get generic info with zero WhatsApp links or verified ad pixels.

I built a lightweight, browserless pipeline that extracts **verified decision-maker contacts, direct WhatsApp click-to-chat links, and checks for 9+ active ad pixels (Meta, TikTok, Google Ads)** for less than a penny per lead (~$0.0009 to $0.0025).

I've packaged the complete workflow into a ready-to-import n8n template for the community!

---

### ⚡ What the workflow does:
1. **Trigger / Input:** Accepts a list of domains or Google Maps business URLs (via Webhook, Google Sheets, or manual list).
2. **High-Speed Enrichment (HTTP/2):** Calls the DuarteLabs Actor on Apify (no Chromium, executes in under 2.5s).
3. **Multi-Channel Parsing:**
   - Separates decision-maker emails (`ceo@`, `founder@`) from generic info (`contact@`).
   - Generates a pre-calculated `whatsapp_direct_url` (click-to-chat with a prefilled message).
   - Audits whether the business spends money on ads (Meta Pixel, Google Tag, TikTok Pixel).
   - Generates a personalized outreach hook in 6 languages (`EN`, `ES`, `PT`, `FR`, `DE`, `IT`).
4. **CRM Sync / Delivery:** Appends the enriched lead directly to your CRM, Google Sheets, or triggers a notification.

---

### 📦 How to install in your n8n instance:
1. In n8n, click **Workflows** -> **Import from URL** or paste the JSON.
2. Template Raw JSON:
   `https://raw.githubusercontent.com/adrian1998duarte-lgtm/duartelabs-ai-automation-suite/main/n8n/n8n_b2b_lead_whatsapp_workflow.json`
3. Add your Apify API Token in the HTTP Request node (Apify gives $5/mo free usage credits, so you can test thousands of leads completely free).

---

### 🔗 Resources & Open-Source Repo:
- **GitHub Suite & Workflow Templates:** [github.com/adrian1998duarte-lgtm/duartelabs-ai-automation-suite](https://github.com/adrian1998duarte-lgtm/duartelabs-ai-automation-suite)
- **Interactive Documentation & ROI Calculator:** [adrian1998duarte-lgtm.github.io/duartelabs-ai-automation-suite](https://adrian1998duarte-lgtm.github.io/duartelabs-ai-automation-suite/)
- **Apify Actor Store:** [apify.com/duartelabs](https://apify.com/duartelabs)

Let me know what you think or if you want me to add more nodes (e.g. HubSpot, Notion, or Slack integration)! Feedback is super welcome. 🙌
