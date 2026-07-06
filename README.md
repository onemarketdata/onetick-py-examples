# onetick-py assistant knowledge base

This repo contains two different datasets:

- onetick-py documentation: `otp-generated-docs` folder
- manually written onetick-py examples: `dataset` folder

The `dataset` folder is split into two groups:

- common onetick-py examples (everything outside `dataset/surveillance`): generic API usage
  applicable to any onetick-py user — selecting time series, ticks creation, quotes/trades,
  tests, data inspection, utilities
- surveillance-specific examples (`dataset/surveillance`): documents that assume a surveillance
  product deployment and its databases — alerts fetching (`alerts_fetch`), client order flow
  (`order_flow`), and order-flow data-quality checks (`sanity_checks`)

This split lets consumers build an index from only the common group, or from common + surveillance.

Both used for [Support Assistant](https://gitlab.sol.onetick.com/solutions/py-onetick/support-assistant) and [Coding Assistant](https://gitlab.sol.onetick.com/solutions/ml-ops/coding-assistant) projects: projects use `llmbase.build_index` to load, embed and store documents in a DB.

## Automated update

Each Monday `onetick-py` CI/CD release a new version and builds up documentation.
One of CI/CD pipeline artifacts is a documentation built as markdown files and saved as zip.

In this repo we have a schedule (each Tuesday) to load these generated markdown filesб store to `otp-generated-docs` folder and then commit all changes.