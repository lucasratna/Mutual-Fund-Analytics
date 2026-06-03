\# Mutual Fund Analytics Data Dictionary



\## 01\_fund\_master



| Column | Type | Description |

|----------|----------|----------|

| amfi\_code | INTEGER | AMFI Scheme Code |

| fund\_house | TEXT | Fund House Name |

| scheme\_name | TEXT | Mutual Fund Scheme |

| category | TEXT | Equity or Debt |

| sub\_category | TEXT | Large Cap, Mid Cap, etc |

| risk\_category | TEXT | Risk Level |



\## 02\_nav\_history



| Column | Type | Description |

|----------|----------|----------|

| amfi\_code | INTEGER | Scheme Code |

| date | DATE | NAV Date |

| nav | FLOAT | Net Asset Value |



\## 08\_investor\_transactions



| Column | Type | Description |

|----------|----------|----------|

| investor\_id | TEXT | Investor ID |

| transaction\_date | DATE | Transaction Date |

| transaction\_type | TEXT | SIP/Lumpsum/Redemption |

| amount\_inr | INTEGER | Transaction Amount |

| state | TEXT | State |

| city | TEXT | City |

| kyc\_status | TEXT | Verification Status |

