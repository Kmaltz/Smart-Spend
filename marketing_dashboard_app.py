import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
data = {
    'Channel': ['Google Ads', 'Facebook Ads', 'Email Marketing', 'SEO', 'Events', 'Influencer Marketing'],
    'Spend ($)': [4000, 2500, 1000, 1500, 2000, 1000],
    'Leads': [160, 300, 220, 180, 90, 60],
    'Sales': [30, 45, 40, 36, 15, 12],
    'Revenue ($)': [4800, 6750, 7200, 6480, 3000, 2400]
}

df = pd.DataFrame(data)
df['Cost per Lead ($)'] = df['Spend ($)'] / df['Leads']
df['Cost per Sale ($)'] = df['Spend ($)'] / df['Sales']
df['ROI (Revenue/Spend)'] = df['Revenue ($)'] / df['Spend ($)']

st.title("📊 Marketing Spending Analysis Dashboard")

st.markdown("## Channel Performance Overview")
st.dataframe(df.style.format({'Spend ($)': '${:,.2f}', 'Revenue ($)': '${:,.2f}',
                              'Cost per Lead ($)': '${:,.2f}', 'Cost per Sale ($)': '${:,.2f}', 
                              'ROI (Revenue/Spend)': '{:.2f}x'}))

st.markdown("## ROI by Channel")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x='ROI (Revenue/Spend)', y='Channel', palette='viridis', ax=ax)
ax.set_title('ROI by Marketing Channel')
st.pyplot(fig)

st.markdown("## Recommendations")
top_roi = df.sort_values('ROI (Revenue/Spend)', ascending=False).iloc[0]
low_roi = df.sort_values('ROI (Revenue/Spend)').iloc[0]

st.success(f"📈 Consider increasing budget for **{top_roi['Channel']}** (ROI: {top_roi['ROI (Revenue/Spend)']:.2f}x)")
st.warning(f"📉 Consider reducing spend on **{low_roi['Channel']}** (ROI: {low_roi['ROI (Revenue/Spend)']:.2f}x)")