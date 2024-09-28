import streamlit as st
import pandas as pd

# Accounting for Share Capital
st.markdown("<h1 style='text-align: center;'>Accounting for Share Capital</h1>", unsafe_allow_html=True)

with st.expander("Meaning"):
    st.write("""Company is an artificial person, created by law having seperate entity with a perpetual succession and a common seal.""")

with st.expander("Features"):
    st.write("""1. Incorporation - Company is an artificial person created by process of law.
2. Seperate legal entity - Company is a artificial person having a legal entity seperate from its shareholders.
3. Artificial Person - In eyes of law, company is an artificial person. It can own property, enter into contract, conduct business, sue or be sued.
4. Perpetual Existence - It has perpetual succession. Life of a company ends only winding up through process of law.
5. Transferability of Shares - Shares of a company are freely transferable in case of companies listed on Stock Exchange. In case of  unlisted / private companies, it is regulates by Articles of Association of the company
6. Common Seal - Company may or may not have a common seal. It's affixed to all important documents of the company if it exists.
7. Management and Ownership - Company isnt managed by all members but by their elected representatives called Directors. Thus, management and ownership is seperate""")

with st.expander("Difference between Partnership and Company"):
    df = pd.DataFrame(
        {
            "Basis": [
                "Mode of Formation",
                "Regulatory Act",
                "Distribution of Profits",
                "Management",
                "Winding Up",
                "Stabiliy of Business"
            ],

            "Parntership": [
                "Set up by agreement among partners. Registions not mandatory under Indian Partnership Act,1932",
                "Indian Partnership Act,1932",
                "As per terms of partnership deed or equally if deed does not exist",
                "May be manages by all partners or any of them acting for all",
                "By agreement or by order of the court",
                "Affected by death, retirement or insolvency of partners"
            ],

            "Company": [
                "Set up by registeration under Companies Act 2013",
                "Companies Act 2013",
                "Board of Directors decide devidend to be paid. Interim dividend is declared by Board of Directors while Proposed dividend is declared by Shareholders",
                "Manages by Direcetors who are elected by Shareholders",
                "Only by process which's permitted by Objects Clase of its Memorandum of Association",
                "Shareholder's death, insolvency or transfer of shares do not affect continuity of company"
            ]
        }
    )
    st.dataframe(df,use_container_width=True, hide_index = True)

with st.expander("Types of Companies"):
    st.write("LAter")

with st.expander("Difference between Preferance and Equity Shares"):
    df = pd.DataFrame(
        {
            "Basis": [
                "Right to Dividend",
                "Rate of Dividend",
                "Convertability",
                "Redemption",
                "Voting Rights",
                "Repayment of Capital",
                "Rigt to participate in Management"
            ],

            "Preferance Shares": [
                "It's paid if its paid on equity shares",
                "Fixed",
                "May be converted to Equity Shares, if terms of issue so provide",
                "Redeemed on due date",
                "Only on Special Situations",
                "Repaid before Equity Share Capital i paid",
                "Don't have right"
            ],

            "Equity Shares": [
                "May or may not be paid if its paid of Preferance Shares",
                "Proposed by Board of Directors and Declared by Shareholders",
                "Not Convertable",
                "Company may buy back its equity shares",
                "In all situations",
                "Is repaid after Preferance Share Capital is paid",
                "Have the right",
            ]
        }
    )

    st.dataframe(df,use_container_width=True, hide_index = True)

with st.expander("Classification of Share Capital"):
    st.subheader("Authorised Capital")
    st.write("It's stated in Memorandum of Associaton and is the max amount that a company can issue for subscription. It's also called Nominal or Registered Capital.")

    st.subheader("Issued Capital")
    st.write("It's a past of Authorised capital that's issued for subscription. It can't be more than Authorised Share Capital.")

    st.subheader("Subscribed Capital")
    st.write("It's a part of Issued Capital which is for the time being subscribed by members of a company.")

