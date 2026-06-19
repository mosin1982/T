\# Market Coverage



\*\*Project:\*\* T

\*\*Maintainer:\*\* T Technology Research Lab

\*\*Status:\*\* Public Alpha / Research Software



T is designed as a research-only Financial Intelligence Operating System. Market coverage should be added gradually through modular research adapters, not through unsafe live-trading promises.



```text

Research only. Not financial advice.

```



\## 1. Purpose



The purpose of market coverage documentation is to clearly define which markets T may study, which markets are planned, and which features are intentionally disabled or limited for safety.



Different markets have different:



\* Data structures

\* Trading hours

\* Risk profiles

\* Liquidity conditions

\* Tax rules

\* Exchange rules

\* Broker terms

\* Regulatory requirements

\* Regional restrictions



T does not determine whether a user is legally permitted to access, analyze, trade, or act in any market.



\## 2. Current Market Status



Current public alpha status:



| Market                   | Status                  | Execution |

| ------------------------ | ----------------------- | --------- |

| Demo/sample market data  | Research-ready          | Disabled  |

| Crypto-style sample data | Research/backtest-ready | Disabled  |

| Live crypto execution    | Not enabled by default  | Disabled  |

| Indian equities          | Planned research mode   | Disabled  |

| US equities              | Planned research mode   | Disabled  |

| Forex                    | Planned research mode   | Disabled  |

| Commodities              | Planned research mode   | Disabled  |

| Options/Futures          | Future research only    | Disabled  |



\## 3. Market Status Labels



T should use safe market status labels.



Recommended labels:



\* Research-ready

\* Backtest-ready

\* Observation-ready

\* Planned

\* Experimental

\* Disabled by default

\* Human review required



Avoid labels such as:



\* Trading-ready

\* Profit-ready

\* Signal-ready

\* Auto-earning ready

\* Fully advisory

\* Fully compliant for all markets



\## 4. Current Recommended Scope



For the current public alpha direction, T should focus on:



```text

Demo data

Crypto-style research data

Backtest analytics

Dashboard visualization

Research-only output

Human-reviewed interpretation

```



This keeps the system focused and avoids unsafe overreach.



\## 5. Planned Market Adapters



Future market adapter structure may use:



```text

markets/

├─ crypto/

│  ├─ rules.py

│  ├─ schema.py

│  └─ README.md

├─ india\_equity/

│  ├─ rules.py

│  ├─ schema.py

│  └─ README.md

├─ us\_equity/

│  ├─ rules.py

│  ├─ schema.py

│  └─ README.md

├─ forex/

│  ├─ rules.py

│  ├─ schema.py

│  └─ README.md

└─ commodities/

&#x20;  ├─ rules.py

&#x20;  ├─ schema.py

&#x20;  └─ README.md

```



Each adapter should define:



\* Market name

\* Asset type

\* Data schema

\* Timezone

\* Trading/session hours where applicable

\* Risk warning

\* Research-only disclaimer

\* Execution status

\* Compliance notes

\* Required data fields



\## 6. Crypto Research Mode



Crypto may be the first practical research market because:



\* It is active 24/7

\* Public APIs are widely available

\* Demo data is easier to create

\* Volume and sentiment research can be tested

\* Dashboard demos are easier to explain



However, crypto is also highly volatile and risky. T must not present crypto research as financial advice or as a return-assurance system.



\## 7. Indian Equity Research Mode



Indian equity research may be valuable for local users and small teams.



Future Indian equity support should remain:



\* Research-only

\* Backtest-focused

\* Dashboard-focused

\* Human-reviewed

\* Execution disabled by default



Users are responsible for understanding and following applicable Indian laws, exchange rules, broker terms, tax rules, and regulations.



\## 8. US Equity Research Mode



US equity research may improve global credibility and developer interest.



Future US equity support should remain:



\* Research-only

\* Data-provider aware

\* Broker-neutral

\* Human-reviewed

\* Execution disabled by default



Users are responsible for applicable local, exchange, data-provider, broker, and tax rules.



\## 9. Forex and Commodities



Forex and commodities may be added later as research modes.



These markets may involve:



\* Leverage

\* Regional restrictions

\* Different trading sessions

\* High volatility

\* Complex broker terms

\* Different data-provider rules



T should treat these as planned or experimental research areas until proper documentation and testing exist.



\## 10. Options and Futures



Options and futures are complex and high-risk instruments.



T should not prioritize these in early public alpha releases.



Future support should be:



\* Research-only

\* Risk-focused

\* Backtest-focused

\* Human-reviewed

\* Clearly marked as advanced

\* Execution disabled by default



\## 11. Execution Policy



Default policy:



```text

Execution disabled by default.

```



T should not enable live execution unless there is a separate, reviewed, documented, and clearly scoped module.



Even if execution modules exist in the future, they should not change the core project positioning:



```text

Research only. Not financial advice.

```



\## 12. Compliance Responsibility



T does not provide legal, tax, compliance, investment, or trading advice.



Users are responsible for:



\* Local laws

\* Tax obligations

\* Exchange rules

\* Broker terms

\* Data-provider terms

\* Regional restrictions

\* Suitability and risk review

\* Human decision-making



\## 13. Safe Market Statement



Recommended official statement:



```text

T provides research infrastructure for studying market data through backtesting, dashboards, and safety-guarded research output. It does not provide financial advice, investment advice, trade recommendations, portfolio management, or execution services by default.

```



\## 14. Future Roadmap



Planned market roadmap:



```text

Step 1: Demo/sample research data

Step 2: Crypto-style research adapter

Step 3: Indian equity research adapter

Step 4: US equity research adapter

Step 5: Forex and commodities research adapters

Step 6: Advanced instruments research notes

Step 7: Compliance-aware market policy layer

```



\## 15. Disclaimer



T remains research-only software across all market contexts.



```text

Research only. Not financial advice.

```



Users are responsible for reviewing outputs, validating assumptions, and following applicable laws, exchange rules, broker terms, tax rules, and regulations.



━━━━━━━━━━━━━━━━━━━━

T

T Technology Research Lab

━━━━━━━━━━━━━━━━━━━━



