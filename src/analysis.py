import matplotlib.pyplot as plt
import seaborn as sns

def generate_visual_insights(df):
    """
    Generates core EDA plots for the technical report.
    """
    # Customizing the look so it doesn't look like default matplotlib
    sns.set_theme(style="ticks")
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: AQI Distribution
    sns.histplot(df['aqi_value'], bins=40, kde=True, ax=axes[0], color='#2a9d8f')
    axes[0].set_title('National AQI Distribution Density')

    # Plot 2: Ranking States (Horizontal bar is easier to read)
    avg_aqi = df.groupby('state')['aqi_value'].mean().sort_values(ascending=False).head(10)
    avg_aqi.plot(kind='barh', ax=axes[1], color='#e76f51')
    axes[1].set_title('Top 10 Most Polluted States (Mean AQI)')
    axes[1].invert_yaxis() # Highest on top

    plt.tight_layout()
    plt.savefig('outputs/aqi_insights.png', dpi=300)
    plt.close()