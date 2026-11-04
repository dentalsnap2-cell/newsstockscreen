
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import html

st.set_page_config(
    page_title="NewsDesk Studio",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------
# DEFAULT NEWS STORY
# --------------------------------

DEFAULTS = {
    "headline": "INDIA'S ECONOMY IN FOCUS",
    "subheadline": "SPECIAL REPORT | ECONOMIC OUTLOOK",
    "ticker": "BREAKING NEWS  •  INDIA'S ECONOMY IN FOCUS",
    "metric1_name": "GDP GROWTH",
    "metric1_value": "6.8%",
    "metric2_name": "INFLATION",
    "metric2_value": "4.2%",
    "metric3_name": "UNEMPLOYMENT",
    "metric3_value": "5.1%",
    "metric4_name": "MARKET INDEX",
    "metric4_value": "24,500",
    "report": (
        "India's economic outlook remains in focus. "
        "This illustrative report demonstrates how a news "
        "presenter can display data and explain the story."
    ),
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


def safe(value):
    """Escape user-entered text before displaying it in HTML."""
    return html.escape(str(value))


# --------------------------------
# BROADCAST DESIGN
# --------------------------------

st.markdown("""
<style>
.stApp {
    background: #07101c;
    color: white;
}

header[data-testid="stHeader"] {
    background: #07101c;
}

section[data-testid="stSidebar"] {
    background: #101c2d;
}

.news-topbar {
    background: #14243a;
    padding: 10px 18px;
    border-bottom: 4px solid #e63946;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.news-brand {
    font-size: 20px;
    font-weight: 900;
    color: white;
}

.news-live {
    color: #ff4c5b;
    font-weight: bold;
    font-size: 15px;
}

.news-headline {
    background: #14243a;
    padding: 22px;
    margin-top: 12px;
    border-left: 8px solid #e63946;
}

.news-headline h1 {
    color: white;
    font-size: clamp(28px, 4vw, 58px);
    font-weight: 900;
    line-height: 1.1;
    margin: 0;
}

.news-subheadline {
    color: #b7c8dd;
    font-size: 18px;
    margin-top: 12px;
}

.news-metric {
    background: #14243a;
    border-bottom: 4px solid #e63946;
    padding: 20px;
    min-height: 115px;
}

.metric-label {
    color: #a8bdd6;
    font-size: 15px;
    font-weight: bold;
}

.metric-value {
    color: white;
    font-size: clamp(28px, 3vw, 42px);
    font-weight: 900;
}

.news-report {
    background: #14243a;
    border-radius: 8px;
    padding: 22px;
    color: white;
    font-size: 20px;
    line-height: 1.6;
    min-height: 250px;
}

.news-ticker {
    background: #e63946;
    color: white;
    font-size: 20px;
    font-weight: 900;
    padding: 12px 20px;
    margin-top: 12px;
}

.broadcast-footer {
    color: #9eb3cc;
    font-size: 12px;
    text-align: right;
    padding: 8px;
}

div.stButton > button {
    background: #e63946;
    color: white;
    border: none;
    font-weight: bold;
    border-radius: 6px;
}

div.stButton > button:hover {
    background: #c92d3a;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------
# CHART BUILDER
# --------------------------------

def create_chart():
    data = pd.DataFrame({
        "Year": ["2021", "2022", "2023", "2024", "2025"],
        "Growth": [8.7, 7.0, 7.6, 6.5, 6.8]
    })

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=data["Year"],
            y=data["Growth"],
            marker_color="#e63946",
            text=data["Growth"],
            textposition="outside"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#07101c",
        plot_bgcolor="#07101c",
        font=dict(color="white"),
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis_title="Growth (%)",
        xaxis_title="Year",
        showlegend=False
    )

    return fig


# --------------------------------
# BROADCAST SCREEN
# --------------------------------

def show_broadcast():

    st.markdown("""
    <div class="news-topbar">
        <div class="news-brand">
            NEWS DESK STUDIO
        </div>
        <div class="news-live">
            ● LIVE NEWS
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="news-headline">
            <h1>{safe(st.session_state.headline)}</h1>
            <div class="news-subheadline">
                {safe(st.session_state.subheadline)}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    columns = st.columns(4)

    for i, column in enumerate(columns, start=1):

        name = safe(
            st.session_state[f"metric{i}_name"]
        )

        value = safe(
            st.session_state[f"metric{i}_value"]
        )

        with column:
            st.markdown(
                f"""
                <div class="news-metric">
                    <div class="metric-label">{name}</div>
                    <div class="metric-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    left, right = st.columns([1.4, 1])

    with left:
        st.markdown(
            "### ECONOMIC DATA | SAMPLE CHART"
        )

        st.plotly_chart(
            create_chart(),
            use_container_width=True,
            config={
                "displayModeBar": False,
                "responsive": True
            }
        )

    with right:
        st.markdown("### SPECIAL REPORT")

        st.markdown(
            f"""
            <div class="news-report">
                {safe(st.session_state.report)}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="news-ticker">
            {safe(st.session_state.ticker)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="broadcast-footer">
            NEWS DESK STUDIO | SAMPLE DATA
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------
# APPLICATION ROUTING
# --------------------------------

view = st.query_params.get("view", "control")

if view == "broadcast":

    show_broadcast()

    # Return to the newsroom editor
    if st.button("← Return to Control Room"):
        st.query_params["view"] = "control"
        st.rerun()

else:

    # --------------------------------
    # CONTROL ROOM
    # --------------------------------

    st.title("📺 NewsDesk Studio")

    st.caption(
        "NEWSROOM CONTROL ROOM | GRAPHICS EDITOR"
    )

    st.markdown(
        "Edit the content below. "
        "Your changes will appear in Broadcast Mode."
    )

    with st.sidebar:

        st.header("Newsroom Editor")

        st.subheader("Headline")

        st.text_input(
            "Main headline",
            key="headline"
        )

        st.text_input(
            "Subheadline",
            key="subheadline"
        )

        st.text_input(
            "News ticker",
            key="ticker"
        )

        st.divider()

        st.subheader("Data Graphics")

        for i in range(1, 5):

            st.text_input(
                f"Metric {i} label",
                key=f"metric{i}_name"
            )

            st.text_input(
                f"Metric {i} value",
                key=f"metric{i}_value"
            )

        st.divider()

        st.subheader("News Report")

        st.text_area(
            "Report content",
            key="report",
            height=200
        )

        if st.button("Reset Sample Story"):

            for key, value in DEFAULTS.items():
                st.session_state[key] = value

            st.rerun()

    # Preview
    st.subheader("Broadcast Preview")

    show_broadcast()

    st.divider()

    if st.button(
        "▶ OPEN BROADCAST MODE",
        use_container_width=True
    ):

        st.query_params["view"] = "broadcast"
        st.rerun()

    st.caption(
        "For a clean television display, use your "
        "browser's full-screen mode (F11)."
    )
