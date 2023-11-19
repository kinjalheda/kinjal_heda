import streamlit as st

# Title
st.title("To determine the total hardness of a given water sample")

# First concept
st.subheader("Prior Concept:")
st.write("Hard water, effect of hard water, hardness causing agents.")

# Second concept
st.subheader("New Concepts:")
st.write("Complex formation, EDTA, EBT, Ligand")

st.subheader("Proposition1:")
st.write("Hardness of water is due to the presence of Ca and Mg salts in it.")







st.subheader("Proposition 2:")
st.write("(Disodium salt of ethylene diamine tetra acetic acid) is used for determination of hardness by virtue of its stability and its complex forming efficiency with Ca2+ and Mg2+ from hard water. EBT (Eriochrome black-T) is used as an indicator in above complexometric titration. EBT forms wine red complex with Ca/Mg ions. Addition of EDTA displaces these ions and formation of colorless EDTA-M complex with regeneration of blue colored dye takes place. This change in color from red to blue marks the end point of titration.")





st.subheader("Proposition 3:")
st.write("From the amount (ml) of standard solution of disodium-EDTA required during complexometric titration with hard water, the amount of hardness present in hard water sample (in ppm) is calculated.")






st.header("Information Input:")
st.subheader("1)Chemical Reactions")



st.subheader("2)Structure of Metal-EDTA Complex:")



# Chemicals
st.subheader("Chemicals:")
st.write("EDTA, Eriochrome black T, ZnSO4, hard water sample.")

# Apparatus
st.subheader("Apparatus:")
st.write("Burette, pipette, conical flask, etc")

# Stepwise Procedure
st.header("Stepwise Procedure:")
st.subheader("Part I - Standardization of EDTA solution")
st.write("Rinse and fill the burette with a little quantity of EDTA and fill it up to the mark. "
         "Pipette out 10ml ZnSO4 solution and add into it 5 ml of buffer solution having pH 10. "
         "Add 4-5 drops of Eriochrome black T indicator. Titrate this solution against EDTA till "
         "the color changes to sky blue. Repeat the procedure for three times until constant readings "
         "are obtained and find out the molarity of the EDTA solution (M2).")

# NEXT Button
st.subheader("Part II - Determination of total hardness in water:")
st.write("Fill the burette with EDTA solution up to the mark. Pipette out 10ml of water sample "
         "and add to it 5 ml of buffer solution having pH 10. Add 3-4 drops of Eriochrome black T indicator. "
         "Titrate this solution against EDTA till wine red color changes to sky blue. Repeat the procedure "
         "for three times until constant readings are obtained and find out the hardness of the water sample.")

# Observations
st.header("Observations:")
st.subheadrer("Estimation of total hardness")
st.write("1) In burette - EDTA Solution\n"
         "2) In conical flask – 10 ml hard water + 5ml buffer solution (pH 10)\n"
         "3) Indicator - 3-4 drops of Eriochrome black T\n"
         "4) End point – Wine red to sky blue")

# Given molarity of Na2-EDTA solution
st.subheader("Given molarity of Na2-EDTA solution:")
if st.button("0.01M"):
    st.write("Given molarity of Na2-EDTA solution = 0.01M")
