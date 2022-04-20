#[-----------------------=Part I=----------------------------]

#Libraries
#---------------------

import streamlit as st
import numpy as np
import pandas as pd
import plotly as plt
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

#Loading Datas
pops = pd.read_csv("DataSource/pop_sample.csv")
fems = pd.read_csv("DataSource/pop_female.csv")
males = pd.read_csv("DataSource/pop_male.csv")
sexs = pd.read_csv('DataSource/sex_population.csv')
sex_fem = pd.read_csv('DataSource/sex_fem.csv')
sex_male = pd.read_csv('DataSource/sex_male.csv')



pop = pops.loc[:,['Country Name', 'Country Code', 'YR2011',
       'YR2012', 'YR2013', 'YR2014', 'YR2015', 'YR2016', 'YR2017', 'YR2018',
       'YR2019', 'YR2020']].copy()

fem = fems.loc[:,['Country Name', 'Country Code', 'YR2011',
       'YR2012', 'YR2013', 'YR2014', 'YR2015', 'YR2016', 'YR2017', 'YR2018',
       'YR2019', 'YR2020']].copy()

male = males.loc[:,['Country Name', 'Country Code','YR2011',
       'YR2012', 'YR2013', 'YR2014', 'YR2015', 'YR2016', 'YR2017', 'YR2018',
       'YR2019', 'YR2020']].copy()

#[-----------------------=Menu=----------------------------]
with st.sidebar:
    st.markdown('<link href="https://unpkg.com/boxicons@2.1.2/css/boxicons.min.css" rel="stylesheet">',unsafe_allow_html=True)
    st.markdown("""
        <div class="container-xxl">
            <span class="title">Ingrid Cadu</span><br>
            <span class="sub-title">Data Scientist Jr.</span><br>
            <div class="social">
                <a href="https://github.com/Ingrid-0906/"><i class='bx bxl-github'></i></a>
                <a href="#"><i class='bx bxl-linkedin-square'></i></a>
            </div>
            <ul class="nav">
                <li class="nav-item">
                    <a href="#world-unployment-growth" class="nav-link" aria-current="page">Introduction</a>
                </li>
                <li class="nav-item">
                    <a href="#the-path" class="nav-link" aria-current="page">The Path</a>
                </li>
                <li class="nav-item">
                    <a href="#the-big-picture" class="nav-link" aria-current="page">The Big Picture</a>
                </li>
                <li class="nav-item">
                    <a href="#the-dilleme" class="nav-link" aria-current="page">The Dilleme</a>
                </li>
                <li class="nav-item">
                    <a href="#the-gap" class="nav-link" aria-current="page">The Gap</a>
                </li>
                <li class="nav-item">
                    <a href="#conclusion" class="nav-link" aria-current="page">Conclusion</a>
                </li>
            </ul>
        </div>
    </div>""",
        unsafe_allow_html=True)

#[-----------------------=CSS Style=----------------------------]

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

template_style="plotly_white"

#[-----------------------=Layout 1=----------------------------]

img = Image.open("./wallpaper.jpg")
st.image(img, width=800, use_column_width=True, caption="Photo by alevision.co on Unsplash")

head_col1, head_col2= st.columns(2)

#Header
#---------------------

st.header("WORLD UNEMPLOYMENT GROWTH")

head_col1, head_col2, head_col3 = st.columns(3)
head_col1.write("Mar, 27, 2022 | 5 Min. Read")
head_col2.write("Descriptive Statistics")
link1 = '[Code Source](http://github.com/...)'
head_col3.markdown(link1, unsafe_allow_html=True)
st.text("")
st.write("According to the OECD (Organisation for Economic Co-operation and Development), unemployment is people above a specified age (usually 15) not being in paid employment or self-employment but currently available for work during the reference period. It is a reality that happens in every country around the world, and even the developed ones must face this problem, not with the same aggressivity as the countries in development do. Many economists point to the source as a global recession reflection, but it is not the only main reason. One that is hidden by many is the fact of overpopulation that increases every year, as we saw in the last report. So, what is the reality of unemployment? How has it evolved over ten years?")
st.text("")
st.text("")
st.text("")


