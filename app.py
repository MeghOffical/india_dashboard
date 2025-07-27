# load the libraries
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px



# title of sidebar 
st.sidebar.title("India Intelligence Dashboard")

# option available
option = st.sidebar.selectbox("Select a option", ['Home', 'Census Data', 'Crime Data', 'Health and Nutrition Data', 'Budget Data'])


if option == 'Home':
    html = """
    <!-- load font + icons -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">

    <style>
      body { margin:0; padding:0; font-family:'Poppins',sans-serif; background: #0f2027; }
      .container { max-width:1200px; margin: auto; padding:50px 20px; }
      .title { text-align:center; font-size:3rem; color:#00ffc3; margin-bottom:10px; text-shadow:1px 1px 2px #000; }
      .subtitle { text-align:center; font-size:1.2rem; color:#ccc; margin-bottom:40px; }
      .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:30px; }
      .card {
        background: rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.2);
        backdrop-filter:blur(10px);
        border-radius:20px;
        padding:30px 20px;
        text-align:center;
        transition:transform .3s, box-shadow .3s, border-color .3s;
        color:#fff;
      }
      .card:hover {
        transform:translateY(-10px);
        box-shadow:0 12px 24px rgba(0,255,195,0.2);
        border-color:#00ffc3;
      }
      .card i { font-size:2.5rem; margin-bottom:15px; color:#00ffc3; }
      .card h3 { margin-bottom:10px; font-size:1.3rem; }
      .card p { font-size:0.9rem; color:#ddd; line-height:1.4; }
      .footer { text-align:center; margin-top:50px; color:#888; font-size:0.85rem; }
      @media(max-width:600px){
        .title { font-size:2.2rem; }
        .subtitle { font-size:1rem; }
      }
    </style>

    <div class="container">
      <div class="title">🇮🇳 Demographix Dashboard</div>
      <div class="subtitle">
        Your one‑stop portal for exploring Census, Crime, Health & Budget insights at the district level.
      </div>

      <div class="grid">
        <div class="card">
          <i class="fas fa-users"></i>
          <h3>Census & Demographics</h3>
          <p>Population, literacy, gender ratio & infrastructure data straight from Census 2011.</p>
        </div>

        <div class="card">
          <i class="fas fa-shield-alt"></i>
          <h3>Crime Data</h3>
          <p>District‑wise NCRB crime patterns—identify hotspots and trends with ease.</p>
        </div>

        <div class="card">
          <i class="fas fa-heartbeat"></i>
          <h3>Health & Nutrition</h3>
          <p>Analyze NFHS‑5 indicators: maternal health, child nutrition, immunization & more.</p>
        </div>

        <div class="card">
          <i class="fas fa-rupee-sign"></i>
          <h3>Budget & Spending</h3>
          <p>Track financial allocations, GVA contributions & scheme effectiveness.</p>
        </div>
      </div>

      <div class="footer">
        © 2025 • Made with ❤️ by <strong>@Megh Bavarva</strong>
      </div>
    </div>
    """

    # embed it
    components.html(html, height=650, width=2500, scrolling=True)



