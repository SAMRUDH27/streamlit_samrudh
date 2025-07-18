import streamlit as st

# Display an image (replace with your actual image file name or URL)
st.image("CCD09636.JPG", caption="Welcome Home Image", use_column_width=True)

# Titles and Text
st.title("Welcome to the Streamlit App!")
st.header("This is a simple Streamlit application.")
st.subheader("Explore the features and functionalities.")
st.info("This app is designed to demonstrate the basic usage of Streamlit.")
st.write("Feel free to modify and enhance it as per your requirements.")

# Displaying a range
st.write(list(range(50)))

# Additional text content
st.markdown("**samrudh**")
st.text("my college is christ")

# Caption already given above
st.caption("This is a caption for the image above.")

# Add a button
if st.button("Click Me"):
    st.success("You clicked the button!")

# Optional footer
st.markdown("---")
st.markdown("Made with  using Streamlit")
