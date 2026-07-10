# Public Source And Platform Method

Status: research and preparation policy; no integration configured
Date checked: 2026-07-10

## Public-Source Method

The intake role may read public product pages, official docs, public blogs, changelogs, pricing pages, press releases, and public company news. Manually observed public social content can suggest language, format, or objection themes only. It cannot prove buyer pain, market demand, conversion, revenue, ROI, customer outcome, or platform capability.

For each accepted signal, store only a concise public-safe record:

| Field | Requirement |
|---|---|
| Source category | Official product/company news, official platform guidance, public company page, or public format observation |
| URL and date checked | Public URL plus the date it was reviewed |
| Extracted theme | A short summary, not copied post/comment text |
| Evidence grade | Primary official, public company, or format hypothesis |
| Claim status | FACT, INTERPRETATION, HYPOTHESIS, or GAP |
| Disposition | Accepted for planning, needs review, or blocked |

Do not retain screenshots, video downloads, copied comment threads, handles, profile data, follower figures, account identifiers, or raw engagement data.

## Platform Readiness Matrix

| Surface | Preparation allowed now | Future API or publishing condition | Current status and official source |
|---|---|---|---|
| LinkedIn | Public-safe draft and visual specification; manually observed public formats only | Separate approval must confirm permitted use case, authorization, data handling, required access tier, and owner approval | LinkedIn documents organization-content management and a reviewed access process. [Community Management API migration guide](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-api-migration-guide?view=li-lms-2026-06), [Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api?view=li-lms-2026-03&viewFallbackFrom=li-lms-2025-03) |
| X | Public-safe draft and short-form adaptation; no collection | Separate approval must cover developer access, credentials, budget, rate limits, policy compliance, and explicit owner action | X documents developer access and API policy; no X access is configured for this architecture. [Getting access](https://docs.x.com/x-api/getting-started/getting-access), [Developer guidelines](https://docs.x.com/developer-guidelines) |
| Threads | Draft adaptation and mockup specification only | Recheck the current Meta documentation, authorization, terms, data use, and owner approval before any implementation | GAP - current official Meta guidance must be rechecked before implementation. The official [Threads documentation](https://developers.facebook.com/docs/threads/) was not retrievable during this review, so this document makes no capability claim. |
| Reels-style formats | Storyboard, static cover, and script only | Recheck current Meta documentation and obtain explicit approval before any account or publishing action | GAP - no Instagram/Reels API capability is asserted. Use the official [Instagram Platform documentation](https://developers.facebook.com/docs/instagram-platform/) as the approval-time starting point. |
| Shorts-style formats | Short script, cover, and companion static only | Separate approval must cover API terms, authorization, and any upload action | YouTube search is documented as an API endpoint and its services have separate terms; no API call or upload is authorized here. [Search reference](https://developers.google.com/youtube/v3/docs/search/list), [API services terms](https://developers.google.com/youtube/terms/api-services-terms-of-service) |
| TikTok-style formats | Format research, script, and cover only | Separate approval must cover registered-app, user authorization, scope, and publishing review | TikTok documents a user-authorized content-posting flow; it is not enabled by this plan. [Content Posting API](https://developers.tiktok.com/products/content-posting-api/) |

## Absolute Prohibitions

- No scraping, browser automation, private-account access, direct messages, comments, profile enrichment, follower/engagement graphs, downloaded media, API calls, credentials, or account writes.
- No automatic or cross-account posting, scheduling, publishing, uploading, replying, liking, following, or message sending.
- No provider activation or external writeback.
- No claim that a platform integration exists because an official documentation URL exists.

## Competitor Content Analyzer Method

Compare public messages by alternative category: product-management suite, insight repository, AI PRD drafting tool, workspace AI, and manual/human alternative. Capture an observed public message, the source URL, and a bounded differentiation hypothesis. The ArchFlow wedge remains source-bound evidence, review gates, acceptance criteria, and task/knowledge handoff; it is an interpretation to test, not market proof.
