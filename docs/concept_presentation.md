# Crypto Hedge Fund Concept Presentation

For more description check corresponding notebooks, that are mentioned in
README.

## Content

1. [Hedge fund model](#hedge-fund-model)
2. [Risk management](#risk-management)
3. [Portfolio management](#portfolio-management)
4. [System architecture](#system-architecture) 


# Hedge fund model

Classical technical indicators can be applied on asset price and volume for 
market movement comprehension. 
ML models could be applied on stage for forecasting data, detecting risk. 
It's role is to detect profitable opportunities and adaptation to the 
market behavior.
For instance rule based model can be defined for managing portfolio and 
RFL model for fixing rule based model parameters over time. Also AI can solve
classification problems for detecting volatility regimes.
AI agents interact via an API or a common framework (for example, in Python with
libraries like Ray for multi-agent): forecasts from ML agents are fed into the 
MPT for daily portfolio rebalancing. If volatility is predicted to be high, the
agent can "advise" hedging (options or futures).

#### Resources
- [Technical indicators to go](https://www.investopedia.com/top-7-technical-analysis-tools-4773275)
- [Most common indicators](https://www.cryptohopper.com/ru/blog/the-5-most-used-technical-indicators-and-how-they-work-306)

# Risk management

The five principal risk measures include:
- Alpha - risk relative to the market or a selected benchmark index, 
- Beta - measures the volatility or systematic risk of a fund in comparison to
the market or the selected benchmark index, 
- R-squared - percentage of an investment's movement attributable to movements
in its benchmark index, 
- Standard deviation (volatility), 
- Sharpe ratio = $\frac{R_p - R_f}{\sigma_p}$, where $R_p$ - return of portfolio, $R_f$ - risk-free rate, $\sigma_p$ - standard divination of the portfolio's excess return. 

AI helps mitigate losses during high-volatility periods by enabling peeking
in the future (predictions) of asset price or liquidity. That knowledge
enables correction of weights in the portfolio. Using predictions
technical indicators can be applied and therefore signals "buy" or "sell"
to be obtained.

For assessing volatility I would use GARCH model, and for liquidity - trading volume.
As a ML models I would prefer to use random forest, XGBoost or Gradient Boosting, 
because of their simplicity in implementation.

---
#### Resources
- [Briefly about risk measures](https://www.investopedia.com/terms/r/riskmeasures.asp)
- [ML in mitigating volatility](https://superagi.com/mitigating-market-volatility-a-comparative-analysis-of-the-best-ai-risk-assessment-tools-for-financial-institutions-and-investors/)


# Portfolio management
The Modern portfolio theory (MPT) is a mathematical framework for assembling 
a portfolio of assets such that the expected return is maximized for a given 
level of volatility. It is a formalization of diversification in investing, 
i.e., the idea that owning different kinds of financial assets is less risky 
than owning one single asset. 

Traditional methods, such as the Markowitz mean-variance model (MPT), rely on 
statistical assumptions and linear relationships, which may not adequately
capture the complexities of financial markets. Given that these markets often 
exhibit non-linear dynamics and intricate interdependencies, Deep Learning (DL) 
emerges as a compelling alternative for portfolio optimization.

Another approach for example, an XGBoost or Random Forest agent predicts future returns, and 
GARCH predicts volatility; together, they produce a covariance matrix for 
Markowitz optimization. 
This is useful during the rebalancing phase (daily or hourly) to adapt to the market.
Adaptation can be achieved through classification of the volatility regime and
fixed time periods (based on the strategies horizons). 
Here multiple ML models are applicable: EM-algorithm, KNN, Random Forest.

---
#### Resources
- [Briefly about MPT](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)
- [Entertaining article about DL in MPT](https://www.faba.bg/index.php/faba/article/view/265)
- [Great notebook with MPT presentation](https://www.kaggle.com/code/yousefsaeedian/modern-portfolio-theory-mpt/notebook)

# System architecture

System should consist of several layers, consequently connected:
- Data fetching, cleansing, normalization
- Storage of data
- Exploratory data analysis and feature engineering (e.g. indicators)
- Risk management
- Portfolio management
- Serialization of models and server-side deployment.

Risk management module should be devoted to volatility forecasting. 
Portfolio management module should be connected with risk management module
for portfolio rebalancing.
After backtesting of those modules and models training, they should be wrapped
in docker container and sended to a server-side where can be accessible via API.
