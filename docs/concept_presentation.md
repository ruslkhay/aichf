# Crypto Hedge Fund Concept Presentation

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
RFL model for fixing rule based model parameters over time. 

---
#### Resources
- https://www.investopedia.com/top-7-technical-analysis-tools-4773275
- https://www.cryptohopper.com/ru/blog/the-5-most-used-technical-indicators-and-how-they-work-306

# Risk management
The five principal risk measures include:
- alpha, 
- beta, 
- R-squared, 
- standard deviation, 
- Sharpe ratio. 

AI helps mitigate losses during high-volatility periods by enabling peeking
in the future (predictions) of asset price or liquidity. Using predictions
technical indicators can be applied and therefore signals "buy" or "sell"
to be obtained.

For assessing volatility I would use GARCH model, and for liquidity - trading volume.
As a ML models I prefer to use random forest, XGBoost or Gradient Boosting, 
because of their simplicity in implementation.

---
#### Resources
- https://www.investopedia.com/terms/r/riskmeasures.asp
- [ML in mitigating](https://superagi.com/mitigating-market-volatility-a-comparative-analysis-of-the-best-ai-risk-assessment-tools-for-financial-institutions-and-investors/)


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

---
#### Resources
- https://www.investopedia.com/terms/m/modernportfoliotheory.asp
- https://www.faba.bg/index.php/faba/article/view/265/137#info


# System architecture
