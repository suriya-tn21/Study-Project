import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center;'>Circular Flow of Income</h1>", unsafe_allow_html=True)

with st.expander("Meaning"):
    st.write("It refers to the cycle of generation of income in the production process, its distribution among the factors of production and finally, its circulation from households to firms in the form of consumption expenditure on goods and serices produced by them.")
    st.write("""Phases of Circular Flow of Income:
1. Generation Phase - In this phase, firms produce goods and services with help of factor services
2. Distribution Phase - This phase involves flow of factor income from firms to households
3. Disposition Phase - In this phase, income received by factors of production is spent on goods and services by firms""")
    
with st.expander("Difference between Stock and Flow"):
        df = pd.DataFrame(
              {
                    "Basis":[
                          "Meaning",
                          "Time Dimension",
                          "Nature of Concept",
                    ],

                    "Stock":[
                          "Variable which is measured at a particular point of time",
                          "Done not have it",
                          "Static"
                    ],

                    "Flow":[
                          "Variable which is measured over a period of time",
                          "Has as its magnitude can be measured over a period of time",
                          "Dynamic"
                    ]
              }
        )

        st.dataframe(df,use_container_width=True, hide_index = True)

with st.expander("Difference between Real and Money Flow"):
        df = pd.DataFrame(
              {
                    "Basis":[
                          "Meaning",
                          "Kind of Exchange",
                          "Difficulty in Exchange",
                          "Other name"
                    ],

                    "Real Flow":[
                          "Flow of goods and services between firms and households",
                          "Exchange of goods and services",
                          "May be difficulties in barter system in exchange of goods and factor services",
                          "Physical Flow"
                    ],

                    "Money Flow":[
                          "Flow of money between firms and households",
                          "Exchange of Money",
                          "No Difficulty",
                          "Nominal Flow"
                    ]
              }
        )

        st.dataframe(df,use_container_width=True, hide_index = True)

with st.expander("Circular Flow In Simple Economy - 2 Sector Economy"):
    st.write("A simple economy assumes the existence of only 2 sectors - Household and Firm sector. Households are the owners of factors of production and consumers of goods and services. Firms produce goods andd services and sell them to the households.")
    st.write('''Assumptions:
1. There are only 2 sectors in economy: Households and Firms. There is no government and foreign sector.
2. Household sector supplies factor services only to firms and firms hire factor services only from households.
3. Firms produce goods and services and sell their entire output to households.
4. Households receive factor income for their services and spend the entire amount on consumption of goods and services.
5. There are no savings in an economy. ''')
    
    st.image("Economics\\2sectoreconomy.jpg")
    
    st.write("The outer loop of diagram shows the real flow.")
    st.write("The inner loop of diagram shows the money flow.")

    st.write('''Conclusion:
1. Total Production of goods and services by Firms = Total Comsumption of goods and services by Households
2. Factor Payments by Firms = Factor Incomes of Households
3. Consumption Expenditure by Households = Factor Income of Households
4. Real Flow = Money Flow''')
      
with st.expander("Difference between Factor Income and Transfer Income"):
      df = pd.DataFrame(
            {
                  "Basis":[
                        "Meaning",
                        "Nature",
                        "Concept",
                        "Recipient",
                        "Example"
                  ],

                  "Factor Income":[
                        "It refers to income received by factors of production for rendering factor services in the production process",
                        "Included in both National and Domestic Income",
                        "Earning concept",
                        "Received by factors of production",
                        "Rent, Wages, Interest, Profit"
                  ],

                  "Transfer Income":[
                        "It refers to income received without rendering any productive service in return",
                        "Not included in both National and Domestic Income",
                        "Receipt Conceipt",
                        "Received by households and government",
                        "Scholarship, Old age pension, Unemployment allowance"
                  ]
            }
      )

      st.dataframe(df, use_container_width=True, hide_index = True)

with st.expander("Difference between Final Goods and Intermediate Goods"):
      df = pd.DataFrame(
            {
                  "Basis":[
                        "Meaning",
                        "Nature",
                        "Value Addition",
                        "Production Boundry"
                  ],

                  "Final Goods":[
                        "Refers to those goods which are used either for consumption or for investment",
                        "Included in both National and Domestic Income",
                        "Ready to use by their final users",
                        "Crossed it"
                  ],

                  "Intermediate Goods":[
                        "Refers to those goods which are used either for resale or for further production in the same year",
                        "Not included in both National and Domestic Income",
                        "Not ready for use",
                        "Still within it",
                  ]
            }
      )

      st.dataframe(df, use_container_width=True, hide_index = True)