#Page one -
#---------------------
pg1_col1, pg1_col2= st.columns((1,2))

with pg1_col1:
       st.header("THE PATH")
       st.write("In 2011 the global mean was 8.16p.p. and increased consequently over two years, reaching a rate of 8.25p.p.  in 2013. It's the highest point in this frame time. After that, we see a sequential decrease, and just in 2019, we have got 7.24p.p. the lowest rate in nine years. However, along this year appeared the Covid-19, the major pandemic faced in the XX century, closing 2020 with a growth of 0.05%.")


z = {'Year': pop.columns[2:], 'Mean': np.array(np.mean(pop, axis=0)), 'Deviation': np.array(np.std(pop, axis=0))}
total = pd.DataFrame(data=z)

fig1 = px.line(total, x='Year', y='Mean', 
             labels={'Mean':' ', 'Year':' '},
             title="Global World Mean of Unemployment 2011-2020",
             width=600, height=400, template=template_style)

fig1.update_layout(template=template_style)

pg1_col2.plotly_chart(fig1)


#Page two -
#---------------------
pg2_col1, pg2_col2= st.columns((1,2))


#The big-picture
#-------------------------

b = {'name': pop['Country Name'], 'code': pop['Country Code'], 'mean': np.mean(pop, axis=1)}
pop_countries = pd.DataFrame(data=b)


#Plotting with Plotly
#-------------------------

fig2 = go.Figure(data=go.Choropleth(
    locations = pop_countries['code'],
    z = pop_countries['mean'],
    text = pop_countries['name'],
    colorscale = 'Blues',
    showlegend = False,
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_orientation="h",
))

fig2.update_layout(
    title_text="Mean of Unemployment Map Growth 2011-2020",
    width=600,
    height=420,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        lakecolor='rgb(255, 255, 255)'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        showarrow = False,
        text=" ",
    )],

)


fig2.data[0].colorbar.y=-0.2
fig2.data[0].colorbar.thickness=2

pg2_col2.plotly_chart(fig2)

with pg2_col1:
       st.header("THE BIG PICTURE")
       st.write("In the Americas, Haiti, Costa Rica, and Guyana are over 13 p.p. In Europe, North of Macedonia, Greece, and Spain are the leaders of the rank, getting over 20p.p. In the African continent, and Worldly, South Africa has the highest mean rate of unemployment mean, reaching about 26p.p. In Oceania, an island called New Caledonia has 14.59p.p of unemployed. It's the highest rate on the continent.")


#Page four -
#---------------------
pg4_col1, pg4_col2= st.columns((1,2))

with pg4_col1:
       st.header("THE DILLEME")
       st.write("The lowest that Women have gotten is 16.96 p.p. in 2018, but along this frame time, the mean was stable and had not shown a significative changing as the Men's rate. It means, Men are still a world priority of employment, and Women are in the second plan.")

fm = {'Year': fem.columns[2:], 'Population': sexs['Female Mean'], 'Unemployed': np.array(np.mean(fem, axis=0))}
female = pd.DataFrame(data=fm)
female['Percentage'] = round((female['Unemployed'] / female['Population']) * 100, 2)

ml = {'Year': fem.columns[2:], 'Population': sexs['Male Mean'], 'Unemployed': np.array(np.mean(male, axis=0))}
males = pd.DataFrame(data=ml)
males['Percentage'] = round((males['Unemployed'] / males['Population']) * 100, 2)


#PLotting
Year = ['YR2011','YR2012', 'YR2013', 'YR2014', 'YR2015', 'YR2016', 'YR2017', 'YR2018','YR2019', 'YR2020']

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=Year, y=female['Percentage'], name="Women p.p.",mode='lines', stackgroup='one',line_color='rgb(131, 90, 241)'))
fig4.add_trace(go.Scatter(x=Year, y=males['Percentage'], mode='lines', name="Men p.p.",stackgroup='one',line_color='rgb(111, 231, 219)'))


