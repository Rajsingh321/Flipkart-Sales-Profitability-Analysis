import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Flipkart Sales Analysis | Raj Singh", layout="wide")

# --- Custom Title ---
st.markdown("""
    <h1 style='text-align: center; font-size: 42px; color: #262730;'>
        📊 Flipkart Sales & Profitability Analysis
    </h1>
    <h3 style='text-align: center; font-weight: 400; color: #555;'>
        Stopping Revenue Leakage and Driving Smarter E-commerce Growth
    </h3>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Problem Statement ---
st.markdown("## 🧩 Problem Statement", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
Flipkart offers thousands of products but not all of them are profitable.<br>  
Many products have deeply negative margins, and high discounting often leads to losses. Meanwhile, categories like Technology are highly profitable but under-leveraged.<br>
<b>The problem:</b> How can Flipkart use its own data to:<br>
-Stop profit leakage<br>
-Invest more in high-margin categories<br>
-Optimize pricing and discount strategy
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Objective ---
st.markdown("## 🎯 Objective", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
Use data analytics to:<br>
- Uncover category and product-level performance patterns<br>
- Identify loss-making products and discount thresholds<br>
- Track growth trends over time<br>
- Support smarter decisions in pricing, promotion, and inventory</li>
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Dataset Overview ---
st.markdown("## 🗃 Dataset Overview", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>         
- 38,000+ transactions<br>
- ₹2M+ total sales<br>              
- 286K total profit<br>              
- 3 main categories: Technology, Furniture, Office Supplies<br>
- Time range: 2014–2017  
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Analysis Process ---
with st.container():

    st.markdown("""
    <style>
    .centered-download {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        align-items: center;        
    }
    div.stDownloadButton > button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 5px;
    }
    div.stDownloadButton > button:hover {
        background-color: #0056b3;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


    st.markdown("## 🔍 Data Analysis Process", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    # --- Data Analysis ---
    with col1:
        st.markdown("""
            <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
                <div style='font-size: 36px;'>📊</div>
                <h4 style='margin-top: 10px;'>Data Analysis</h4>
                <p style='color: #555; font-size: 20px;'>
                    Skilled in transforming raw data into actionable insights through cleaning, exploration, and visualization.
                </p>
            </div>
        """, unsafe_allow_html=True)
        with open("flipkart/notebooks/collection and cleaning.ipynb", "rb") as f:
            st.download_button("See Code", f, file_name="flipkart_clean_&_format.ipynb", key="clean_data_download")

    # --- Dashboard Creation ---
    with col2:
        st.markdown("""
            <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
                <div style='font-size: 36px;'>📈</div>
                <h4 style='margin-top: 10px;'>Dashboard Creation</h4>
                <p style='color: #555; font-size: 20px;'>Experienced in building clean, executive-level dashboards using Power BI for strategic decision-making.</p>
            </div>
        """, unsafe_allow_html=True)
        with open("files/flipkart_dashbord_presentation.pptx", "rb") as f:
            st.download_button("See Dashboard", f, file_name="flipkart_dashboard_presentation.pptx", key="dash_download")

    # --- Business Insights ---
    with col3:
        st.markdown("""
            <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
                <div style='font-size: 36px;'>💡</div>
                <h4 style='margin-top: 10px;'>Business Insights</h4>
                <p style='color: #555; font-size: 20px;'>Focused on delivering insights that solve business problems and drive growth using real-world datasets.</p>
            </div>
        """, unsafe_allow_html=True)
        with open("notebooks/pandas_01.ipynb", "rb") as f:
            st.download_button("See Code", f, file_name="flipkart_analyze.ipynb", key="data_analyze_download")

    # --- Data Storytelling ---
    with col4:
        st.markdown("""
            <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
                <div style='font-size: 36px;'>🗣</div>
                <h4 style='margin-top: 10px;'>Data Storytelling</h4>
                <p style='font-size: 20px; color: #555;'>
                Strong presentation and communication skills. Use Power BI dashboards to explain insights clearly and drive decisions.
                </p>
            </div>
        """, unsafe_allow_html=True)
        with open("files/flipkart_data_analysis_Presentation1.pptx", "rb") as f:
            st.download_button("See Presentation", f, file_name="flipkart_data_analysis_presentation.pptx", key="story_download")

# --- Key Insights ---
st.markdown("## 📊 Key Insights", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
✅ <b>20+ products</b> have margins below <b>-270%</b> → must be cut or renegotiated<br>
💰 <b>Technology</b> = 47% of total profit → invest more in this category<br>            
⛔ <b>Discounts above 30%</b> consistently lead to losses → cap discounts<br>            
📈 <b>Copiers, Phones, Accessories</b> are highest-margin sub-categories → prioritize<br>
📅 Sales peak in <b>March, September, November</b> → plan ahead for campaigns  
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Visuals ---
st.markdown("## 📸 Dashboard Visuals", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
Visualized in a 4-slide Power BI dashboard:
</p>
<p style='font-size: 20px;'>                        
- Sales and profit trends<br>
- Discount impact analysis<br>
-Profitability by sub-category<br>
- Monthly performance trends<br>
</p>
""", unsafe_allow_html=True)

#bussiness recommendation
col1, col2 = st.columns(2)
with col1:
    st.image("data/flipkart_dashboard_1.jpg", caption="Slide 1: Overall Metrics", use_column_width=True)
    st.image("data/flipkart_dashboard_3.jpg", caption="Slide 3: Discount vs Profit", use_column_width=True)

with col2:
    st.image("data/flipkart_dashboard_2.jpg", caption="Slide 2: Top vs Bottom Products", use_column_width=True)
    st.image("data/flipkart_dashboard_4.jpg", caption="Slide 4: Time Series Analysis", use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## 📌 Business Recommendations", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
                <p
                style='font-size: 25px;'>               
    1. Immediately remove or fix 20+ SKUs causing negative margin drag<br>                  
    2. Prioritize Technology category through homepage, ads, and strategic discounting<br>
    3. Limit discounts to <30% across loss-sensitive categories <br>                  
    4. Bundle high-margin categories (like Phones + Accessories) to increase AOV  
    </p>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
                <p
                style='font-size: 25px;'>
    5. Use seasonality trends to guide Q1 and Q3 inventory planning<br>
    6. Monitor monthly dashboard reports to track progress and prevent margin erosion<br>  
    7. Invest in pricing automation that reacts to real profit behavior, not sales pressure<br>  
    8. Apply insights to test private label pricing strategies before full rollout
    </p>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Conclusion ---
st.markdown("## 🧠 Conclusion", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 25px; text-align: justify;'>
This project tackled a core operational issue in e-commerce: Flipkart, like many platforms, offers thousands of products — but not all drive value.  
The problem lies in hidden revenue leakage caused by excessive discounting, poor pricing control, and overlooked product categories that consistently lose money.<br>
To solve this, I collected order-level data, cleaned and transformed it, and built a multi-slide Power BI dashboard that gave product, sales, and category teams real visibility  
From margin outliers to category performance, I uncovered where the business is bleeding profit and where it can confidently scale.  
Dashboards and KPIs were engineered to guide immediate action — identifying loss-making SKUs, high-potential sub-categories, seasonal patterns, and actionable discount caps.<br>
The result is a clear, data-backed case for smarter pricing, stronger product lifecycle management, and smarter campaign timing.  
This isn't just analysis — it's business guidance, built from the ground up.
</p>
""", unsafe_allow_html=True)

st.markdown("### 🔑 Key Takeaways", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 25px;'>
- Over 20 products were found to have consistent losses with margins worse than -270%, showing urgent need for cost review or removal<br>  
- Technology category alone contributes 47% of total profit but was not proportionately promoted — a missed opportunity for scalable growth<br>  
- Discount levels above 30% sharply correlate with profit decline, indicating a ceiling beyond which discounting erodes business value<br>  
- Copiers, Phones, and Accessories are the most efficient categories — high sales, high profit, low discount impact<br>  
- Monthly sales spikes in March, September, and November point to clear seasonality patterns that should guide inventory and campaign timing<br>  
- Combining financial KPIs with visual dashboards empowers even non-technical teams to make fast, informed business decisions
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## 🛠 Tools & Contact", unsafe_allow_html=True)

tool_col, contact_col = st.columns(2)

with tool_col:
    st.markdown("""
    <p style='font-size: 25px;'>
    - Python: pandas, data cleaning, preprocessing<br>  
    - Power BI:multi-slide dashboards, slicers, DAX KPIs<br>  
    - Skills: margin optimization, sales segmentation, discount elasticity, category analytics  
    </p>
    """, unsafe_allow_html=True)

with contact_col:
    st.markdown(""" 
    <p style='font-size: 25px;'>                
    📧 Email: <b>rajbgi377@gmail.com</b><br>
    🔗 <a href="https://www.linkedin.com/in/rajsinghsendhav" target="_blank">LinkedIn Profile</a><br>
    📁 <a href="https://yourwebsite.com/resume.pdf" target="_blank">Download Resume</a>
    </p>
    """, unsafe_allow_html=True)
