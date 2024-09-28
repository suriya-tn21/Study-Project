import streamlit as st

st.set_page_config(page_title = "Study Plan", layout = "wide")

pages = {
    "Home": [
        st.Page("Home.py", title = "Home")
    ],

    "Accountancy": [
        st.Page("Accountancy/achap1.py", title = "1. Fundamentals of Partnership"),
        st.Page("Accountancy/achap2.py", title = "2. Goodwill"),
        st.Page("Accountancy/achap3.py", title = "3. Change in profit Sharing Ratio"),
        st.Page("Accountancy/achap4.py", title = "4. Admission of Partner"),
        st.Page("Accountancy/achap5.py", title = "5. Retirement of Partner"),
        st.Page("Accountancy/achap6.py", title = "6. Death of Partner"),
        st.Page("Accountancy/achap7.py", title = "7. Dissolution of Partner"),
        st.Page("Accountancy/achap8.py", title = "8. Accounting for Share Capital"),
        st.Page("Accountancy/achap9.py", title = "9. Accounting for Debentures"),
        st.Page("Accountancy/achap10.py", title = "10. Financial Statements of a company"),
        st.Page("Accountancy/achap11.py", title = "11. Financial Statement Analysis"),
        st.Page("Accountancy/achap12.py", title = "12. Accounting Ratios"),
        st.Page("Accountancy/achap13.py", title = "13. Cash Flow Statement"),
        st.Page("Accountancy/achap14.py", title = "14. Tools of Financial Statement Analysis Comparative Statements and Common-Size Statements")
    ],

    "English": [
        st.Page("English/echap1.py", title = "1. The Third Level"),
        st.Page("English/echap2.py", title = "2. The Tiger King"),
        st.Page("English/echap3.py", title = "3. Journey to the end of the Earth"),
        st.Page("English/echap4.py", title = "4. The Enemy"),
        st.Page("English/echap5.py", title = "5. On the Face of It"),
        st.Page("English/echap6.py", title = "6. Memories of Childhood"),
        st.Page("English/echap7.py", title = "7. The Last Lesson"),
        st.Page("English/echap8.py", title = "8. Lost Spring"),
        st.Page("English/echap9.py", title = "9. Deep Water"),
        st.Page("English/echap10.py", title = "10. The Rattrap"),
        st.Page("English/echap11.py", title = "11. Indigo"),
        st.Page("English/echap12.py", title = "12. Poets and Pancakes "),
        st.Page("English/echap13.py", title = "13. The Interview"),
        st.Page("English/echap14.py", title = "14. Going Places"),
        st.Page("English/echap15.py", title = "15. My Mother at Sixty-Six"),
        st.Page("English/echap16.py", title = "16. Keeping Quiet"),
        st.Page("English/echap17.py", title = "17. A Thing of Beauty "),
        st.Page("English/echap18.py", title = "18. A Roadside Stand"),
        st.Page("English/echap19.py", title = "19. Aunt Jennifer’s Tigers"),
        st.Page("English/echap20.py", title = "20. Writing Stuff")   
    ],

    "Business Studies": [
        st.Page("Business Studies/bchap1.py", title = "1. Nature and Significance of Management"),
        st.Page("Business Studies/bchap2.py", title = "2. Principles of Management"),
        st.Page("Business Studies/bchap3.py", title = "3. Business Environment"),
        st.Page("Business Studies/bchap4.py", title = "4. Planning"),
        st.Page("Business Studies/bchap5.py", title = "5. Organising"),
        st.Page("Business Studies/bchap6.py", title = "6. Staffing"),
        st.Page("Business Studies/bchap7.py", title = "7. Directing"),
        st.Page("Business Studies/bchap8.py", title = "8. Controlling"),
        st.Page("Business Studies/bchap9.py", title = "9. Financial Management"),
        st.Page("Business Studies/bchap10.py", title = "10. Financial Markets"),
        st.Page("Business Studies/bchap11.py", title = "11. Marketing Management"),
        st.Page("Business Studies/bchap12.py", title = "12. Consumer Protection")
    ],
    
    "Economics": [
        st.Page("Economics/ecchap1.py", title = "1. National Income and Related Aggregates"),
        st.Page("Economics/ecchap2.py", title = "2. Money & Banking"),
        st.Page("Economics/ecchap3.py", title = "3. Determination of Income and Employment"),
        st.Page("Economics/ecchap4.py", title = "4. Government Budget and the Economy"),
        st.Page("Economics/ecchap5.py", title = "5. Balance of Payments"),
        st.Page("Economics/ecchap6.py", title = "6. Indian Economy on the Eve of Independance"),
        st.Page("Economics/ecchap7.py", title = "7. Indian Economy 1950 - 1990"),
        st.Page("Economics/ecchap8.py", title = "8. Liberalisation, Privatisation and Globalisation"),
        st.Page("Economics/ecchap9.py", title = "9. Human Capital Formation"),
        st.Page("Economics/ecchap10.py", title = "10. Rural Development"),
        st.Page("Economics/ecchap11.py", title = "11. Employment"),
        st.Page("Economics/ecchap12.py", title = "12. Environment and Sustainable Development"),
        st.Page("Economics/ecchap13.py", title = "13. Comparative Development Experiances of India and its Neighbours"),
    ],

    "Computer Science": [
        st.Page("Computer Science/cchap1.py", title = "1. Revision Tour - 1"),
        st.Page("Computer Science/cchap2.py", title = "2. Revision Tour - 2"),
        st.Page("Computer Science/cchap3.py", title = "3. Working with Functions"),
        st.Page("Computer Science/cchap4.py", title = "4. File Handling"),
        st.Page("Computer Science/cchap5.py", title = "5. Exception Handling"),
        st.Page("Computer Science/cchap6.py", title = "6. Data Structure"),
        st.Page("Computer Science/cchap7.py", title = "7. Computer Networks - 1"),
        st.Page("Computer Science/cchap8.py", title = "8. Computer Networks - 2"),
        st.Page("Computer Science/cchap9.py", title = "9. Relational Database"),
        st.Page("Computer Science/cchap10.py", title = "10. MySQL"),
        st.Page("Computer Science/cchap11.py", title = "11. MySQL with Python")
    ],
}

pg = st.navigation(pages)
pg.run()

