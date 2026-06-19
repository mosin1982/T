\# Multi-Language Developer Architecture



\*\*Project:\*\* T

\*\*Maintainer:\*\* T Technology Research Lab

\*\*Status:\*\* Public Alpha / Research Software



T is currently a Python-first financial research system. Future developer-language support may include Go, Rust, TypeScript, and WebAssembly extension layers.



```text

Research only. Not financial advice.

```



\## 1. Purpose



The purpose of multi-language developer architecture is to prepare T for long-term scalability without making the current public alpha repository confusing.



T should not become a random mixed-language repository. Each language must have a clear role.



\## 2. Current Core Language



The current core language is:



```text

Python

```



Python is used for:



\* Research logic

\* Backtesting

\* Scoring

\* Dashboard

\* CLI workflows

\* Tests

\* Safety guard

\* Data analysis



Python remains the main public alpha language.



\## 3. Architecture Principle



T should follow this principle:



```text

Python-first core with optional extension layers.

```



This means:



\* Python remains the main system.

\* Other languages should extend T, not replace it.

\* Each language must solve a real technical problem.

\* Empty or decorative language folders should be avoided.



\## 4. Planned Developer Language Roles



| Language         | Planned Role                                              |

| ---------------- | --------------------------------------------------------- |

| Python           | Core research engine, backtest engine, dashboard, CLI     |

| Go               | SDK, API client, fast connectors, deployment tools        |

| Rust             | Risk/scoring engine, validation, high-performance modules |

| TypeScript       | Future web dashboard and frontend interface               |

| WebAssembly      | Browser-side risk/scoring modules                         |

| SQL              | Data storage, reporting, query layer                      |

| Shell/PowerShell | Setup, local automation, deployment scripts               |



\## 5. Python Core



Python should continue to handle:



\* Backtest analytics

\* Research scoring

\* Dashboard logic

\* Safety guard

\* Report generation

\* Data workflows

\* Test automation



Current Python folders may include:



```text

backtest/

dashboard/

modes/

quality/

tests/

```



\## 6. Go Extension Layer



Go may be used later for:



\* Lightweight API clients

\* Data collectors

\* Fast CLI utilities

\* Deployment helpers

\* Microservices

\* Cloud-friendly connectors



Suggested future structure:



```text

sdk/

└─ go/

&#x20;  ├─ README.md

&#x20;  ├─ go.mod

&#x20;  └─ tclient.go

```



Go should only be added when there is a real SDK or connector use case.



\## 7. Rust Extension Layer



Rust may be used later for:



\* High-performance scoring

\* Risk validation

\* Data integrity checks

\* Safe numerical modules

\* WebAssembly compilation

\* Performance-critical research components



Suggested future structure:



```text

engines/

└─ rust-risk/

&#x20;  ├─ Cargo.toml

&#x20;  └─ src/

&#x20;     └─ lib.rs

```



Rust should be added carefully because it increases build and CI complexity.



\## 8. TypeScript Frontend Layer



TypeScript may be used later if T moves beyond Streamlit into a full web dashboard.



Possible future uses:



\* Web dashboard

\* Client-facing UI

\* API-driven frontend

\* Component-based analytics views

\* Multi-language UI support



Suggested future structure:



```text

web/

├─ package.json

├─ src/

└─ README.md

```



TypeScript should not replace Streamlit until the project needs a more advanced production-style interface.



\## 9. WebAssembly Layer



WebAssembly may be useful for:



\* Browser-side scoring

\* Fast local risk checks

\* Portable analytics modules

\* Rust-to-browser execution



Suggested future structure:



```text

wasm/

└─ risk-score/

```



WebAssembly should remain a future target, not an immediate public alpha requirement.



\## 10. CI Strategy



Each language adds tooling burden.



Future CI may include:



| Layer      | Tooling                       |

| ---------- | ----------------------------- |

| Python     | Black, Ruff, Pytest           |

| Go         | gofmt, go test                |

| Rust       | cargo fmt, cargo test, clippy |

| TypeScript | npm test, eslint, build       |

| Docs       | markdown lint optional        |



T should not add language CI until the corresponding language has real code.



\## 11. What Not To Do



Avoid:



\* Empty Go/Rust folders with no purpose

\* Adding languages for marketing only

\* Overcomplicated CI before core stability

\* Replacing Python too early

\* Mixing responsibilities across languages

\* Claiming production readiness too early



\## 12. Recommended Roadmap



Recommended order:



```text

Step 1: Python core stable

Step 2: Documentation for future architecture

Step 3: Go SDK skeleton only when API/client need exists

Step 4: Rust scoring/risk module only when performance need exists

Step 5: TypeScript dashboard only when Streamlit is no longer enough

Step 6: WebAssembly only for browser-side scoring modules

```



\## 13. Current Position



For the current public alpha:



```text

Python is the only required development language.

```



Other languages are planned extension layers.



\## 14. Official Positioning



Correct positioning:



```text

T is a Python-first financial research OS with planned Go, Rust, TypeScript, and WebAssembly extension layers.

```



Avoid:



```text

T is already a full multi-language production platform.

```



\## 15. Disclaimer



T remains research-only software across all language layers.



```text

Research only. Not financial advice.

```



━━━━━━━━━━━━━━━━━━━━

T

T Technology Research Lab

━━━━━━━━━━━━━━━━━━━━



