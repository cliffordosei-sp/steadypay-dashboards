"""
Apps registry — add or remove entries here to control what appears on the hub.
Each entry is a dict with the following keys:
  - name:        Display name of the app
  - description: One-line description shown on the card
  - url:         Full URL to the app (Cloud Run URL or localhost for dev)
  - icon:        Emoji used as the card icon
  - tag:         Short category label, e.g. "Marketing", "Ops", "Risk"
  - status:      "live" | "dev" | "coming_soon"
"""

APPS = [
    {
        "name": "CashWave Marketing Dashboard",
        "description": "Acquisition, channel performance, onboarding funnel, and risk model overview for CashWave D2C.",
        "url": "https://cashwave-dashboard-791218390362.europe-west2.run.app/",
        "tag": "Marketing",
        "status": "live",
    },
    # {
    #     "name": "Partner Approvals",
    #     "description": "Review and approve partner applications and loan configurations.",
    #     "url": "https://your-partner-approvals-url.run.app",  # ← replace
    #     "icon": "🤝",
    #     "tag": "Ops",
    #     "status": "live",
    # },
    # ── Add more apps below ──────────────────────────────────────────────────
    # {
    #     "name": "My New App",
    #     "description": "What it does.",
    #     "url": "https://...",
    #     "icon": "🔍",
    #     "tag": "Risk",
    #     "status": "dev",
    # },
]
