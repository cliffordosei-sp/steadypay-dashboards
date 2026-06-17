import streamlit as st
from apps import APPS

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Steadypay Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Styles ───────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Base */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #f7f4fa;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stAppViewContainer"] > .main > div {
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }
    [data-testid="stSidebar"] { display: none; }
    header[data-testid="stHeader"] { background: transparent; }

    /* Header */
    .hub-header {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 0.25rem;
    }
    .hub-logo {
        width: 44px;
        height: 44px;
        background: #1D9E75;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        flex-shrink: 0;
    }
    .hub-title {
        font-size: 1.75rem;
        font-weight: 700;
        color: #1a0a1e;
        letter-spacing: -0.02em;
        margin: 0;
    }
    .hub-subtitle {
        color: #6b5c72;
        font-size: 0.95rem;
        margin-top: 0.15rem;
        margin-bottom: 2rem;
    }

    /* Divider */
    .hub-divider {
        height: 1px;
        background: #e0d9e8;
        margin: 0.5rem 0 2rem 0;
    }

    /* App cards */
    .app-card {
        background: #ffffff;
        border: 1px solid #e8e2f0;
        border-radius: 14px;
        padding: 1.4rem 1.5rem 1.3rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
        transition: box-shadow 0.18s ease, border-color 0.18s ease;
        position: relative;
        overflow: hidden;
    }
    .app-card:hover {
        box-shadow: 0 6px 24px rgba(29, 158, 117, 0.10);
        border-color: #1D9E75;
    }
    .card-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 8px;
    }
    .card-icon {
        font-size: 2rem;
        line-height: 1;
    }
    .card-tag {
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #1D9E75;
        background: #e8f7f1;
        border-radius: 6px;
        padding: 3px 8px;
        white-space: nowrap;
    }
    .card-name {
        font-size: 1.05rem;
        font-weight: 600;
        color: #1a0a1e;
        margin: 0;
        line-height: 1.3;
    }
    .card-desc {
        font-size: 0.85rem;
        color: #6b5c72;
        line-height: 1.5;
        flex-grow: 1;
        margin: 0;
    }
    .card-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 0.4rem;
    }
    .status-live {
        display: flex;
        align-items: center;
        gap: 5px;
        font-size: 0.75rem;
        color: #1D9E75;
        font-weight: 500;
    }
    .status-live::before {
        content: '';
        width: 7px;
        height: 7px;
        background: #1D9E75;
        border-radius: 50%;
        display: inline-block;
    }
    .status-dev {
        display: flex;
        align-items: center;
        gap: 5px;
        font-size: 0.75rem;
        color: #b08a00;
        font-weight: 500;
    }
    .status-dev::before {
        content: '';
        width: 7px;
        height: 7px;
        background: #f0c000;
        border-radius: 50%;
        display: inline-block;
    }
    .status-coming_soon {
        display: flex;
        align-items: center;
        gap: 5px;
        font-size: 0.75rem;
        color: #9b8ca5;
        font-weight: 500;
    }
    .status-coming_soon::before {
        content: '';
        width: 7px;
        height: 7px;
        background: #c8b8d4;
        border-radius: 50%;
        display: inline-block;
    }
    .open-btn {
        font-size: 0.78rem;
        font-weight: 600;
        color: #1D9E75;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .open-btn:hover { text-decoration: underline; }

    /* Section label */
    .section-label {
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #9b8ca5;
        margin-bottom: 0.85rem;
    }

    /* Coming soon overlay */
    .app-card.coming-soon {
        opacity: 0.6;
        pointer-events: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hub-header">
        <div class="hub-logo">⚡</div>
        <h1 class="hub-title">Steadypay Hub</h1>
    </div>
    <p class="hub-subtitle">Internal tools & dashboards — click any card to open the app.</p>
    <div class="hub-divider"></div>
    """,
    unsafe_allow_html=True,
)

# ── Split apps by status ──────────────────────────────────────────────────────
live_apps = [a for a in APPS if a["status"] in ("live", "dev")]
coming_apps = [a for a in APPS if a["status"] == "coming_soon"]

STATUS_LABELS = {
    "live": "Live",
    "dev": "In development",
    "coming_soon": "Coming soon",
}

def render_card(app: dict) -> str:
    tag = app.get("tag", "")
    status = app.get("status", "live")
    status_label = STATUS_LABELS.get(status, status)
    is_coming = status == "coming_soon"
    card_class = "app-card coming-soon" if is_coming else "app-card"
    link_html = (
        f'<a class="open-btn" href="{app["url"]}" target="_blank">Open ↗</a>'
        if not is_coming
        else '<span class="open-btn" style="color:#c8b8d4">Coming soon</span>'
    )
    return f"""
    <div class="{card_class}">
        <div class="card-top">
            <span class="card-tag">{tag}</span>
        </div>
        <p class="card-name">{app["name"]}</p>
        <p class="card-desc">{app["description"]}</p>
        <div class="card-footer">
            <span class="status-{status}">{status_label}</span>
            {link_html}
        </div>
    </div>
    """

# ── Live / dev apps ───────────────────────────────────────────────────────────
if live_apps:
    st.markdown('<p class="section-label">Apps</p>', unsafe_allow_html=True)
    cols = st.columns(3, gap="medium")
    for i, app in enumerate(live_apps):
        with cols[i % 3]:
            st.markdown(render_card(app), unsafe_allow_html=True)

# ── Coming soon ───────────────────────────────────────────────────────────────
if coming_apps:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-label">Coming soon</p>', unsafe_allow_html=True)
    cols = st.columns(3, gap="medium")
    for i, app in enumerate(coming_apps):
        with cols[i % 3]:
            st.markdown(render_card(app), unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <br><br>
    <div style="text-align:center; color:#c8b8d4; font-size:0.78rem;">
        Steadypay internal tools · not for external distribution
    </div>
    """,
    unsafe_allow_html=True,
)
