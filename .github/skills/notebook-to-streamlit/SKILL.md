---
name: notebook-to-streamlit
description: Reuse the analysis logic from the Rosa's Pizza notebook when building the Streamlit app.
---

# Notebook to Streamlit

Use the same calculation logic from the Jupyter Notebook in the Streamlit app.

When building the app:

- Import ZONES, TIME_BLOCKS, COSTS, and delivery_times from starter.
- Let the user select a delivery zone and time block.
- Let the user choose the range of promised delivery times.
- Let the user adjust refund cost, churn per late order, and profit margin.
- For each promised time, calculate total order profit and total late-order cost.
- Calculate net profit as total order profit minus total late-order cost.
- Recommend the promised delivery time with the highest net profit.
- Keep the Streamlit calculations consistent with the notebook.