with st.expander("Uses of Securites Premium"):
    st.write("""1. Issuing fully paid bonus shares to members.
2. Writing off preliminary expenses of company.
3. Writing off expenses of, or commission paid or discount allowed on any issue of securites or debenture of the company.
4. Providing for the premium payable on the redemption of any redeemable preferance shares or of any debentures of the company.
5. In purchasing its own shares or other securites under Section 68""")

with st.expander("Journals"):
    st.write("### Normal Journals")
    journal_entries = [
        (
            """Bank A/c                                  Dr
    To Share Application A/c""",
            "Application money received"
        ),
        (
            """Share Application A/c                     Dr
    To Share Capital A/c
    To Securities Premium A/c (if any)
    To Bank A/c (if excess)""",
            "Shares allotted and excess application money is refunded"
        ),
        (
            """Share Allotment A/c                       Dr
    To Share Capital A/c
    To Securities Premium A/c (if any)""",
            "Allotment money due"
        ),
        (
            """Bank A/c                                  Dr
    To Share Allotment A/c""",
            "Allotment money received"
        ),
        (
            """Share First Call A/c                      Dr
    To Share Capital A/c""",
            "First call money due"
        ),
        (
            """Bank A/c                                  Dr
    To Share First Call A/c""",
            "First call money received"
        ),
        (
            """Share Second and Final Call A/c           Dr
    To Share Capital A/c""",
            "Second and final call money due"
        ),
        (
            """Bank A/c                                  Dr
    To Share Second and Final Call A/c""",
            "Second and final call money received"
        ),
        (
            """Share Capital A/c                         Dr
    To Share Forfeiture A/c
    To Unpaid Calls A/c""",
            "Shares are forfeited due to non-payment of calls"
        ),
        (
            """Bank A/c                                  Dr
Share Forfeiture A/c                     Dr
    To Share Capital A/c""",
            "Forfeited shares reissued"
        ),
        (
            """Share Forfeiture A/c                      Dr
    To Capital Reserve A/c""",
            "Profit on reissue transferred to capital reserve"
        )
    ]
    
    for i, (entry, narration) in enumerate(journal_entries, 1):
        st.markdown(f"**Journal Entry {i}:**")
        st.code(entry + "\n(" + narration + ")")
        st.divider()
        
    st.write("### Calls in Arrears")
    calls_in_arrears = [
        (
            """Calls in Arrears A/c                      Dr
    To Share First Call A/c
    To Share Second and Final Call A/c""",
            "When calls are in arrears (unpaid)"
        ),
        (
            """Bank A/c                                  Dr
    To Calls in Arrears A/c""",
            "When calls in arrears are received later"
        )
    ]

    for i, (entry, narration) in enumerate(calls_in_arrears, 1):
        st.markdown(f"**Calls in Arrears Entry {i}:**")
        st.code(entry + "\n(" + narration + ")")
        st.divider()

    st.write("### Calls in Advance")
    calls_in_advance = [
        (
            """Bank A/c                                  Dr
    To Calls in Advance A/c""",
            "When calls are received in advance"
        ),
        (
            """Calls in Advance A/c                      Dr
    To Share Second and Final Call A/c""",
            "When final call is made and calls in advance is adjusted"
        )
    ]

    for i, (entry, narration) in enumerate(calls_in_advance, 1):
        st.markdown(f"**Calls in Advance Entry {i}:**")
        st.code(entry + "\n(" + narration + ")")
        st.write("---")

    st.write("### Consideration Other Than Cash")
    other_consideration = [
        (
            """Sundry Assets A/c                         Dr
Goodwill A/c (if deficit)                 Dr
    To Vendor A/c
    To Liabilities A/c (if any)
    To Capital Reserve A/c (if deficit)""",
            "(Purchase of Asset / Business)"
        ),
        (
            """Vendor A/c                                  Dr
Discount on issue of shares A/c             Dr
    To Share Capital A/c
    To Securities Premium A/c""",
            "(Shares are issued to vendors for purchase of business)"
        )
    ]

    for i, (entry, narration) in enumerate(other_consideration, 1):
        st.markdown(f"**Consideration Other Than Cash Entry {i}:**")
        st.code(entry + "\n" + narration)
        st.write("---")

st.divider()