with st.expander("Depreciation"):
    st.write("It refers to fall in value of fixed assets due to normal wear and tear, passage of time or expected obsolescence.")

with st.expander("3 Methods of Calculating National Income"):
    st.write("Value Added Method")
    st.text("Sales + Change in Stock = Value of Output - Intermediate Consumption = GDP @ MP - Depreciation = NDP @ MP - Net Indirect Taxes = NDP @ FC + NFIA = NNP @ FC")
    st.write("Income Method")
    st.text("Compensation of Employees + Operating Surplus + Mixed Income = NDP @ FC + NFIA = NNP @ FC")
    st.write("Expenditure Method")
    st.text("Private Final Comsumption Expenditure + Government Final Comsumption Expenditure + Gross Domestic Capital Formation + Net Export = GDP @ MP")

with st.expander("Double Counting"):
    st.write("""Double counting refers to the error of including the value of intermediate goods more than once when calculating the national income. It occurs when the same output is counted multiple times at different stages of production. Since national income is only supposed to reflect the value of final goods and services produced in an economy during a given period, including intermediate goods (which are inputs for further production) results in inflated figures, giving an inaccurate measure of economic output.""")
    st.write("""Explanation:
1. Final Goods: These are products that are ready for consumption and are not used as inputs for further production.
1. Intermediate Goods: These are goods that are used in the production of final goods (e.g., raw materials).

In measuring national income, only the value of final goods should be counted, because intermediate goods are already embedded in the value of final goods. If intermediate goods are also counted separately, it leads to double counting, which overstates the national income.
""")

with st.expander("Difference between National Income at Constant and Current Price"):
      df = pd.DataFrame(
            {
                  "Basis":[
                        "Meaning",
                        "Index of Economic Growth",
                        "Causes of Change",
                        "Caluculation",
                        "Other Name"
                  ],

                  "National Income at Current Price":[
                        "Refers to money value of final goods and services produced by normal residents of a country in a year, measured at current year prices",
                        "Not a good tool",
                        "Change in Both price and quantity",
                        "Current Price x Current Quantity",
                        "Nominal National Income"
                  ],

                  "National Income at Constant Price":[
                        "Refers to money value of final goods and services produced by normal residents of a country in a year, measured at prices of base yea`r",
                        "Good tool",
                        "Change in quantity",
                        "Base Year Price x Current Quantity",
                        "Real National Income"
                  ]
            }
      )

      st.dataframe(df,use_container_width=True, hide_index = True)

with st.expander("GDP & Welfare"):
    st.write("""
1. Distribution of GDP: It's possible with rise in GDP, inequalities in distribution of income may also increase. GDP doesn't take into account charges of inequalities in distribution of income. 
2. Change in prices: If increase in GDP is due to rise in prices and not of physical output, then its an unreliable index of economic welfare.
3. Non monetary exchanges: Many activities in an economy are not evaluated in monetary terms. Such activities influence economic welfare.
4. Externalities: It refers to benefits or harms of an activity caused by a firm or on individual, for which they're not paid or penalised. Positive externalities are activities which benefit others while Negative externalities are activities which result in harm to others.
5. Rate of Population Growth: GDP doesn't consider changes in population. If rate of population growth > rate of growth of GDP, then it'll decrease per capita availability of goods and services.
6. Composition of GDP: Higher GDP will promote welfare only if increased output comprises of goods of mass consumption and essential goods. Increase of war goods doesn't lead to any direct increase in welfacre of people.""")

with st.expander("Nominal GDP vs Real GDP"):
    st.write("""Real GDP is better than Nominal GDP because:
1. Real GDP helps in determining the effect of increased production of goods and services as it's affected by change in physical output only.
2. Real GDP is a better measure to make periodic comparision.
3. Real GDP facilitates international comparision of economic performace.""")
    st.write("Real GDP = (Nominal GDP / Price Index) x 100   ")
    st.write("Nominal GDP = (Real GDP x Price Index) / 100   ")
    st.write("Price Index = (Nominal GDP / Real GDP) x 100   ")
