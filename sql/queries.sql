-- 1 Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM "03_aum_by_fund_house"
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) AS avg_nav
FROM "02_nav_history";

-- 3 Monthly Average NAV
SELECT substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM "02_nav_history"
GROUP BY month;

-- 4 SIP YoY Growth
SELECT *
FROM "04_monthly_sip_inflows";

-- 5 Transactions by State
SELECT state,
COUNT(*) AS total_transactions
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_transactions DESC;

-- 6 Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM "07_scheme_performance"
WHERE expense_ratio_pct < 1;

-- 7 Top 10 Performing Funds
SELECT scheme_name, return_5yr_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 8 Average Return by Category
SELECT category,
AVG(return_5yr_pct)
FROM "07_scheme_performance"
GROUP BY category;

-- 9 Investor Count by KYC Status
SELECT kyc_status,
COUNT(*)
FROM "08_investor_transactions"
GROUP BY kyc_status;

-- 10 Portfolio Sector Allocation
SELECT sector,
SUM(weight_pct)
FROM "09_portfolio_holdings"
GROUP BY sector
ORDER BY SUM(weight_pct) DESC;