if option =='Census Data':
    
    # Load the revelant dataset
    df = pd.read_csv('india_data.csv')

    st.set_page_config(layout="wide")

    # Extract unique states
    listOfStates = list(df['State'].unique())
    listOfStates.insert(0, 'Overall India')
    
    # get parameter values
    primaryParameters = list(df.columns[5:127])
    secondaryParameters = list(df.columns[5:127])


    # Sidebar Inputs
    selected_state = st.sidebar.selectbox("Select a State", listOfStates)
    primary = st.sidebar.selectbox("Select Primary Parameter", primaryParameters)
    secondary = st.sidebar.selectbox("Select Secondary Parameter", secondaryParameters)
    plot = st.sidebar.button("Plot Graph")



    # Top 5 values for  primary parameter of state
    top5_primary = df[df['State'] == selected_state] .sort_values(by=primary, ascending=False).head()[['District', primary]]
    top5_primary.index = range(1, len(top5_primary) + 1)
    top5_primary.index.name = "Rank"

    # Top 5 values for  secondary parameter of state
    top5_secondary = df[df['State'] == selected_state] .sort_values(by=secondary, ascending=False) .head()[['District', secondary]]
    top5_secondary.index = range(1, len(top5_secondary) + 1)
    top5_secondary.index.name = "Rank"


    # Top 5 values for  primary parameter of India
    top5_primary_overall = df.groupby('State')[primary].sum().reset_index() .sort_values(by=primary, ascending=False).head()
    top5_primary_overall.index = range(1, len(top5_primary_overall) + 1)
    top5_primary_overall.index.name = "Rank"

    # Top 5 values for  secondary parameter of India
    top5_secondary_overall = df.groupby('State')[secondary].sum().reset_index().sort_values(by=secondary, ascending=False).head()
    top5_secondary_overall.index = range(1, len(top5_secondary_overall) + 1)
    top5_secondary_overall.index.name = "Rank"



    # Title for census dashboard
    st.title("Indian Census")
    
    # when we not plot the graph we need to show a frontpage for census dashborad
    if not plot:
        
        st.markdown("""
        ---
        ### 🧠 What is Demographix?

        **Demographix** is an interactive, district-level data visualization platform built to help users explore and analyze demographic, health, infrastructure, and development indicators from the **Indian Census and public datasets**. 

        With a simple yet powerful interface, it transforms complex tabular data into dynamic maps. Each district is represented as a **bubble on the map**, making it easy to see patterns, compare regions, and draw meaningful insights about India's population and development landscape.

        Whether you're comparing literacy rates, access to toilets, electricity, or housing conditions, Demographix gives you a geographic and visual perspective on how India performs — across **28 states, 8 UTs, and over 600 districts**.

        ---

        ### 🎯 Why This Dashboard?

        Raw data tables can be overwhelming and uninspiring. Demographix bridges that gap by offering a **visual and interactive experience**. It is perfect for:

        - 📚 **Students and researchers** exploring population trends or doing social science projects
        - 🧑‍⚖️ **Policy makers and NGOs** planning welfare or development programs
        - 📊 **Journalists and data analysts** seeking stories hidden in the numbers
        - 👨‍👩‍👧‍👦 **General public** interested in their district’s data and comparison with others

        This tool democratizes census data by making it accessible, engaging, and insightful for everyone.

        ---

        ### 🔎 How to Use Demographix

        Use the **left sidebar panel** to customize your visualization:

        1. **Select a State**: View data from a specific state or explore "Overall India"
        2. **Choose a Primary Parameter**: This controls the **size** of each district’s bubble
        3. **Choose a Secondary Parameter**: This determines the **color** of the bubbles
        4. Click **"Plot Graph"** to view the map

        You can zoom, pan, and hover over any bubble to see the name of the district and the actual values for the selected parameters.

        ---

        ### 🧰 Tech Stack

        - 🐍 **Python** for scripting and data processing  
        - 📦 **Pandas & NumPy** for data wrangling  
        - 📊 **Plotly Express (Mapbox)** for geospatial visualization  
        - 🌐 **Streamlit** for building the user interface  
        - 🗺️ **OpenStreetMap / Carto-positron** as the basemap style

        The entire platform is lightweight, fast, and runs directly in the browser — no special tools required.

        ---

        ### 🙌 Why It Matters

        Data transparency and awareness are cornerstones of progress. Tools like Demographix bring powerful, actionable insights to **citizens**, **leaders**, and **communities**. 

        You don’t need to be a data scientist to understand trends like:
        - Which districts have the least access to sanitation?
        - Where is literacy high but healthcare poor?
        - Which regions need infrastructure prioritization?

        Use this dashboard to **explore, question, and act**.

        """)

        st.markdown("""
        ---
        ### 👨‍💻 Created by [Megh Bavarva](https://github.com/MeghOffical)

        This project is open-source and driven by a passion for data, civic technology, and public insight.  
        """)
    

    
    # when we plot the graph
    if plot:
        
        # if option selected is india
        if selected_state == 'Overall India':
            with st.spinner("Loading map..."):
                fig = px.scatter_mapbox(
                    df,
                    lat='Latitude',
                    lon='Longitude',
                    size=primary,
                    color=secondary,
                    color_continuous_scale='Plasma',
                    zoom=3.25,
                    width=1200,
                    height=600,
                    hover_name='District',
                    mapbox_style="carto-positron"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                
                st.subheader(f'Top 5  State for {primary} Parameters is : ')
                st.dataframe(top5_primary_overall)
                
                st.subheader(f'Top 5  State for {secondary} Parameters is : ')
                st.dataframe(top5_secondary_overall)


                st.markdown(f"""
                ---
                ## 📌 Interpretation Guide
                
                - The **size** of each circle (bubble) represents the **'{primary}'** parameter you selected.
                - The **color** of each bubble corresponds to the **'{secondary}'** parameter.
                - The **Plasma color scale** is used to visually distinguish values (from cool to warm tones).
                - Hover over any district to view detailed values.
                
                This visualization helps you **compare trends and disparities** across India's districts with just a glance.
                """)

         
        else:
            state_df = df[df['State'] == selected_state]
            with st.spinner("Loading map..."):
                fig = px.scatter_mapbox(
                    state_df,
                    lat='Latitude',
                    lon='Longitude',
                    size=primary,
                    color=secondary,
                    color_continuous_scale='Plasma',
                    zoom=5,
                    width=1200,
                    height=600,
                    hover_name='District',
                    mapbox_style="carto-positron"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader(f'Top 5 District for {primary} Parameters is : ')
                st.dataframe(top5_primary)
                
                st.subheader(f'Top 5 District for {secondary} Parameters is : ')
                st.dataframe(top5_secondary)

                st.markdown(f"""
                ---
                ## 📌 Interpretation Guide

                - The **size** of each circle (bubble) represents the **'{primary}'** parameter for districts in **{selected_state}**.
                - The **color** of each bubble shows the **'{secondary}'** parameter.
                - A vibrant **Plasma color map** indicates the range of values — from low (cool colors) to high (warm colors).
                - Hover over districts to get exact values.

                This allows for district-level comparisons within the selected state.

                """)



if option == 'Crime Data':
    
    # Load the revelant dataset
    df=pd.read_csv('crime_data.csv')
    
    st.set_page_config(layout="wide")    
    
    # list of year avaialable
    yearParameters=list(df['YEAR'].unique())
    year=st.sidebar.selectbox("Select a year",yearParameters)
    
    # get choosen year dataframe
    year_df=df[df['YEAR']==year]
    
     # Extract unique states
    listOfStates = list(year_df['State'].unique())
    listOfStates.insert(0, 'Overall India')
    
     # get parameter values
    primaryParameters = list(year_df.columns[1:31])
    
    # Sidebar Inputs
    selected_state = st.sidebar.selectbox("Select a State", listOfStates)
    primary = st.sidebar.selectbox("Choose a Crime Category", primaryParameters)
    plot = st.sidebar.button("Plot Graph")
    
    
     # Top 5 values for  primary parameter of state
    top5_primary = year_df[year_df['State'] == selected_state].sort_values(by=primary, ascending=False) .head()[['District', primary]]
    top5_primary.index = range(1, len(top5_primary) + 1)
    top5_primary.index.name = "Rank"
    
    
    # Top 5 values for  primary parameter of India
    top5_primary_overall = year_df.groupby('State')[primary].sum().reset_index().sort_values(by=primary, ascending=False).head()
    top5_primary_overall.index = range(1, len(top5_primary_overall) + 1)
    top5_primary_overall.index.name = "Rank"
    
    
     # Title for crime dashboard
    st.title("Crime in India")

    # when we not plot the graph we need to show a frontpage for crime dashborad
    if not plot:
        
        st.markdown("""
        ---
        ### 🚨 What is India's Crime Lens?

        **India's Crime Lens** is an interactive dashboard that enables users to explore crime patterns across Indian districts years.

        With data from **NCRB** and public crime records, this tool transforms raw reports into **visual insights**. Crimes are mapped district-wise using **bubbles and choropleths**, showing trends in **cybercrime, violence, theft, women and child safety**, and more.

        Whether you're a policymaker, student, or concerned citizen, this feature helps you **identify regional hotspots**, compare districts, and understand how crime impacts communities.

        ---
        
        ### 🎯 Why This Crime Dashboard?

        Crime data, though public, is often buried in static PDF reports and spreadsheets. This dashboard changes that by making it **accessible, visual, and actionable**.

        It is ideal for:

        - 👮 **Police departments & law enforcement** seeking spatial crime patterns  
        - 📰 **Journalists and analysts** looking for investigative angles  
        - 🎓 **Researchers and students** studying social or legal issues  
        - 🙋 **Civic activists and NGOs** working on women’s and child safety  
        - 🧑‍💼 **Policy makers** prioritizing crime prevention and resource allocation  

        With this tool, crime becomes **data to understand**, not just numbers to report.

        ---
        
        ### 🔎 How to Use the Crime Map

        Use the **sidebar panel** to adjust your exploration:

        1. **Select a State**: Zoom into a specific region  
        2. **Year Selection**: Compare crime stats across 2001 to 2012  
        3. **Choose a Crime Category**: (e.g., Cybercrime, Theft, Rape, Domestic Violence)  
        4. Click **"Plot Graph"** to generate the map  

        Each bubble shows the intensity of crime (via size and color). Hover for exact values and district names.

        ---
        
        ### 🧰 Tech Stack

        - 📊 **NCRB & Public Crime Reports** 
        - 🐍 **Python**, **pandas**, **NumPy** for data wrangling  
        - 📍 **Plotly Express (Mapbox)** for crime visualizations  
        - 💻 **Streamlit** for the frontend  
        - 🌍 **Geospatial matching** using district lat/lon  

        The crime dashboard seamlessly integrates with the census and health layers of Demographix.

        ---
        
        ### ⚠️ Why Crime Data Matters

        Crime affects lives, livelihoods, and trust in institutions. By visualizing crime:

        - 📌 We spotlight **vulnerable districts**
        - 🧭 We guide **policy and police response**
        - 💡 We raise **public awareness**
        - 📈 We track **trends** and **improvement zones**

        This tool helps you **see where change is needed most**.

        ---
        
        ### 👨‍💻 Created by [Megh Bavarva](https://github.com/MeghOffical)

        Part of the **Demographix** initiative to promote **open data**, **visual insight**, and **citizen empowerment**.

        """)


    # when we plot the graph
    if plot:
        
        # if option selected is india
        if selected_state == 'Overall India':
            with st.spinner("Loading map..."):
                fig = px.scatter_mapbox(
                    year_df,
                    lat='Latitude',
                    lon='Longitude',
                    size=primary,
                    color=primary,
                    color_continuous_scale='Plasma',
                    zoom=3.25,
                    width=1200,
                    height=600,
                    hover_name='District',
                    mapbox_style="carto-positron"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                
                st.subheader(f'Top 5  State for {primary} Crime Category is : ')
                st.dataframe(top5_primary_overall)
                

                st.markdown(f"""
                ---
                ## 📌 Interpretation Guide
                
                - The **size** of each circle (bubble) represents the **'{primary}'** crime category you selected.
                - The **Plasma color scale** is used to visually distinguish values (from cool to warm tones).
                - Hover over any district to view detailed values.
                
                This visualization helps you **compare trends and disparities** across India's districts with just a glance.
                """)


        else:
            state_df = year_df[year_df['State'] == selected_state]
            with st.spinner("Loading map..."):
                fig = px.scatter_mapbox(
                    state_df,
                    lat='Latitude',
                    lon='Longitude',
                    color=primary,
                    size=primary,
                    color_continuous_scale='Plasma',
                    zoom=5,
                    width=1200,
                    height=600,
                    hover_name='District',
                    mapbox_style="carto-positron"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader(f'Top 5 District for {primary} Crime Category is : ')
                st.dataframe(top5_primary)

                st.markdown(f"""
                ---
                ## 📌 Interpretation Guide

                - The **size** of each circle (bubble) represents the **'{primary}'** crime category for districts in **{selected_state}**.
                - A vibrant **Plasma color map** indicates the range of values — from low (cool colors) to high (warm colors).
                - Hover over districts to get exact values.

                This allows for district-level comparisons within the selected state.

                """)
                
                
                
if option == 'Health and Nutrition Data':
    
    # Load the revelant dataset
    df = pd.read_csv('health_data.csv')

    st.set_page_config(layout="wide")

    # Extract unique states
    listOfStates = list(df['State'].unique())
    listOfStates.insert(0, 'Overall India')

    # get parameter values
    primaryParameters = list(df.columns[2:109])
    secondaryParameters = list(df.columns[2:109])
    
    # Sidebar Inputs
    selected_state = st.sidebar.selectbox("Select a State", listOfStates)
    primary = st.sidebar.selectbox("Select Primary Parameter", primaryParameters)
    # optional secondary parameters
    use_secondary = st.sidebar.checkbox("Use Secondary Parameter?", value=True)
    plot = st.sidebar.button("Plot Graph")

    
    if use_secondary:
        secondary = st.sidebar.selectbox("Select Secondary Parameter (Bubble Color)", secondaryParameters)  
    else:
        secondary = None
        
        
    # Top 5 values for  primary parameter of state
    top5_primary = df[df['State'] == selected_state] .sort_values(by=primary, ascending=False).head()[['District', primary]]
    top5_primary.index = range(1, len(top5_primary) + 1)
    top5_primary.index.name = "Rank"


    # Top 5 values for  primary parameter of India
    top5_primary_overall = df.groupby('State')[primary].sum().reset_index() .sort_values(by=primary, ascending=False).head()
    top5_primary_overall.index = range(1, len(top5_primary_overall) + 1)
    top5_primary_overall.index.name = "Rank"


    # Title for Health dashboard
    st.title('Healthy Bharat')
    
    
    # when we not plot the graph we need to show a frontpage for census dashborad
    if not plot:
        
        st.markdown("""
        ---
        ### 🧬 India’s Health & Nutrition Pulse

        Part of the **Demographix** initiative to promote **open data**, **visual insight**, and **citizen empowerment**, this dashboard brings to life critical **Health and Nutrition indicators** at the **district level** across India, powered by the **NFHS-5 survey**.

        With a clean interface and powerful geospatial visualization, this tool enables you to explore patterns in child health, women's well-being, vaccination coverage, malnutrition, and more — across **700+ districts**.

        Whether you're a policymaker looking at anemia hotspots, or a student comparing female literacy vs institutional births, this platform gives you the map and numbers to explore, analyze, and act.

        ---

        ### 🎯 Why This Matters

        India's progress in health is complex and varied. Some districts lead in maternal health and immunization, while others face challenges in nutrition or child mortality.

        This dashboard helps:
        - 👩‍⚕️ **Health officials & NGOs** plan better interventions
        - 🧑‍🎓 **Students & researchers** study patterns in gender, income, and health
        - 🧭 **Policymakers** prioritize districts needing urgent attention
        - 🧒 **Citizens** understand health outcomes in their region

        Health data can be life-changing — when it's accessible and visible.

        ---

        ### 🔎 How to Use This Tool

        In the **left sidebar panel**, you can:

        1. **Select a State** or view pan-India data
        2. **Choose a Primary Parameter**: determines the **bubble size**
        3. **(Optional)** Choose a Secondary Parameter: controls the **color**
        4. Click **"Plot Graph"** to generate the interactive health map

        Hover over each district’s bubble to get actual indicator values — like percentage of stunted children, institutional deliveries, anemia prevalence, or family planning adoption.

        ---

        ### 📚 What’s Inside the Data

        Data is from the **National Family Health Survey (NFHS-5)** — India's premier source for district-level health stats. Indicators include:

        - 🧒 Child health (stunting, wasting, underweight, mortality)
        - 💉 Vaccination coverage (BCG, polio, DPT, measles)
        - 👩‍🍼 Women's health (anemia, contraception, maternal care)
        - 🏥 Institutional births, antenatal checkups, infant mortality
        - 💧 Household amenities related to hygiene & drinking water

        You can compare **health vs development** and see how education, gender, and geography affect wellness.

        ---

        ### 🛠️ Powered By

        - 🐍 Python + Pandas for data prep  
        - 📍 Plotly + Mapbox for interactive maps  
        - 🧱 Streamlit for building the UI  
        - 🗺️ District-wise geolocation centroids  

        The dashboard is **lightweight**, **interactive**, and works in your browser — no installations needed.

        ---

        ### 🌱 Let's Build a Healthier India

        Understanding health at the **district level** is key to targeted action.

        With Demographix, you can uncover answers like:
        - Which districts have high anemia but good sanitation?
        - Are female health outcomes better in educated regions?
        - Where is child malnutrition improving?

        Explore the stories that data tells — and become part of the change.

        """)

        st.markdown("""
        ---
        ### 👨‍💻 Created by [Megh Bavarva](https://github.com/MeghOffical)

        This open-source dashboard is part of a broader mission to make data accessible and actionable for all.  
        """)
        
        
    
    if plot:
        
        # if secondary parameter is selected
        if secondary:
            
            # Top 5 values for  secondary parameter of State
            top5_secondary = df[df['State'] == selected_state] .sort_values(by=secondary, ascending=False) .head()[['District', secondary]]
            top5_secondary.index = range(1, len(top5_secondary) + 1)
            top5_secondary.index.name = "Rank"
        
            # Top 5 values for  secondary parameter of India
            top5_secondary_overall = df.groupby('State')[secondary].sum().reset_index().sort_values(by=secondary, ascending=False).head()
            top5_secondary_overall.index = range(1, len(top5_secondary_overall) + 1)
            top5_secondary_overall.index.name = "Rank"   
            
            # if india is selected
            if selected_state == 'Overall India':
                with st.spinner("Loading map..."):
                    fig = px.scatter_mapbox(
                        df,
                        lat='Latitude',
                        lon='Longitude',
                        size=primary,
                        color=secondary,
                        color_continuous_scale='Plasma',
                        zoom=3.25,
                        width=1200,
                        height=600,
                        hover_name='District',
                        mapbox_style="carto-positron"
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    
                    st.subheader(f'Top 5  State for {primary} Parameters is : ')
                    st.dataframe(top5_primary_overall)
                    
                    st.subheader(f'Top 5  State for {secondary} Parameters is : ')
                    st.dataframe(top5_secondary_overall)


                    st.markdown(f"""
                    ---
                    ## 📌 Interpretation Guide
                    
                    - The **size** of each circle (bubble) represents the **'{primary}'** parameter you selected.
                    - The **color** of each bubble corresponds to the **'{secondary}'** parameter.
                    - The **Plasma color scale** is used to visually distinguish values (from cool to warm tones).
                    - Hover over any district to view detailed values.
                    
                    This visualization helps you **compare trends and disparities** across India's districts with just a glance.
                    """)


            else:
                state_df = df[df['State'] == selected_state]
                with st.spinner("Loading map..."):
                    fig = px.scatter_mapbox(
                        state_df,
                        lat='Latitude',
                        lon='Longitude',
                        size=primary,
                        color=secondary,
                        color_continuous_scale='Plasma',
                        zoom=5,
                        width=1200,
                        height=600,
                        hover_name='District',
                        mapbox_style="carto-positron"
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    st.subheader(f'Top 5 District for {primary} Parameters is : ')
                    st.dataframe(top5_primary)
                    
                    st.subheader(f'Top 5 District for {secondary} Parameters is : ')
                    st.dataframe(top5_secondary)

                    st.markdown(f"""
                    ---
                    ## 📌 Interpretation Guide

                    - The **size** of each circle (bubble) represents the **'{primary}'** parameter for districts in **{selected_state}**.
                    - The **color** of each bubble shows the **'{secondary}'** parameter.
                    - A vibrant **Plasma color map** indicates the range of values — from low (cool colors) to high (warm colors).
                    - Hover over districts to get exact values.

                    This allows for district-level comparisons within the selected state.

                    """)

            
        # if secondary parameter is not selected
        else:
            
            # if india is selected
            if selected_state == 'Overall India':
                with st.spinner("Loading map..."):
                    fig = px.scatter_mapbox(
                        df,
                        lat='Latitude',
                        lon='Longitude',
                        size=primary,
                        color_continuous_scale='Plasma',
                        zoom=3.25,
                        width=1200,
                        height=600,
                        hover_name='District',
                        mapbox_style="carto-positron"
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    
                    st.subheader(f'Top 5  State for {primary} Parameters is : ')
                    st.dataframe(top5_primary_overall)

                    st.markdown(f"""
                    ---
                    ## 📌 Interpretation Guide
                    
                    - The **size** of each circle (bubble) represents the **'{primary}'** parameter you selected.
                    - The **Plasma color scale** is used to visually distinguish values (from cool to warm tones).
                    - Hover over any district to view detailed values.
                    
                    This visualization helps you **compare trends and disparities** across India's districts with just a glance.
                    """)


            else:
                state_df = df[df['State'] == selected_state]
                with st.spinner("Loading map..."):
                    fig = px.scatter_mapbox(
                        state_df,
                        lat='Latitude',
                        lon='Longitude',
                        size=primary,
                        color_continuous_scale='Plasma',
                        zoom=5,
                        width=1200,
                        height=600,
                        hover_name='District',
                        mapbox_style="carto-positron"
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    st.subheader(f'Top 5 District for {primary} Parameters is : ')
                    st.dataframe(top5_primary)
                    

                    st.markdown(f"""
                    ---
                    ## 📌 Interpretation Guide

                    - The **size** of each circle (bubble) represents the **'{primary}'** parameter for districts in **{selected_state}**.
                    - The **color** of each bubble shows the **'{secondary}'** parameter.
                    - A vibrant **Plasma color map** indicates the range of values — from low (cool colors) to high (warm colors).
                    - Hover over districts to get exact values.

                    This allows for district-level comparisons within the selected state.

                    """)
                    
                    
                    
if option == 'Budget Data':
    
    # Load the revelant dataset
    df = pd.read_csv('budget_data.csv')

    st.set_page_config(layout="wide")

    # Extract unique states
    listOfStates = list(df['State'].unique())
    listOfStates.insert(0, 'Overall India')

    # Sidebar Inputs
    primaryParameters = list(df.columns[5:20])
    secondaryParameters = list(df.columns[5:20])
    
    # Sidebar Inputs
    selected_state = st.sidebar.selectbox("Select a State", listOfStates)
    primary = st.sidebar.selectbox("Select Primary Parameter", primaryParameters)
    secondary = st.sidebar.selectbox("Select Secondary Parameter", secondaryParameters)
    plot = st.sidebar.button("Plot Graph")
    
    
    # Ensure uniqueness for districts in the selected state
    unique_districts = df[df['State'] == selected_state].drop_duplicates(subset=['State', 'District'])

    # Top 5 values for  primary parameter of state
    top5_primary = unique_districts.sort_values(by=primary, ascending=False).head()[['District', primary]]
    top5_primary.index = range(1, len(top5_primary) + 1)
    top5_primary.index.name = "Rank"

    # Top 5 values for  secondary parameter of state
    top5_secondary = unique_districts.sort_values(by=secondary, ascending=False).head()[['District', secondary]]
    top5_secondary.index = range(1, len(top5_secondary) + 1)
    top5_secondary.index.name = "Rank"



    # Ensure uniqueness for state in the India
    unique_states = df.drop_duplicates(subset=['State'])

    # Top 5 values for  primary parameter of India
    top5_primary_overall = unique_states.groupby('State')[primary].sum().reset_index().sort_values(by=primary, ascending=False).head()
    top5_primary_overall.index = range(1, len(top5_primary_overall) + 1)
    top5_primary_overall.index.name = "Rank"

    # Top 5 values for  secondary parameter of India
    top5_secondary_overall = unique_states.groupby('State')[secondary].sum().reset_index().sort_values(by=secondary, ascending=False).head()
    top5_secondary_overall.index = range(1, len(top5_secondary_overall) + 1)
    top5_secondary_overall.index.name = "Rank"



    # Title for census dashboard
    st.title("Indian Budget")
    
    
    # when we not plot the graph we need to show a frontpage for budget dashborad
    if not plot:
       st.markdown("""
            ### 🏛️ What is SectorView?

            **SectorView** is a deep-dive module of the **Demographix** dashboard that focuses on the **economic and sectoral performance** of Indian districts. It uses detailed GVA (Gross Value Added) data under **Primary, Secondary, and Tertiary sectors** at both **Constant and Current Prices** to give a clear picture of how districts and states contribute to India's economy.

            It allows you to analyze key economic indicators for **all Indian states and their districts** across years, providing insight into industrial growth, agricultural strength, and service sector development.

            ---

            ### 🎯 Why This Module?

            Economic planning and investment require district-level intelligence. This tool helps uncover:

            - 📈 **Which districts are driving economic growth?**
            - 🏭 **Is a district agriculture-heavy or service-dominated?**
            - 🔄 **How has the economy shifted over time?**

            Whether you're a **policy analyst**, **economics student**, or **development researcher**, SectorView provides **powerful visualization** of India’s localized economy.

            ---

            ### 🔎 How to Use SectorView

            Use the **left panel** to customize your view:

            1. **Select a State**: Choose the region you want to analyze.
            2. **Select Primary Parameter**: Determines the size of each bubble (e.g., Primary Sector GVA).
            3. **Select Secondary Parameter**: Determines the bubble color (e.g., Tertiary Sector GVA).
            4. Click **"Plot Graph"** to visualize the data.

            Each bubble represents a district. Hover to explore detailed values for selected parameters. Pan and zoom for focused exploration.

            ---

            ### 📦 Dataset Used

            This module is powered by the dataset:  
            **District-Wise Sectoral Analysis of Indian States**  
            📁 Contains district-level GVA data in Crores ₹ across sectors and years  
            📅 Covers data from **current-years**, using both **constant** and **current** prices  
            🗃️ Includes GDP shares from **Agriculture, Industry, Services**

            ---

            ### 🛠 Tech Stack

            - 🐍 **Python** for data processing  
            - 📊 **Pandas, NumPy** for handling tabular data  
            - 🌍 **Plotly Express + Mapbox** for geospatial visualization  
            - ⚙️ **Streamlit** for web app interactivity

            ---

            ### 🤝 Impact & Use-Cases

            - 🏛️ For **governments and think tanks** to understand regional performance  
            - 🧾 For **budget planning** at local levels  
            - 🎓 For **students and researchers** exploring India's economic landscape  
            - 💼 For **business strategists** identifying emerging district economies

            Use this dashboard to **explore, compare, and act** on India's decentralized economic data.

            ---

            ### 👨‍💻 Created by [Megh Bavarva](https://github.com/MeghOffical)

            Part of the open-source **Demographix** ecosystem, this project aims to make public data **transparent**, **visual**, and **useful** for every Indian.
            """)

    

    
    if plot:
        
        # if india is selected
        if selected_state == 'Overall India':
            with st.spinner("Loading map..."):
                fig = px.scatter_mapbox(
                    df,
                    lat='Latitude',
                    lon='Longitude',
                    size=primary,
                    color=secondary,
                    color_continuous_scale='Plasma',
                    zoom=3.25,
                    width=1200,
                    height=600,
                    hover_name='District',
                    mapbox_style="carto-positron"
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                
                st.subheader(f'Top 5  State for {primary} Parameters is : ')
                st.dataframe(top5_primary_overall)
                
                st.subheader(f'Top 5  State for {secondary} Parameters is : ')
                st.dataframe(top5_secondary_overall)


                st.markdown(f"""
                ---
                ## 📌 Interpretation Guide
                
                - The **size** of each circle (bubble) represents the **'{primary}'** parameter you selected.
                - The **color** of each bubble corresponds to the **'{secondary}'** parameter.
                - The **Plasma color scale** is used to visually distinguish values (from cool to warm tones).
                - Hover over any district to view detailed values.
                
                This visualization helps you **compare trends and disparities** across India's districts with just a glance.
                """)


        else:
            
            state_df = df[df['State'] == selected_state]
            with st.spinner("Loading map..."):
                fig = px.scatter_mapbox(
                    state_df,
                    lat='Latitude',
                    lon='Longitude',
                    size=primary,
                    color=secondary,
                    color_continuous_scale='Plasma',
                    zoom=5,
                    width=1200,
                    height=600,
                    hover_name='District',
                    mapbox_style="carto-positron"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader(f'Top 5 District for {primary} Parameters is : ')
                st.dataframe(top5_primary)
                
                st.subheader(f'Top 5 District for {secondary} Parameters is : ')
                st.dataframe(top5_secondary)

                st.markdown(f"""
                ---
                ## 📌 Interpretation Guide

                - The **size** of each circle (bubble) represents the **'{primary}'** parameter for districts in **{selected_state}**.
                - The **color** of each bubble shows the **'{secondary}'** parameter.
                - A vibrant **Plasma color map** indicates the range of values — from low (cool colors) to high (warm colors).
                - Hover over districts to get exact values.

                This allows for district-level comparisons within the selected state.

                """)


    
    

