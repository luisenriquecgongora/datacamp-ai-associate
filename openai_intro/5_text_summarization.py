import sys
sys.stdout.reconfigure(encoding="utf-8")

import os

from dotenv import load_dotenv
from openai import OpenAI

# Load variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to the .env file (never commit it)."
    )

# Create the OpenAI client
client = OpenAI(api_key=api_key)

finance_text = """
The Quiet Restructuring: How AI Reshaped Financial Work by 2026

By 2026, artificial intelligence has stopped being a line item in financial institutions' innovation budgets and become the operating fabric of the industry itself. The transformation did not arrive as a single disruptive event but as a steady reallocation of human attention away from mechanical tasks and toward judgment, relationships, and risk ownership.

From Processing to Supervising

The most visible change has occurred in the middle and back office. Reconciliation, trade settlement exception handling, invoice matching, and regulatory reporting — activities that once consumed thousands of analyst hours — are now largely executed by agentic AI systems that operate continuously rather than in batch cycles. The finance professional of 2026 spends less time producing numbers and more time interrogating them. Month-end close processes that took ten business days in 2022 now routinely complete in two or three, with human controllers acting as reviewers and escalation points rather than preparers.

This shift has redefined what "junior work" means. Entry-level analysts no longer cut their teeth on manual spreadsheet assembly; instead, they are trained from day one to specify, audit, and challenge machine-generated output. Firms that adapted their talent pipelines early report stronger retention, while those that simply eliminated junior roles are discovering an uncomfortable gap in their future leadership bench.

Advisory, Research, and the Premium on Judgment

In investment research and wealth management, AI has commoditized the first draft. Earnings summaries, comparable company screens, and portfolio commentary are generated in seconds, which has paradoxically raised the value of differentiated human insight. Clients no longer pay for information synthesis — they pay for conviction, contrarian framing, and accountability. Advisors equipped with AI copilots handle materially larger books of business, but the advisors who thrive are those who use the reclaimed time for deeper client conversations rather than simply scaling volume.

Credit analysis has followed a similar path. Underwriting models now ingest alternative data streams — real-time cash flow, supply chain signals, satellite and payments data — producing risk assessments that are faster and often more predictive than traditional methods. Yet regulators in the US, UK, and EU have made clear that explainability is non-negotiable, and "model risk management" has become one of the fastest-growing specializations in finance.

The New Risk Landscape

The gains have come with new exposures. Model concentration risk — many institutions relying on a small number of foundation model providers — is now a standing topic in board risk committees. AI-enabled fraud, particularly deepfake-driven payment authorization scams, has forced banks to invest heavily in verification infrastructure, and the arms race between generative attack tools and AI-powered detection defines much of the 2026 financial crime agenda.

Compliance functions, once seen as cost centers resistant to automation, have become sophisticated AI adopters. Transaction monitoring false-positive rates have fallen dramatically, and continuous auditing is replacing periodic sampling. Still, accountability remains stubbornly human: when an AI system errs, regulators fine the institution, not the algorithm.

The Bottom Line

The lesson of 2026 is that AI did not replace financial professionals — it repriced their skills. Routine cognitive labor has been devalued; judgment, ethical reasoning, client trust, and the ability to govern intelligent systems have appreciated sharply. The institutions winning this transition treated AI not as a headcount reduction tool but as a redeployment of human capital toward the work machines still cannot do: deciding what matters, and standing behind the decision.
"""

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=400
)

print(response.choices[0].message.content)