import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Department": [
        "Water Supply",
        "Sewerage",
        "Maintenance",
        "Administration"
    ],
    "Budget": [400000, 250000, 200000, 150000]
})

# Create interactive pie chart
fig = px.pie(
    df,
    names="Department",
    values="Budget",
    title="AAWSA Department Budget Distribution",
    hole=0.35,  # Donut effect
    color_discrete_sequence=px.colors.qualitative.Set2,
    hover_data=["Budget"]
)

fig.update_traces(
    textposition="inside",
    textinfo="label+percent",
    pull=[0.08, 0, 0, 0],
    hovertemplate=(
        "<b>%{label}</b><br>"
        "Budget: %{value:,.0f}<br>"
        "Share: %{percent}"
        "<extra></extra>"
    )
)

fig.update_layout(
    title_x=0.5,
    template="plotly_white"
)

fig.show()