fig4.update_layout(title="Women vs. Men's Mean of Unemployment 2011-2020", width=600, height=400,legend=dict(orientation="h"),template=template_style)

pg4_col2.plotly_chart(fig4)


#Page four -
#----------------------
pg5_col1, pg5_col2= st.columns((1,2))


#Chart
#-----------
sexs['Female Unemployed'] = np.array(np.mean(fem, axis=0))
sexs['Male Unemployed'] = np.array(np.mean(male, axis=0))
sexs['Female Unemployed Rate'] = round((sexs['Female Unemployed'] / sexs['Female Mean']) * 100, 2)
sexs['Male Unemployed Rate'] = round((sexs['Male Unemployed'] / sexs['Male Mean']) * 100, 2)
sexs['Difference'] = round(sexs['Female Unemployed Rate'] - sexs['Male Unemployed Rate'], 2)

#Map
#------------
m = {'name': fem['Country Name'], 
'code': fem['Country Code'],
'Fem': np.mean(sex_fem, axis=1),
'Fem Unemp': np.mean(fem, axis=1), 
'Male': np.mean(sex_male, axis=1),
'Male Unemp': np.mean(male, axis=1)}
maps = pd.DataFrame(data=m)
maps['mal_dif'] = round((maps['Male Unemp']/maps['Male'])*100, 2)
maps['fem_dif'] = round((maps['Fem Unemp']/maps['Fem'])*100,2)
maps['diff_total'] = round(maps['fem_dif']-maps['mal_dif'],2)

fig5 = px.line(sexs, x='Year', y='Difference', 
             labels={'value':' ', 'Year':' ', 'variable':' '}, 
             title="Difference between Men and Women Unemployed by year (2011-2020)",
             width=600, height=400, template=template_style)


fig6 = go.Figure(data=go.Choropleth(
    locations = maps['code'],
    z = maps['diff_total'],
    text = maps['name'],
    colorscale = 'Blues',
    showlegend = False,
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_orientation="h",
))

fig6.update_layout(
    title_text="Difference between Women and Men Unemployed by country (2011-2020)",
    width=600,
    height=420,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        lakecolor='rgb(255, 255, 255)'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        showarrow = False,
        text=" ",
    )],

)
fig6.data[0].colorbar.y=-0.2
fig6.data[0].colorbar.thickness=2

with pg5_col1:
       st.header("THE GAP")
       st.write("Countries with negative value means they have less men unemployed than women.")
       plotted = st.radio("Select the Visualization",("By Year","By Country"))
       if plotted == "By Country":
              pg5_col2.plotly_chart(fig6)
       else:
              pg5_col2.plotly_chart(fig5)


#Conclusion
#--------------
st.header('Conclusion')
st.write("After five years with lower unemployment indices, 2020 increased by half the growth reaching about 7.75 p.p. It is a disastrous impact caused by pandemic Covid-19.")
st.write("South Africa has gotten the highest rate of unemployment in the world. Some European countries like Spain and Greece face a stable unemployment wave over these years.")
st.write("North America remains with the lowest rates in all countries, except for Greenland.")
st.write("The Men still stand as a priority for employment. However, the incidence of unemployment is more volatile for Men than Women.")
st.write("From 2013 to 2020, the difference between Women's and Men's unemployment mean rates changed roughly.")
st.write("Australia, Papua New Guinea, Canada, and the United States of America are examples of countries with the highest indices of women's unemployment.")
st.text("")
st.text("")
st.text("")

st.header("Web Source")
link1='[Unemployment](https://en.wikipedia.org/wiki/Unemployment)'
link2='[The Causes of Unemployment](https://www.mindcontroversy.com/what-are-the-causes-of-unemployment/#:~:text=The%20main%20causes%20of%20unemployment%20are%201%20Financial,and%20regulatory%20bodies.%20...%205%20Personal%20reasons.%20)'


st.markdown(link1, unsafe_allow_html=True)
st.markdown(link2, unsafe_allow_html=True)
